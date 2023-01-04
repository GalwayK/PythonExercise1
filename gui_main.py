import bonus_functions
import PySimpleGUI as psg

label = psg.Text("Type in a to do: ")
input_box = psg.InputText(tooltip="Enter to do: ")
add_button = psg.Button("Add")
window = psg.Window("My To Do Application", layout=[[label], [add_button, input_box]])
window.read()
window.close() 
