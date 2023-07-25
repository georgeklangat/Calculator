from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        # Set the icon for the application window
        self.icon = "calculator2.png"

        # List of supported operators for calculations
        self.operators = ["/", "*", "+", "-"]

        # Variables to track the last operator and button pressed
        self.last_was_operator = None
        self.last_button = None

        # Create the main layout for the application
        main_layout = BoxLayout(orientation="vertical")

        # Create the text input widget to display the calculation and result
        self.solution = TextInput(background_color="black", foreground_color="white", multiline=False, halign="right",
                                  font_size=55, readonly=True)
        main_layout.add_widget(self.solution)

        # Define the layout of calculator buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["6", "5", "4", "*"],
            ["3", "2", "1", "+"],
            [".", "0", "C", "-"]
        ]

        # Create the calculator buttons and add them to the layout
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # Create the equal button for calculating the result
        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        # Get the current text in the text input
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            # Clear the text input when 'C' button is pressed
            self.solution.text = " "
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Avoid adding multiple operators consecutively
                return
            elif current == " " and button_text in self.operators:
                # If the first button pressed is an operator, ignore it
                return
            else:
                # Append the pressed button text to the current text
                new_text = current + button_text
                self.solution.text = new_text

        # Update the state variables
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        # Calculate the result and display it in the text input
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()

