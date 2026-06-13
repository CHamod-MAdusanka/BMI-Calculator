import FreeSimpleGUI as FSGUI
def calculate_bmi():
    weight_str = FSGUI.popup_get_text(
        "Enter your weight in Kilograms (kg):\n(ඔබේ බර කිලෝග්‍රෑම් වලින් ඇතුළත් කරන්න)",
        title="Step 1: Weight",
        button_color="white on blue", background_color="#2c3e50", text_color="white"
    )