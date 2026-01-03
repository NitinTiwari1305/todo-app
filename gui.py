import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter a to-do")
add_button = fsg.Button(button_text="Add", tooltip="Add a to-do")

window = fsg.Window(title='My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()