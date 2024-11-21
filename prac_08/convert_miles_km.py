
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CONVERSION_RATE = 1.609


class MilesToKm(App):
    """App that converts miles to km."""
    message = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, miles):
        """Covert the mile into km."""
        self.message = str(self.convert_to_float(miles) * CONVERSION_RATE)

    def handle_increment(self, value):
        """ handle the increment"""
        miles = self.convert_to_float(self.root.ids.user_input.text) + value
        self.root.ids.user_input.text = str(miles)

    @staticmethod
    def convert_to_float(text):
        """Convert str to float and if a value error is caught return 0.0."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKm().run()