from functools import WRAPPER_ASSIGNMENTS
from OpenVaxxDB import business as ovb
from OpenVaxxDB import distributor as ovd
from OpenVaxxDB import recipient as ovr
import PySimpleGUI as sg


# -- Colors --
bgColor1 = '#ffffff'
bgColor2 = '#0e1778'
textColor1 = '#ffffff'
textColor2 = '#0e1778'
notVaxxColor = '#e3210b'
warningColor = '#ff9d00'
fullVaxxColor = '#00b315'

# -- Window Layouts -- 
aboutPage = [[]]
recipentLogin = [[]]
distributorLogin = [[]]
businessLogin = [[]]
loginPage = [sg.Column(recipentLogin), sg.VSeparator(color=bgColor2), sg.Column(distributorLogin), 
sg.VSeparator(color=bgColor2), sg.Column(businessLogin)]
recipientPage = [[]]
distributorMain = [[]]
distributorInput = [[]]
businessMain = [[]]
businessOut = [[]]
settingsPage = [[]]
# -- New Window Functions -- 

def open_login_window():
    window = sg.Window("Login into Your Account", loginPage, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

def open_recipient_page(username):
    window = sg.Window("Welcome " + username, recipientPage)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

def open_distributor_main_page(distributor):
    window = sg.Window(distributor, loginPage, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

def open_distributor_input_page(distributor):
    window = sg.Window(distributor + "Vaccine Info Input", loginPage, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break


# Create the Window
aboutWindow = sg.Window('Window Title', aboutPage, size=(200,200))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = aboutWindow.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break 

aboutWindow.close()