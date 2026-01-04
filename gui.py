import functions
import FreeSimpleGUI as fsg
import time

fsg.theme("DarkBlue16")

clock = fsg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="clock")
label = fsg.Text("Type in a to-do:")
input_box = fsg.InputText(tooltip="Enter a to-do", key="add_todo")
add_button = fsg.Button(button_text="Add", tooltip="Add a to-do")
listbox = fsg.Listbox(values=functions.get_todos(), key="todo_list",
                      enable_events=True, size=(45, 10))
edit_button = fsg.Button(button_text="Edit", tooltip="Edit a to-do")
complete_button = fsg.Button(button_text="Complete", tooltip="Complete a to-do")
exit_button = fsg.Button(button_text="Exit", tooltip="Exit the program")


window = fsg.Window(title='My To-Do App',
                    layout=[[clock],[label],
                            [input_box, add_button],
                            [listbox, edit_button, complete_button],
                            [exit_button]],
                    font="Helvetica, 12")
while True:
    events, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match events:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['add_todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['add_todo'].update(value='')
            window['todo_list'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todo_list'][0]
                new_todo = values['add_todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first.", title="Error", font="Helvetica, 12")
        case "Complete":
            try:
                todo_to_complete = values['todo_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_list'].update(values=todos)
                window['add_todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item first.", title="Error", font="Helvetica, 12")

        case "todo_list":
            window["add_todo"].update(value=values['todo_list'][0])

        case "Exit":
            break

        case fsg.WIN_CLOSED:
            break

window.close()