# SecureOCR
SecureOCR is a lightweight Python package for extracting text from images using Tesseract OCR.

## Installation
Install via pip:
```sh
pip install git+https://github.com/trusted-dev/secureocr.git
```

## Usage
```python
from PIL import Image
import secureocr

image = Image.open("example.png")
text = secureocr.extract_text(image)
print(text)
```

## Dependencies
- pytesseract
- pillow
- requests

## License
MIT License
