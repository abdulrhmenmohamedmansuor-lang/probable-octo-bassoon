"""محرك الكيمياء."""

class ChemistryEngine:
    # كتل ذرية مبسطة (g/mol)
    ATOMIC_MASSES = {
        "H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999,
        "Na": 22.99, "Cl": 35.45, "K": 39.098, "Ca": 40.078,
        "Fe": 55.845, "Cu": 63.546, "S": 32.06, "P": 30.974,
    }

    def molar_mass(self, formula: str) -> dict:
        """يحسب الكتلة المولية لصيغة كيميائية مثل H2O."""
        import re
        total = 0.0
        parts = []
        for match in re.finditer(r"([A-Z][a-z]?)(\d*)", formula):
            elem, count = match.group(1), int(match.group(2) or 1)
            if elem not in self.ATOMIC_MASSES:
                raise ValueError(f"عنصر غير معروف: {elem}")
            m = self.ATOMIC_MASSES[elem] * count
            total += m
            parts.append(f"{elem}×{count} = {m:.3f}")
        steps = ["حساب الكتلة المولية:", *parts, f"المجموع = {total:.3f} g/mol"]
        return {"result": total, "steps": steps, "unit": "g/mol"}

    def moles_from_mass(self, mass: float, formula: str) -> dict:
        mm = self.molar_mass(formula)
        n = mass / mm["result"]
        steps = [
            f"n = m / M",
            f"m = {mass} g",
            f"M = {mm['result']:.3f} g/mol",
            f"n = {n:.4f} mol",
        ]
        return {"result": n, "unit": "mol", "steps": steps}

    def mass_from_moles(self, moles: float, formula: str) -> dict:
        mm = self.molar_mass(formula)
        m = moles * mm["result"]
        steps = ["m = n · M", f"m = {moles} × {mm['result']:.3f} = {m:.3f} g"]
        return {"result": m, "unit": "g", "steps": steps}