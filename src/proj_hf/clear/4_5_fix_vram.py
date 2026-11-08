"""
************************************

🧬 程式四_：追加硬體需求欄位

最基礎的推算公式如下：
算法1：VRAM需求(GB) ≒ 模型參數量(B) * ( 量化位元數(Bits) / 8 ) * 1.2預留緩衝  -- (不使用)

模型參數量(B)：模型的總參數數量，以十億為單位，[param_size_b]欄位

量化位元數(Bits)：模型的量化位元數，根據模型名稱與標籤判斷，[model_name]和[tags]欄位
    1. 16bit / 16-bit / fp16 / bf16 / bfloat16  -- 高精度，會使用更多 VRAM
    2. 8bit / 8-bit / int8 / fp8 / gptq-int8 / q8_0 / q8_k / q8_m  -- 中等精度，會使用中等量的 VRAM
    3. 4bit / 4-bit / int4 / nf4 / awq / gptq / q4_ / q4- / w4a / nvfp4  -- 低精度，會使用較少的 VRAM
    4. GGUF 格式：q3_ / q5_ / q6_  -- 根據具體格式決定 VRAM 需求

預留緩衝：為了避免 VRAM 不足，通常會預留 20% 的緩衝空間，因此乘以 1.2。

再者，為了方便使用者快速了解模型對應的 VRAM 需求
我們將 VRAM 需求分為八個等級，[vram_rank]欄位
並給予繁體中文標籤描述，[vram_tier]欄位


算法2：VRAM需求(GB) ≒ 模型參數量(B) * ( 量化位元數(Bits) / 8 ) * 2GB預留緩衝 + 1.5GB(系統開銷)
      量化位元數(Bits)：選用低精度的4bits
       -> VRAM需求(GB) ≒ 模型參數量(B) * 0.575 + 3.5
          根據此公式，我們可以快速估算出模型對應的 VRAM 需求，並將其分為八個等級，方便使用者快速了解模型對應的 VRAM 需求。
          v01：小於1B
          v02：1.1B~4B
          v03：4.1B~6B
          v04：6.1B~10B
          v05：11B~15B
          v06：16B~22B
          v07：24B~36B
          v08：37B以上

************************************
"""




import pandas as pd
import numpy as np  # 引入 np.inf 代表無限大
from proj_hf.clear import clear
from proj_hf.get_root import get_root


def read_csv(csv_path):
    try:
        return pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"❌ 錯誤：找不到原始檔案，請確認路徑：{csv_path}")
        return None

def detect_bits(model_row):
    model_name = "" if pd.isna(model_row.get("model_name")) else str(model_row["model_name"])
    model_tags = "" if pd.isna(model_row.get("tags")) else str(model_row["tags"])
    model_text = f"{model_name} | {model_tags}".lower()

    if any(marker in model_text for marker in ["16bit", "16-bit", "fp16", "bf16", "bfloat16"]):
        return 16.0

    if any(
        marker in model_text
        for marker in ["8bit", "8-bit", "int8", "fp8", "gptq-int8", "q8_0", "q8_k", "q8_m"]
    ):
        return 8.0

    if any(
        marker in model_text
        for marker in ["4bit", "4-bit", "int4", "nf4", "awq", "gptq", "q4_", "q4-", "w4a", "nvfp4"]
    ):
        return 4.0

    if "gguf" in model_text:
        if "q5_" in model_text: return 5.0
        if "q6_" in model_text: return 6.0
        if "q3_" in model_text: return 3.0
        return 4.0

    # 配合全量化 4-bit 策略，若無明確標籤，預設以最通用的 4.0 bit 做基本硬體估算基準
    return 4.0

def calculate_custom_vram(row):
    params_b = row["param_size_b"]
    bits = row["_detected_bits"]
    
    if pd.isna(params_b) or params_b < 1.0:
        return 0.0  # 小於 1B 模型屬於輕量嵌入式邊緣設備，獨立顯存直接歸零
        
    # 工業級優化公式：模型權重 (含 15% 預留) + 3.5GB 系統與長文本 KV Cache 緩衝
    vram_needed = (params_b * (bits / 8) * 1.15) + 3.5
    return round(vram_needed, 1)

def add_vram(model_csv_path):
    models_df = read_csv(model_csv_path)
    if models_df is None:
        return

    required_columns = ["model_name", "tags", "param_size_b"]
    missing_columns = [column for column in required_columns if column not in models_df.columns]
    if missing_columns:
        print(f"⚠️ 模型表缺少必要欄位：{missing_columns}")
        return

    # 清洗與轉換參數型態
    models_df["param_size_b"] = pd.to_numeric(models_df["param_size_b"], errors="coerce")
    
    # 暫存偵測到的位元數以供公式計算
    models_df["_detected_bits"] = models_df.apply(detect_bits, axis=1)
    
    # 1. 計算全新的精準 VRAM 欄位
    models_df["vram"] = models_df.apply(calculate_custom_vram, axis=1)

    # 2. 定義切分區間 (直接用你設計的精準參數量區間，俐落又直覺！)
    param_bins = [-0.1, 1.0, 4.0, 6.0, 10.0, 15.0, 22.0, 36.0, np.inf]
    
    # 3. 建立 vram_rank 欄位
    rank_labels = ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08"]
    models_df["vram_rank"] = pd.cut(models_df["param_size_b"].fillna(0), bins=param_bins, labels=rank_labels)

    # 4. 將 vram_rank 對應為模型參數量級描述，並放在 param_size_b 後
    size_tier_labels = {
        "v01": "小於1B",
        "v02": "1.1B~4B",
        "v03": "4.1B~6B",
        "v04": "6.1B~10B",
        "v05": "11B~15B",
        "v06": "16B~22B",
        "v07": "24B~36B",
        "v08": "37B以上",
    }
    if "size_tier" in models_df.columns:
        models_df.drop(columns=["size_tier"], inplace=True)
    size_tier = models_df["vram_rank"].astype("string").map(size_tier_labels)
    models_df.insert(models_df.columns.get_loc("param_size_b") + 1, "size_tier", size_tier)

    # 4. 建立 vram_tier 欄位
    tier_labels = [
        "極輕量 (1GB/微型嵌入式，智慧型手錶、無人機、電動車、監視器)",
        "手機端 (4GB/高階以上手機平板、辦公用筆電)",
        "輕薄本 (6GB/入門電競筆電)",
        "入門級 (8GB中階主流顯卡/中階主流電競筆電)",
        "進階級 (12GB中高階顯卡/高階電競筆電)",
        "主流級 (16GB高階顯卡)",
        "發燒友 (24GB旗艦單卡)",
        "工作站 (24GB旗艦多卡/企業、大學、醫院、金融專用)"
    ]
    models_df["vram_tier"] = pd.cut(models_df["param_size_b"].fillna(0), bins=param_bins, labels=tier_labels)


    # 清除暫存欄位
    models_df.drop(columns=["_detected_bits"], inplace=True)

    # 5. 儲存並印出結果
    models_df.to_csv(model_csv_path, index=False, encoding="utf-8-sig")
    print(f"🎉 size_tier、VRAM、vram_rank 與 vram_tier 欄位更新完成：{model_csv_path}")
    print(f"📊 共更新 {len(models_df)} 筆模型資料。")
    
    # 預覽新增加的雙欄位結構
    print(models_df[["model_name", "param_size_b", "size_tier", "vram", "vram_rank", "vram_tier"]].head(5))

if __name__ == "__main__":
    clear()
    project_root = get_root()
    model_csv_path = project_root / "data" / "4_dim_model.csv"
    add_vram(model_csv_path)




