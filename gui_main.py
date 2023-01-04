from modules import functions
import PySimpleGUI as psg
to_do_list = functions.read_to_do_list()
print(to_do_list)
label = psg.Text("Type in a to do: ")
input_box = psg.InputText(tooltip="Enter to do: ", key="add")
add_button = psg.Button("Add")
delete_button = psg.Button("Delete")
window = psg.Window("My To Do Application",
                    layout=[[label], [add_button, input_box], [delete_button]],
                    font=["Verdana", 14])
while True:
    event, action = window.read()
    print(event)
    print(action)
    match event:
        case "Add":
            to_do_list.append(action["add"])
        case psg.WIN_CLOSED:
            break
        
    functions.write_to_do_list(to_do_list_local=to_do_list)
window.close() 
