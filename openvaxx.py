
from OpenVaxxDB import business as ovb
from OpenVaxxDB import distributor as ovd
from OpenVaxxDB import recipient as ovr
import PySimpleGUI as sg


# -- Colors --
bgColor1 = '#ffffff'
bgColor2 = '#0e1778'
textColor1 = '#ffffff'
textColor2 = '#0e1778'
buttonBgColor = "#030947"
notVaxxColor = '#e3210b'
warningColor = '#ff9d00'
fullVaxxColor = '#00b315'


# -- Window Layouts -- 
aboutPage = [[
    sg.Column([[
        sg.Column(
        [[sg.Text("OpenVaxx Vaccine Passport Demo", (45, 1), text_color=textColor1, font="Arial", background_color=bgColor2)]],
         background_color=bgColor2
         ),
    sg.Column(
        [[sg.Button("Login", font="Arial", button_color=buttonBgColor),
        sg.Button("Signup", font="Arial", button_color=buttonBgColor )]],
        background_color=bgColor2
        )
        ]], background_color=bgColor2, justification="center"),
        ],
        [sg.HorizontalSeparator(bgColor2)],
         [sg.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." + 
        "Lobortis feugiat vivamus at augue. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. "+
        "Cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl. Id leo in vitae turpis massa. Nisi lacus sed viverra tellus in hac habitasse" +
        " platea dictumst. Amet facilisis magna etiam tempor orci. Id cursus metus aliquam eleifend mi in nulla posuere. Aenean pharetra magna ac placerat. " +
        "Lacinia at quis risus sed. Lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor. Tristique sollicitudin nibh sit amet commodo nulla facilisi. " +
        "Interdum velit laoreet id donec ultrices. Euismod quis viverra nibh cras. Arcu cursus vitae congue mauris. Egestas integer eget aliquet nibh." +
        " Urna id volutpat lacus laoreet non.", s=(90, 30), text_color=textColor2, background_color=bgColor1, expand_x=True, expand_y=True, )
]]
recipentLogin = [[sg.Text("Login as a Recipeint", background_color=bgColor2, text_color=textColor2, font="Arial")],[sg.HorizontalSeparator]]
distributorLogin = [[]]
businessLogin = [[]]
recipentSignup = [[]]
distributorSignup = [[]]
businessSignup = [[]]
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
    window = sg.Window("Login into Your OpenVaxx Account", loginPage, modal=True)
    while True:
        eventlocale, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

def open_recipient_page(username):
    window = sg.Window("OpenVaxx, Welcome " + username, recipientPage)
    while True:
        eventlocale, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    
    window.close()

def open_distributor_main_page(distributor):
    window = sg.Window(distributor, loginPage, modal=True)
    while True:
        eventlocale, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def open_distributor_input_page(distributor):
    window = sg.Window(distributor + "Vaccine Info Input", loginPage, modal=True)
    while True:
        eventlocale, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    
    window.close()


# Create the Window
aboutWindow = sg.Window('OpenVaxx', aboutPage, size=(750,300), background_color="#ffffff")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = aboutWindow.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == "Login":
        open_login_window()

aboutWindow.close()
