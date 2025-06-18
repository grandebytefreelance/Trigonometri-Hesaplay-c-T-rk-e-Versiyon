from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class TrigonometricCalculatorApp(App):
    def build(self):
        self.title = "Trigonometrik Oran Hesaplayıcı"
        layout = BoxLayout(orientation='vertical')

        degree_label = Label(text="Derece Girin:")
        layout.add_widget(degree_label)

        self.entry_degree = TextInput()
        layout.add_widget(self.entry_degree)

        sin_button = Button(text="Sin")
        sin_button.bind(on_press=self.calculate_sin)
        layout.add_widget(sin_button)

        cos_button = Button(text="Cos")
        cos_button.bind(on_press=self.calculate_cos)
        layout.add_widget(cos_button)

        tan_button = Button(text="Tan")
        tan_button.bind(on_press=self.calculate_tan)
        layout.add_widget(tan_button)

        cot_button = Button(text="Cot")
        cot_button.bind(on_press=self.calculate_cot)
        layout.add_widget(cot_button)

        sec_button = Button(text="Sec")
        sec_button.bind(on_press=self.calculate_sec)
        layout.add_widget(sec_button)

        csc_button = Button(text="Csc")
        csc_button.bind(on_press=self.calculate_csc)
        layout.add_widget(csc_button)

        clear_button = Button(text="Temizle")
        clear_button.bind(on_press=self.clear_result)
        layout.add_widget(clear_button)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        return layout

    def calculate_sin(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        sin_value = math.sin(radians)
        self.result_label.text = f"Sin({degree}°) = {sin_value:.4f}"

    def calculate_cos(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        cos_value = math.cos(radians)
        self.result_label.text = f"Cos({degree}°) = {cos_value:.4f}"

    def calculate_tan(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        tan_value = math.tan(radians)
        self.result_label.text = f"Tan({degree}°) = {tan_value:.4f}"

    def calculate_cot(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        cot_value = 1 / math.tan(radians)
        self.result_label.text = f"Cot({degree}°) = {cot_value:.4f}"

    def calculate_sec(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        sec_value = 1 / math.cos(radians)
        self.result_label.text = f"Sec({degree}°) = {sec_value:.4f}"

    def calculate_csc(self, instance):
        degree = float(self.entry_degree.text)
        radians = math.radians(degree)
        csc_value = 1 / math.sin(radians)
        self.result_label.text = f"Csc({degree}°) = {csc_value:.4f}"

    def clear_result(self, instance):
        self.result_label.text = ""

if __name__ == '__main__':
    TrigonometricCalculatorApp().run()