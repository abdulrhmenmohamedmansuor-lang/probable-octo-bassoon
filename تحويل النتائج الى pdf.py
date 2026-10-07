"""تصدير النتائج إلى PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FONT_PATH = "assets/fonts/Cairo-Regular.ttf"


class PDFExporter:
    def __init__(self, font_name: str = "Cairo"):
        self.font_name = "Helvetica"
        if os.path.exists(FONT_PATH):
            pdfmetrics.registerFont(TTFont(font_name, FONT_PATH))
            self.font_name = font_name

    def export(self, path: str, title: str, lines: list[str]):
        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        c.setFont(self.font_name, 16)
        c.drawString(2*cm, height - 2*cm, title)
        c.setFont(self.font_name, 11)
        y = height - 3.2*cm
        for line in lines:
            if y < 2*cm:
                c.showPage()
                c.setFont(self.font_name, 11)
                y = height - 2*cm
            c.drawString(2*cm, y, line)
            y -= 0.7*cm
        c.save()
        return path