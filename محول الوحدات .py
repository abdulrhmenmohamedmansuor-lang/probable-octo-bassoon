"""محول الوحدات - قابل للتوسع عبر register()."""

class UnitConverter:
    def __init__(self):
        # كل فئة: وحدة أساسية + معاملات تحويل إليها
        self.categories: dict[str, dict] = {}

    def register_category(self, name: str, base: str, units: dict[str, float]):
        """units: {unit_name: factor_to_base}"""
        self.categories[name] = {"base": base, "units": units}

    def convert(self, category: str, value: float, from_u: str, to_u: str) -> dict:
        cat = self.categories[category]
        units = cat["units"]
        if from_u not in units or to_u not in units:
            raise ValueError("وحدة غير معروفة")
        base_val = value * units[from_u]
        result = base_val / units[to_u]
        steps = [
            f"تحويل {value} {from_u} → {to_u}",
            f"إلى الوحدة الأساسية ({cat['base']}): {base_val}",
            f"من الوحدة الأساسية إلى {to_u}: {result}",
        ]
        return {"result": result, "steps": steps}


def build_default_converter() -> UnitConverter:
    c = UnitConverter()
    c.register_category("length", "m", {
        "m": 1, "cm": 0.01, "mm": 0.001, "km": 1000,
        "inch": 0.0254, "ft": 0.3048, "mile": 1609.344,
    })
    c.register_category("mass", "kg", {
        "kg": 1, "g": 0.001, "mg": 1e-6, "ton": 1000, "lb": 0.453592,
    })
    c.register_category("time", "s", {
        "s": 1, "min": 60, "hour": 3600, "day": 86400,
    })
    c.register_category("speed", "m/s", {
        "m/s": 1, "km/h": 1/3.6, "mph": 0.44704,
    })
    c.register_category("temperature", "K", {
        # ملاحظة: التحويل الخطي لا يعمل مع الحرارة — تُعالج حالة خاصة
    })
    c.register_category("energy", "J", {
        "J": 1, "kJ": 1000, "cal": 4.184, "kWh": 3.6e6,
    })
    return c