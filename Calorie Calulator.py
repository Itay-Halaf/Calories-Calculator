import PySimpleGUI as sg
import time

#pg.theme("DarkAmber")
layout = [
     [sg.Text("Calories Calculator"), sg.Input(key = '-IN-')],
     #[sg.InputText()],
     [sg.Text('Our output will go here',size = (30,1),key = '-OUT-')],
     [sg.Button("Start"),sg.Button("Exit")],

 ]
window = sg.Window("Calories Calculator", layout,margins= (250,250))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    window['-OUT-'].update(values['-IN-'])
    #print(values)


window.close()