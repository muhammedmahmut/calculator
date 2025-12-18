import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class Calculator(toga.App):

    def startup(self):
        self.expression = ""

        self.display = toga.TextInput(
            readonly=True,
            style=Pack(font_size=24, padding=10)
        )

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        main_box.add(self.display)

        grid = toga.Box(style=Pack(direction=COLUMN))

        row = toga.Box(style=Pack(direction=ROW))
        for i, text in enumerate(buttons):
            btn = toga.Button(
                text,
                on_press=self.on_press,
                style=Pack(flex=1, padding=5, font_size=18)
            )
            row.add(btn)

            if (i + 1) % 4 == 0:
                grid.add(row)
                row = toga.Box(style=Pack(direction=ROW))

        clear_btn = toga.Button(
            "C",
            on_press=self.clear,
            style=Pack(padding=10, font_size=18)
        )

        main_box.add(grid)
        main_box.add(clear_btn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_press(self, widget):
        if widget.text == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += widget.text

        self.display.value = self.expression

    def clear(self, widget):
        self.expression = ""
        self.display.value = ""

def main():
    return Calculator()