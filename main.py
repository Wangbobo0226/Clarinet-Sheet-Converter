import google.generativeai as genai
import os
from PIL import Image

# 設定 API Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def convert_with_ai(image_path):
    model = genai.GenerativeModel('gemini-1.5-flash')
    img = Image.open(image_path)
    
    # 這裡就是關鍵的「指令」，直接告訴 AI 你的公式
    prompt = """
    請提取這張簡譜的主旋律數字，忽略歌詞。
    並將數字依此公式轉換：1->4, 2->5, 3->6, 4->7, 5->1, 6->2, 7->3。
    請保留小節線 |，只需給我轉換後的結果。
    """
    
    response = model.generate_content([prompt, img])
    return response.text

if __name__ == "__main__":
    print(convert_with_ai("input.jpg"))
