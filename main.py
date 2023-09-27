import pytesseract
from PIL import Image

# 画像を読み込む
image = Image.open('ss.png')

# Tesseractを使用してテキストを抽出
text = pytesseract.image_to_string(image)

# 抽出したテキストを表示
print(text)