import bonus_functions
# import PySimpleGUI as psg
# import zipfile
# import pathlib
#
#
# def make_archive(filepaths_local, directory):
#     dest_file = pathlib.Path(directory, "compressed.zip")
#     with zipfile.ZipFile(dest_file, "w") as archive:
#         for filepath in filepaths_local:
#             filepath = pathlib.Path(filepath)
#             archive.write(filepath, arcname=filepath.name)
#     return None
#
#
# textFile = psg.Text("Select file to compress: ")
# textDestination = psg.Text("Select destination folder: ")
# buttonFile = psg.FilesBrowse("Choose", key="Files")
# buttonDestination = psg.FolderBrowse("Choose", key="Folder")
# inputFile = psg.InputText()
# inputDestination = psg.InputText()
# buttonCompress = psg.Button("Compress")
# textStatus = psg.Text("", visible=False, key="status")
# window = psg.Window("File Compressor", layout=[[textFile, inputFile, buttonFile],
#     [textDestination, inputDestination, buttonDestination],
#     [buttonCompress, textStatus]])
# while True:
#     event, action = window.read()
#     match event:
#         case "Compress": #
#             try:
#                 print(f"Event: {event}")
#                 print(f"Action: {action}")
#                 filepaths = action["Files"].split(";")
#                 print(filepaths)
#                 make_archive(filepaths, action["Folder"])
#                 textStatus.update(value="Files successfully compressed", visible=True, text_color="white")
#             except:
#                 window["status"].update("An error has occurred.")
#         case psg.WIN_CLOSED:
#             break
# window.close()
# import PySimpleGUI as psg
#
#
# def convert_feet_to_meters(feet):
#     return feet / 3.281
#
#
# def convert_inches_to_meters(inches):
#     return inches / 39.37
#
#
# inputFeet = psg.InputText("0.0", key="Feet")
# inputInches = psg.InputText("0.0", key="Inches")
# textFeet = psg.Text("Enter feet: ")
# textInches = psg.Text("Enter Inches: ")
# buttonConvert = psg.Button("Convert")
# textStatus = psg.Text("", key="textStatus")
#
# window = psg.Window("Converter",
#                     layout=[[textFeet, inputFeet],
#                             [textInches, inputInches],
#                             [buttonConvert, textStatus]])
# while True:
#     event, action = window.read()
#     print(f"Event: {event}")
#     print(f"Action: {action}")
#
#     match event:
#         case "Convert":
#             try:
#                 feet = float(action["Feet"])
#                 inches = float(action["Inches"])
#                 print(f"Feet {feet}")
#                 print(f"Inches {inches}")
#                 meters = convert_feet_to_meters(feet) + convert_inches_to_meters(inches)
#                 window["textStatus"].update(f"Conversion is: {meters:0.2f} meters.")
#             except ValueError:
#                 pass
#         case psg.WIN_CLOSED:
#             break
# window.close()


# import PySimpleGUI as psg
#
# radioAmphibians = psg.Radio(text="Amphibians", group_id="animal_question")
# radioFish = psg.Radio(text="Fish", group_id="animal_question")
# radioMammals = psg.Radio(text="Mammal", group_id="animal_question")
# radioBirds = psg.Radio(text="Avian", group_id="animal_question")
# title = psg.Text("What are dolphins?")
#
# window = psg.Window("Quiz Game!",
#                     layout=[[title],
#                             [radioAmphibians],
#                             [radioBirds],
#                             [radioMammals],
#                             [radioFish]])
# window.read()
# window.close()

import PySimpleGUI as sg


def km_to_miles(km):
    return km * 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")
left_column = sg.Column([[label], [input_box]])
output = sg.Text(key="output")
right_column = sg.Column([[miles_button], [output]])

window = sg.Window('Km to Miles Converter',
                   layout=[[left_column, right_column]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                km = float(values["kms"])
                result = km_to_miles(km)
                window['output'].update(value=result)
            except ValueError:
                continue
        case sg.WIN_CLOSED:
            break

window.close()
