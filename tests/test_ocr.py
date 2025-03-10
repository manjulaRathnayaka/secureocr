from PIL import Image
import secureocr

def test_ocr():
    """Basic test to check OCR functionality."""
    image = Image.new("RGB", (100, 100), color="white")  # Create a blank image
    text = secureocr.extract_text(image)
    assert isinstance(text, str)  # Ensure OCR returns a string

if __name__ == "__main__":
    test_ocr()
    print("Test passed!")
