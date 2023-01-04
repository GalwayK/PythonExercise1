from modules import functions
import PySimpleGUI as psg

to_do_list = functions.read_to_do_list()
print(to_do_list)
label = psg.Text("Type in a to do: ")
add_input = psg.InputText(tooltip="Enter to do: ", key="add")
add_button = psg.Button("Add")
edit_input = psg.InputText(tooltip="", key="edit", visible=False)
edit_button = psg.Button("Edit", visible=False)
list_to_dos = psg.Listbox(values=to_do_list, key="list", size=(20, 10), enable_events=True)
finish_button = psg.Button("Finish", visible=False)
window = psg.Window("My To Do App",
                    layout=[[label],
                            [add_button, add_input],
                            [edit_button, edit_input],
                            [list_to_dos, finish_button]],
                    font=["Verdana", 12])
while True:
    event, action = window.read()
    print(event)
    print(action)
    match event:
        case "Add":
            to_do_list.append(action["add"])
            window["list"].update(values=to_do_list)
            add_input.update("")
            edit_input.update(visible=False)
            edit_button.update(visible=False)
            finish_button.update(visible=False)
        case "list":
            try:
                window["edit"].update(value=action["list"][0])
                edit_button.update(visible=True)
                edit_input.update(visible=True)
                finish_button.update(visible=True)
            except IndexError:
                continue
        case "Edit":
            print(action["edit"])
            to_do_list[to_do_list.index(action["list"][0])] = action["edit"]
            edit_button.update(visible=False)
            edit_input.update(visible=False)
            finish_button.update(visible=False)
            window["list"].update(values=to_do_list)
        case "Finish":
            print(action)
            to_do_list.pop(to_do_list.index(action["edit"]))
            edit_input.update(visible=False)
            edit_button.update(visible=False)
            finish_button.update(visible=True)
            window["list"].update(values=to_do_list)
        case psg.WIN_CLOSED:
            break

    functions.write_to_do_list(to_do_list_local=to_do_list)
window.close()
