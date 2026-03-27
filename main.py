import google.generativeai as genai
import os
from PIL import Image

# 1. 安全地讀取你的 API Key (稍後我們會在終端機設定環境變數)
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    print("❌ 錯誤：找不到 API Key！請先設定 GEMINI_API_KEY 環境變數。")
    exit()

genai.configure(api_key=GOOGLE_API_KEY)

def process_sheet_music_with_ai(image_path):
    print("🤖 AI 正在讀取並思考轉換邏輯，請稍候...")
    
    # 選擇最新的 Gemini 視覺模型
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 讀取圖片
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "❌ 找不到 input.jpg 圖片檔案！"

    # ✨ 這裡就是 AI 視覺的核心：用「人類語言」下達轉換指令 (Prompt)
    prompt = """
    這是一張鋼琴簡譜。請幫我提取出「主旋律」的數字，忽略所有的中文字歌詞。
    並且直接幫我把提取出的數字進行轉換，規則如下：
    原譜的 1 轉換為 4
    原譜的 2 轉換為 5
    原譜的 3 轉換為 6
    原譜的 4 轉換為 7
    原譜的 5 轉換為 1
    原譜的 6 轉換為 2
    原譜的 7 轉換為 3
    0 保留為 0。
    
    請盡量保留原本的小節線(|)與排版，只輸出轉換後的數字結果，不要給我其他解釋或廢話。
    """

    # 把圖片和指令一起丟給 AI
    response = model.generate_content([prompt, img])
    
    return response.text

if __name__ == "__main__":
    target_image = "input.jpg"
    print("\n=== 🎷 AI 轉換後的豎笛簡譜 ===\n")
    print(process_sheet_music_with_ai(target_image))
