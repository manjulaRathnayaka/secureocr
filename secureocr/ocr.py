from PIL import Image
import secureocr

def ocr_image(image_path: str) -> str:
    """Loads an image and extracts text using OCR."""
    try:
        image = Image.open(image_path)
        return secureocr.extract_text(image)
    except Exception as e:
        return f"Error processing image: {str(e)}"

if __name__ == "__main__":
    print(ocr_image("sample_image.png"))  # Example usage
