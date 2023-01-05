from modules import functions
import PySimpleGUI as psg
import time

to_do_list = functions.read_to_do_list()
print(to_do_list)
psg.theme("DarkBlue")
text_time = psg.Text(time.strftime("%A %B %Y"), key="Time")
label = psg.Text("Type in a to do: ")
add_input = psg.InputText(tooltip="Enter to do: ", key="add")
add_button = psg.Button("Add")
edit_input = psg.InputText(tooltip="", key="edit", visible=False)
edit_button = psg.Button("Edit", visible=False)
list_to_dos = psg.Listbox(values=to_do_list, key="list", size=(30, 10), enable_events=True)
finish_button = psg.Button("Finish", visible=False)
button_exit = psg.Button("Exit", key="Exit")
window = psg.Window("My To Do App",
                    layout=[[label],
                            [add_button, add_input],
                            [edit_button, edit_input],
                            [list_to_dos, finish_button],
                            [button_exit, text_time]],
                    font=["Verdana", 12])
while True:
    event, action = window.read(timeout=1000)
    window["Time"].update(time.strftime("%A %B %Y"))
    print(event)
    print(action)
    match event:
        case "Add":
            if action["add"]:
                to_do_list.append(action["add"])
                window["list"].update(values=to_do_list)
                add_input.update("")
                edit_input.update(visible=False)
                edit_button.update(visible=False)
                finish_button.update(visible=False)
            else:
                psg.popup("Please enter a to do item.", font=("Verdana", 12))
                continue
        case "list":
            try:
                window["edit"].update(value=action["list"][0])
                edit_button.update(visible=True)
                edit_input.update(visible=True)
                finish_button.update(visible=True)
            except IndexError:
                psg.popup("Please enter a to do item before attempting to make changes.", font=("Verdana", 12))
                continue
        case "Edit":
            if action["edit"]:
                to_do_list[to_do_list.index(action["list"][0])] = action["edit"]
                edit_button.update(visible=False)
                edit_input.update(visible=False)
                finish_button.update(visible=False)
                window["list"].update(values=to_do_list)
            else:
                psg.popup("Please enter a to do item.", font=("Verdana", 12))
        case "Finish":
            to_do_list.remove(action["edit"])
            edit_input.update(visible=False)
            edit_button.update(visible=False)
            finish_button.update(visible=False)
            window["list"].update(values=to_do_list)
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            break

    functions.write_to_do_list(to_do_list_local=to_do_list)
window.close()
