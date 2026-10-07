"""استخراج نص من صور."""
from PIL import Image
import pytesseract


class OCRReader:
    def __init__(self, tesseract_cmd: str | None = None, lang: str = "eng+ara"):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.lang = lang

    def read(self, image_path: str) -> str:
        img = Image.open(image_path)
        # تحسين بسيط
        img = img.convert("L")
        text = pytesseract.image_to_string(img, lang=self.lang)
        return self._normalize(text)

    @staticmethod
    def _normalize(text: str) -> str:
        """تنظيف النص ليصبح قابلاً للحساب."""
        replacements = {
            "×": "*", "÷": "/", "−": "-", "–": "-",
            "π": "pi", "√": "sqrt", "²": "**2", "³": "**3",
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return " ".join(text.split())