"""حل المعادلات، المصفوفات، الأعداد المركبة، خطوة بخطوة."""
from sympy import (
    symbols, solve, simplify, factor, expand, Matrix,
    Eq, sympify, latex, I
)
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

TRANSFORMS = standard_transformations + (implicit_multiplication_application,)

class AlgebraEngine:
    def __init__(self):
        self.x, self.y, self.z = symbols("x y z")

    # ---------- حل المعادلات ----------
    def solve_equation(self, equation: str, var: str = "x") -> dict:
        """يحل معادلة ويعرض الخطوات."""
        eq_str = self._normalize(equation)
        if "=" in eq_str:
            lhs, rhs = eq_str.split("=")
            eq = Eq(parse_expr(lhs, transformations=TRANSFORMS),
                    parse_expr(rhs, transformations=TRANSFORMS))
        else:
            eq = Eq(parse_expr(eq_str, transformations=TRANSFORMS), 0)

        variable = symbols(var)
        solutions = solve(eq, variable)
        steps = [
            f"1) المعادلة الأصلية: {equation}",
            f"2) توحيد الطرفين: {latex(eq)}",
            f"3) الحل: {variable} = {', '.join(map(str, solutions)) or 'لا يوجد حل'}",
        ]
        return {"solutions": solutions, "steps": steps}

    def solve_quadratic(self, a: float, b: float, c: float) -> dict:
        disc = b**2 - 4*a*c
        steps = [
            f"المعادلة: {a}x² + {b}x + {c} = 0",
            f"المميز Δ = b² - 4ac = {disc}",
        ]
        if disc >= 0:
            x1 = (-b + disc**0.5) / (2*a)
            x2 = (-b - disc**0.5) / (2*a)
            sols = [x1, x2]
        else:
            real = -b / (2*a)
            imag = (-disc)**0.5 / (2*a)
            sols = [f"{real}+{imag}ت", f"{real}-{imag}ت"]
            steps.append("المميز سالب ← حلول مركبة")
        steps.append(f"الحلول: {sols}")
        return {"solutions": sols, "steps": steps}

    def solve_system(self, equations: list[str], vars_: list[str]) -> dict:
        syms = symbols(" ".join(vars_))
        eqs = []
        for eq in equations:
            if "=" in eq:
                l, r = eq.split("=")
                eqs.append(Eq(sympify(l), sympify(r)))
            else:
                eqs.append(Eq(sympify(eq), 0))
        sol = solve(eqs, syms, dict=True)
        steps = [f"النظام: {equations}", f"الحل: {sol}"]
        return {"solutions": sol, "steps": steps}

    # ---------- التبسيط والتحليل ----------
    def simplify_expr(self, expr: str) -> dict:
        e = parse_expr(self._normalize(expr), transformations=TRANSFORMS)
        s = simplify(e)
        f = factor(e)
        steps = [
            f"التعبير: {expr}",
            f"بعد التبسيط: {s}",
            f"التحليل: {f}",
        ]
        return {"simplified": s, "factored": f, "steps": steps}

    # ---------- المصفوفات ----------
    def matrix_operation(self, op: str, a: list, b: list | None = None) -> dict:
        A = Matrix(a)
        steps = [f"المصفوفة A = {A.tolist()}"]
        if op == "det":
            r = A.det()
            steps.append(f"det(A) = {r}")
        elif op == "inv":
            r = A.inv()
            steps.append(f"A⁻¹ = {r.tolist()}")
        elif op == "transpose":
            r = A.T
            steps.append(f"Aᵀ = {r.tolist()}")
        else:
            B = Matrix(b)
            steps.append(f"المصفوفة B = {B.tolist()}")
            if op == "add":
                r = A + B
            elif op == "sub":
                r = A - B
            elif op == "mul":
                r = A * B
            else:
                raise ValueError(f"عملية غير معروفة: {op}")
            steps.append(f"النتيجة = {r.tolist()}")
        return {"result": r, "steps": steps}

    def _normalize(self, expr: str) -> str:
        """دعم الحرف 'ت' للوحدة التخيلية."""
        return expr.replace("ت", "I").replace("×", "*").replace("÷", "/")