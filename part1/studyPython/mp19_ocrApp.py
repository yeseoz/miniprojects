# 글자추출
# 이미지 처리 모듈 pillow # pip install pillow
# OCR 모듈  # pip install pytesseract
# Tesseract-OCR 컴퓨터에 설치 https://github.com/UB-Mannheim/tesseract/wiki
from PIL import Image
import pytesseract as tess

img_path = './studyPython/한글이미지.png '
tess.pytesseract.tesseract_cmd = 'C:/DEV/Tools/Tesseract-OCR/tesseract.exe' # https://github.com/tesseract-ocr/tessdata

result = tess.image_to_string(Image.open(img_path), lang = 'kor')
print(result)