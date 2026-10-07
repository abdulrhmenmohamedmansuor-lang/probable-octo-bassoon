from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerMenu, MDNavigationDrawerItem
from kivymd.uix.boxlayout import MDBoxLayout

from ui.i18n import I18n
from ui.theme import apply_theme
from ui.screens.calculator_screen import CalculatorScreen

APP_VERSION = "1.0.0"


class ABScientificCalculator(MDApp):
    def build(self):
        self.title = "AB Scientific Calculator"
        self.i18n = I18n(lang="en")
        self.dark_mode = False
        apply_theme(self, dark=False)

        root = MDBoxLayout(orientation="vertical")

        self.sm = MDScreenManager()
        self.sm.add_widget(CalculatorScreen(i18n=self.i18n))

        root.add_widget(self.sm)
        return root

    def toggle_lang(self):
        new = "ar" if self.i18n.lang == "en" else "en"
        self.i18n.load(new)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        apply_theme(self, self.dark_mode)


if __name__ == "__main__":
    ABScientificCalculator().run()