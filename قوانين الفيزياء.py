"""محرك الفيزياء - بنية قابلة لإضافة قوانين جديدة بسهولة."""
from dataclasses import dataclass, field

@dataclass
class Formula:
    key: str
    name_en: str
    name_ar: str
    formula_latex: str
    variables: dict          # {"v": "السرعة (m/s)", ...}
    solve_for: str           # المتغير الناتج
    func: callable = field(repr=False, default=None)

    def compute(self, **kwargs) -> dict:
        steps = [f"القانون: {self.formula_latex}",
                 f"القيم المدخلة: {kwargs}"]
        result = self.func(**kwargs)
        steps.append(f"النتيجة: {self.solve_for} = {result}")
        return {"result": result, "steps": steps, "formula": self.formula_latex}


class PhysicsEngine:
    def __init__(self):
        self.formulas: dict[str, Formula] = {}
        self._register_defaults()

    def register(self, formula: Formula):
        self.formulas[formula.key] = formula

    def list_formulas(self) -> list[Formula]:
        return list(self.formulas.values())

    def compute(self, key: str, **kwargs) -> dict:
        if key not in self.formulas:
            raise KeyError(f"قانون غير معروف: {key}")
        return self.formulas[key].compute(**kwargs)

    def _register_defaults(self):
        self.register(Formula(
            key="velocity", name_en="Velocity", name_ar="السرعة",
            formula_latex="v = d / t",
            variables={"d": "المسافة (m)", "t": "الزمن (s)"},
            solve_for="v",
            func=lambda d, t: d / t if t else float("inf"),
        ))
        self.register(Formula(
            key="force", name_en="Force (Newton)", name_ar="القوة",
            formula_latex="F = m · a",
            variables={"m": "الكتلة (kg)", "a": "التسارع (m/s²)"},
            solve_for="F",
            func=lambda m, a: m * a,
        ))
        self.register(Formula(
            key="work", name_en="Work", name_ar="الشغل",
            formula_latex="W = F · d",
            variables={"F": "القوة (N)", "d": "الإزاحة (m)"},
            solve_for="W",
            func=lambda F, d: F * d,
        ))
        self.register(Formula(
            key="ohm", name_en="Ohm's Law", name_ar="قانون أوم",
            formula_latex="V = I · R",
            variables={"I": "التيار (A)", "R": "المقاومة (Ω)"},
            solve_for="V",
            func=lambda I, R: I * R,
        ))
        self.register(Formula(
            key="power_electric", name_en="Electric Power", name_ar="القدرة الكهربائية",
            formula_latex="P = V · I",
            variables={"V": "الجهد (V)", "I": "التيار (A)"},
            solve_for="P",
            func=lambda V, I: V * I,
        ))
        # أضف المزيد هنا بسهولة…