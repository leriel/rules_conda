from PIL import Image
from pathlib import Path

import pytesseract

img_path = Path(__file__).parent / "tesseract_test.png"
print(pytesseract.image_to_string(Image.open(img_path)))
