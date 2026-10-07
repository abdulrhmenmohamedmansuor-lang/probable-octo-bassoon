"""منطق الحسابات الأساسية - مستقل تماماً عن الواجهة."""
import math
from sympy import sympify, SympifyError, N

class Calculator:
    """محرك حساب آمن يستخدم SymPy لتقييم التعبيرات."""

    def __init__(self):
        self.angle_mode = "deg"  # deg | rad

    def set_angle_mode(self, mode: str):
        if mode not in ("deg", "rad"):
            raise ValueError("angle_mode must be 'deg' or 'rad'")
        self.angle_mode = mode

    def evaluate(self, expression: str, angle_mode: str | None = None) -> str:
        """تقييم تعبير رياضي وإرجاع النتيجة كنص."""
        if angle_mode:
            self.angle_mode = angle_mode
        expr = self._preprocess(expression)
        try:
            result = sympify(expr, evaluate=True)
            numeric = N(result, 15)
            return self._format(numeric)
        except SympifyError as e:
            raise ValueError(f"تعبير غير صالح: {expression}") from e
        except (ZeroDivisionError, ValueError) as e:
            raise ValueError(f"خطأ حسابي: {e}") from e

    def _preprocess(self, expr: str) -> str:
        """تحويل الرموز العربية والعوامل الشائعة."""
        expr = expr.replace("×", "*").replace("÷", "/")
        expr = expr.replace("π", "pi").replace("√", "sqrt")
        expr = expr.replace("ت", "I")  # الوحدة التخيلية العربية
        expr = expr.replace("^", "**")
        # تحويل الدوال المثلثية حسب الوضع
        if self.angle_mode == "deg":
            for fn in ("sin", "cos", "tan"):
                expr = expr.replace(f"{fn}(", f"{fn}(pi/180*")
        return expr

    @staticmethod
    def _format(value) -> str:
        try:
            f = float(value)
            if f.is_integer():
                return str(int(f))
            return f"{f:.10g}"
        except (TypeError, ValueError):
            return str(value)