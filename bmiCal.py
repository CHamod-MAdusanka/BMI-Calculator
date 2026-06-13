import FreeSimpleGUI as FSGUI

def calculate_bmi():
    # 1. වින්ඩෝ එකේ Layout එක හදමු
    layout = [
        [FSGUI.Text("Enter your weight (kg):", size=(20, 1)), FSGUI.InputText(key="-WEIGHT-")],
        [FSGUI.Text("Enter your height (m):", size=(20, 1)), FSGUI.InputText(key="-HEIGHT-")],
        [FSGUI.Button("Calculate", button_color="white on blue"), FSGUI.Button("Cancel", button_color="white on red")]
    ]

    # වින්ඩෝ එක නිර්මාණය කිරීම
    window = FSGUI.Window("BMI Calculator", layout, background_color="#2c3e50")

    while True:
        event, values = window.read()

        # වින්ඩෝ එක වැහුවොත් හෝ Cancel එබුවොත්
        if event == FSGUI.WIN_CLOSED or event == "Cancel":
            break

        # Calculate බොත්තම එබුවොත්
        if event == "Calculate":
            try:
                weight = float(values["-WEIGHT-"])
                height = float(values["-HEIGHT-"])

                if height <= 0:
                    FSGUI.popup("Error: Height must be greater than zero!", background_color="red")
                    continue

                bmi = round(weight / (height * height), 2)

                # BMI අගය අනුව කාණ්ඩය සහ පාට තීරණය කිරීම
                if bmi < 18.5:
                    category = "Underweight (බර අඩුයි)"
                    result_color = "orange"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal Weight (සාමාන්‍ය බර)"
                    result_color = "green"
                elif 25 <= bmi < 29.9:
                    category = "Overweight (බර වැඩියි)"
                    result_color = "purple"
                else:
                    category = "Obese (අධික තරබාරුයි)"
                    result_color = "red"

                # 5. ප්‍රතිඵලය Popup එකෙන් පෙන්වීම
                result_text = f"Your BMI Value is : {bmi}\n\nCategory : {category}"
                FSGUI.popup(
                    result_text,
                    title="Your BMI Result",
                    background_color=result_color,
                    text_color="white"
                )

            except ValueError:
                FSGUI.popup("Error: Please enter valid numbers!", background_color="red")

    window.close()

if __name__ == "__main__":
    calculate_bmi()