import bonus_functions
import PySimpleGUI as psg

textFile = psg.Text("Select file to compress: ")
textDestination = psg.Text("Select destination folder: ")
buttonFile = psg.FilesBrowse("Choose")
buttonDestination = psg.FolderBrowse("Choose")
inputFile = psg.InputText()
inputDestination = psg.InputText()
buttonCompress = psg.Button("Compress")
textStatus = psg.Text("")
window = psg.Window("File Compressor", layout=[[textFile, inputFile, buttonFile],
    [textDestination, inputDestination, buttonDestination],
    [buttonCompress, textStatus]])
window.read()
window.close()

# import PySimpleGUI as psg
#
# inputFeet = psg.InputText("Enter feet: ")
# inputInches = psg.InputText("Enter inches: ")
# textFeet = psg.Text("Enter feet: ")
# textInches = psg.Text("Enter Inches: ")
# buttonConvert = psg.Button("Convert")
#
# window = psg.Window("Converter",
#                     layout=[[textFeet, inputFeet],
#                             [textInches, inputInches],
#                             [buttonConvert]])
# window.read()
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