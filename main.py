import google.generativeai as genai
import os
from PIL import Image

# 1. 從環境變數中安全讀取 API KEY
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    print("❌ 錯誤：找不到 API Key！請先在終端機設定環境變數：export GEMINI_API_KEY='你的鑰匙'")
    exit()

# 2. 設定 Gemini
genai.configure(api_key=GOOGLE_API_KEY)

def convert_sheet_with_ai(image_path):
    print("🤖 AI 正在讀取並理解簡譜，這大約需要 10-20 秒，請稍候...")
    
    # 使用最新的 Gemini 1.5 Flash 模型 (快速且視覺能力強)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 讀取圖片
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "❌ 找不到 input.jpg 圖片檔案！"

    # ✨ 核心：撰寫高精確度的「AI 咒語 (Prompt)」
    prompt = """
    你是一位專業的音樂老師。這是一張鋼琴簡譜照片。請幫我完成以下任務：
    
    1. 忽略所有中文字歌詞和雜訊，只提取純數字的「主旋律」。
    2. 請精確地執行以下簡譜轉換公式：
       原譜的 1 -> 轉換為 4
       原譜的 2 -> 轉換為 5
       原譜的 3 -> 轉換為 6
       原譜的 4 -> 轉換為 7
       原譜的 5 -> 轉換為 1
       原譜的 6 -> 轉換為 2
       原譜的 7 -> 轉換為 3
       0 保留為 0。
    3. 轉換後的數字（特別是原本的 5, 6, 7），請依照簡譜慣例，在數字上面加一個 (') 符號代表高音。
    4. 請保留原本的小節線 (|)。
    
    只需輸出轉換後的數字結果，不要給我任何解釋。
    """

    # 把圖片和指令一起丟給 AI
    response = model.generate_content([prompt, img])
    
    return response.text

if __name__ == "__main__":
    target_image = "input.jpg"  # 確保你上傳了原始照片
    print("\n=== 🎷 AI 串接轉換後的豎笛簡譜 ===\n")
    print(convert_sheet_with_ai(target_image))
