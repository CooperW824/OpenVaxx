
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

class page_layout:
    layout_list = []
    def __init__(self, layout:list):
        self.layout_list = layout

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
        ]], background_color=bgColor2),
        ],
        [sg.HorizontalSeparator(bgColor2)],
         [sg.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." + 
        "Lobortis feugiat vivamus at augue. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. "+
        "Cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl. Id leo in vitae turpis massa. Nisi lacus sed viverra tellus in hac habitasse" +
        " platea dictumst. Amet facilisis magna etiam tempor orci. Id cursus metus aliquam eleifend mi in nulla posuere. Aenean pharetra magna ac placerat. " +
        "Lacinia at quis risus sed. Lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor. Tristique sollicitudin nibh sit amet commodo nulla facilisi. " +
        "Interdum velit laoreet id donec ultrices. Euismod quis viverra nibh cras. Arcu cursus vitae congue mauris. Egestas integer eget aliquet nibh." +
        " Urna id volutpat lacus laoreet non.", s=(90, 30), text_color=textColor2, background_color=bgColor1, expand_x=True, expand_y=True, auto_size_text=True)
]]


recipientPage = [[]]
distributorMain = [[]]
distributorInput = [[]]
businessMain = [[]]
businessOut = [[]]
# -- New Window Functions -- 

def make_window(title, layout, modal, bgColor, size):
    pgLayout = layout
    return sg.Window(title, pgLayout, modal, background_color=bgColor1, size=size )

def open_login_window():
    recipentLogin = [[sg.Text("Login as a Recipient", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Login As Recipient", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 40), (5,5)))]]

    distributorLogin = [[sg.Text("Login as a Distributor", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Login As Distributor", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 40), (5,5)))]]

    businessLogin = [[sg.Text("Login as a Business", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Login As Business", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 40), (5,5)))]]

    loginPage = [
            [sg.Column([[sg.Text("Login to your OpenVaxx Account", font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="center", element_justification="Center" ),
            sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
            [sg.Column(recipentLogin, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(distributorLogin, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(businessLogin, background_color=bgColor2, size=(225, 275))]
            ]
    layout = page_layout(loginPage)
    window = sg.Window("Login into Your OpenVaxx Account", loginPage, modal=True, background_color=bgColor1, size=(750,300))
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break    
    window.close()

def open_recipient_page(username):
    window = sg.Window("OpenVaxx, Welcome " + username, recipientPage)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break
    
    window.close()

def open_distributor_main_page(distributor):
    window = sg.Window(distributor, distributorMain, modal=True)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break

    window.close()

def open_distributor_input_page(distributor):
    window = sg.Window(distributor + "Vaccine Info Input", distributorInput, modal=True)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break
    
    window.close()

def open_signup_window():
    recipentSignup = [[sg.Text("Signup as a Recipient", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Signup As Recipient", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 45), (5,5)))]]

    distributorSignup = [[sg.Text("Signup as a Distributor", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Signup As Distributor", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 45), (5,5)))]]

    businessSignup = [[sg.Text("Signup as a Business", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Username:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Username", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Signup As Business", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 45), (5,5)))]]

    signupPage = [
            [sg.Column([[sg.Text("Signup for an OpenVaxx Account", font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(160, 1)),]], background_color=bgColor2, size=(550, 30), justification="left",),
            sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
            [sg.Column(recipentSignup, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(distributorSignup, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(businessSignup, background_color=bgColor2, size=(225, 275))]
            ]
    window = sg.Window("Create Your OpenVaxx Account", signupPage, modal=True, background_color=bgColor1, size=(750,300))
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
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
    elif event == "Signup":
        open_signup_window()

aboutWindow.close()
