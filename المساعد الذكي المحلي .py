"""مساعد ذكي محلي Offline."""
from core.algebra import AlgebraEngine
from core.calculator import Calculator


class SmartBot:
    def __init__(self, dictionary: dict, lang: str = "en"):
        self.dict = dictionary
        self.lang = lang
        self.algebra = AlgebraEngine()
        self.calc = Calculator()

    def set_language(self, lang: str):
        self.lang = lang

    def reply(self, question: str) -> str:
        q = question.strip().lower()

        # 1) بحث في القاموس
        for term, info in self.dict.items():
            if term in q:
                return self._format_term(term, info)

        # 2) محاولة حل معادلة
        if "=" in q and any(v in q for v in "xyz"):
            try:
                res = self.algebra.solve_equation(question)
                return "\n".join(res["steps"])
            except Exception:
                pass

        # 3) محاولة تقييم تعبير رقمي
        try:
            value = self.calc.evaluate(question)
            return f"النتيجة: {value}"
        except Exception:
            pass

        return ("لم أتمكن من فهم السؤال. جرّب:\n"
                "- سؤال عن مصطلح علمي\n"
                "- معادلة مثل: x^2 - 4 = 0\n"
                "- تعبير مثل: sin(30)+cos(60)")

    def _format_term(self, term: str, info: dict) -> str:
        name = info.get("ar" if self.lang == "ar" else "en", term)
        definition = info.get("definition_ar" if self.lang == "ar" else "definition_en", "")
        return f"📘 {name}\n{definition}"