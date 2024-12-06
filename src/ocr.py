from PIL import Image
import pytesseract

def extract_text(image_path):
    """
    Extrai texto de uma imagem.
    """
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text