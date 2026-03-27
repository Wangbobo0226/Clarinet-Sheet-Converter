import cv2
import pytesseract
import os

# 設定你的轉換邏輯
def convert_logic(text):
    mapping = {
        '1': '4', '2': '5', '3': '6', '4': '7',
        '5': '1', '6': '2', '7': '3', '0': '0'
    }
    return "".join([mapping.get(char, char) for char in text])

def process_image(img_path):
    # 讀取圖片並轉為灰階（增加辨識率）
    img = cv2.imread(img_path)
    if img is None: return "找不到圖片！"
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 執行 OCR 辨識數字與符號
    config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=01234567.|-'
    raw_text = pytesseract.image_to_string(gray, config=config)
    
    # 輸出轉換後的結果
    return convert_logic(raw_text)

if __name__ == "__main__":
    target_image = "input.jpg"  # 預設讀取的圖片檔名
    if os.path.exists(target_image):
        print("\n=== 🎵 轉換後的豎笛簡譜 ===\n")
        print(process_image(target_image))
    else:
        print("❌ 錯誤：請確保倉庫中有名為 'input.jpg' 的圖片檔案。")
