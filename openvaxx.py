
from OpenVaxxDB import business as ovb
from OpenVaxxDB import distributor as ovd
from OpenVaxxDB import recipient as ovr
import PySimpleGUI as sg

user_var = None

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

# -- New Window Functions -- 


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
                [sg.Text("Distribution Site:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Distribution Site", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Login As Distributor", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 40), (5,5)))]]

    businessLogin = [[sg.Text("Login as a Business", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Business Name:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Business Name", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Login As Business", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 40), (5,5)))]]

    loginPage = [
            [sg.Column([[sg.Text("Login to your OpenVaxx Account", font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="Center" ),
            sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
            [sg.Column(recipentLogin, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(distributorLogin, background_color=bgColor2, size=(225, 275)), sg.VSeparator(color=bgColor2), sg.Column(businessLogin, background_color=bgColor2, size=(225, 275))]
            ]
    window = sg.Window("Login into Your OpenVaxx Account", loginPage, modal=True, background_color=bgColor1, size=(750,300))
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            window.close()
            break 
        elif eventlocale == "Login As Recipient":
            user_var = ovr.recipient(values[1], values[3])
            user_data = user_var.get_user_data()
            if user_data != [False, False]:
                img = "OpenVaxxDB/qrcodes/" + user_data[0] + ".png"
                window.close()
                open_recipient_page(user_data[1], img)
                break  
            else:
                sg.popup("Invalid Username or Password, try again.")
            
        elif eventlocale == "Login As Distributor":
            user_var = ovd.distributor(values[6], values[8])
            if user_var.loginConfirm:
                window.close()
                open_distributor_main_page(user_var)
                break  
            else:
                sg.popup("Invalid Username or Password, try again.")
        elif eventlocale == "Login As Business":
            user_var = ovd.distributor(values[11], values[13])
            user_data = user_var.get_user_data()
            if user_data != [False, False]:
                window.close()
                open_business_main_page(user_data[1])
                break  
            else:
                sg.popup("Invalid Username or Password, try again.")      

def open_recipient_page(username, img_path):
    recipientPage = [
            [sg.Column([[sg.Text("Welcome " + username, font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="left"),
            sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
            [sg.HorizontalSeparator(bgColor2, (10, 5))],
            [sg.Text("Your Personal QR Code, have businesses scan this to see your anonomous vaccination status.", background_color=bgColor2, text_color=textColor1, justification="center")],
            [sg.Column([[sg.Image(img_path,size=(300, 300), background_color=bgColor1)]], justification="center", element_justification="center", background_color=bgColor1)],
            [sg.Column([[sg.Text("Choose a Place to save your QR Code: ", background_color=bgColor2, text_color=textColor1), sg.FolderBrowse("Browse Folders", key="qrCodeLoc", button_color=buttonBgColor), sg.Button("Save QR Code", button_color=buttonBgColor)]], bgColor2, justification="center", element_justification="center")]
            ]
    window = sg.Window("OpenVaxx, Welcome " + username, recipientPage, background_color=bgColor1)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break
    
    window.close()

def open_distributor_main_page(dist: ovd.distributor):
    
    distributorMain = [[sg.Column([[sg.Text("Welcome " + dist._username, font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="left"),
                    sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
                    [sg.Column([[sg.Text("Scan a QR Code to add/update a users vaccination status.", background_color=bgColor2, text_color=textColor1)]], background_color=bgColor2, element_justification="center", justification="center")],
                    [sg.Column([[sg.Button("Click Here to Scan QR Code", button_color=buttonBgColor)]], background_color=bgColor1, justification="center", element_justification="center")]]
    window = sg.Window("Welcome " + dist._username, distributorMain, modal=True, background_color=bgColor1)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break
        elif eventlocale == "Click Here to Scan QR Code":
            window.close()
            dist.scan_qrcode()
            open_distributor_input_page(dist)
            break

    window.close()

def open_distributor_input_page(dist:ovd.distributor):
    vaccineInfo  = dist.read_vaccine_info()
    if vaccineInfo[0] == "no data":
        defaultVal = "Choose One:"
    else:
        defaultVal = vaccineInfo[0]
    distributorInput = [[sg.Column([[sg.Text("Enter a Recipient's Vaccine Information", font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="Center" ),
                    sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
                    [sg.Column([[sg.Text("Please Enter the relevant information about recipients vaccine status: ", background_color=bgColor2, text_color=textColor1, font="Arial")]], justification="center", element_justification="center", background_color=bgColor2)],
                    [sg.Column([[sg.Text("Please Select the vaccine the recipient recived:", background_color=bgColor2, text_color=textColor1)],[sg.DropDown(["Pfizer", "Moderna", "J&J"], default_value=defaultVal, text_color=textColor2, size=(40,1), readonly=True,)], 
                    [sg.Text("Vaccine Dose 1 Distribution Date: (mm/dd/yyyy)", text_color=textColor1, background_color=bgColor2)], [sg.Input(vaccineInfo[1], text_color=textColor2)],
                    [sg.Text("Vaccine Dose 2 Distribution Date: ([type 'no data' for not applicable/not yet recieved] mm/dd/yyyy)", text_color=textColor1, background_color=bgColor2)], [sg.Input(vaccineInfo[2], text_color=textColor2)],
                    [sg.Text("Vaccine Booster Dose Distribution Date: ([type 'no data' for not applicable/not yet recieved] mm/dd/yyyy)", text_color=textColor1, background_color=bgColor2)], [sg.Input(vaccineInfo[3], text_color=textColor2)],
                    [sg.Button("Save Vaccine Information", button_color=buttonBgColor), sg.Button("Close Without Saving", button_color=buttonBgColor)]], background_color=bgColor2, justification="center", element_justification="center")]]
    window = sg.Window(dist._username + " Vaccine Info Input", distributorInput, background_color=bgColor1, modal=True)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED or eventlocale == "Close Without Saving":
            closeNoSave = sg.PopupYesNo("Are you sure you would like to close without saving?")
            if closeNoSave == "Yes":
                window.close()
                open_distributor_main_page(dist)
                break

        elif eventlocale == "Save Vaccine Information":
            dist.update_vaccine_info(values[0], values[1], values[2], values[3], vaccineInfo[4])
            sg.Popup("Information Saved")
            window.close()
            open_distributor_main_page(dist)
            break
    window.close()

def open_business_main_page(business):
    businessMain = [[sg.Column([[sg.Text("Welcome " + business, font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="left"),
                    sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
                    [sg.Column([[sg.Text("Scan a QR Code to anonymously see a customers vaccination status.", background_color=bgColor2, text_color=textColor1)]], background_color=bgColor2, element_justification="center", justification="center")],
                    [sg.Column([[sg.Button("Click Here to Scan QR Code", button_color=buttonBgColor)]], background_color=bgColor1, justification="center", element_justification="center")]]
    window = sg.Window("Welcome " + business, businessMain, modal=True, background_color=bgColor1)
    while True:
        eventlocale, values = window.read()
        if eventlocale == "Exit" or eventlocale == sg.WIN_CLOSED:
            break
        elif eventlocale == "Click Here to Scan QR Code":
            window.close()
            open_business_return_page("{{ business }}")
            break
    
    window.close()

def open_business_return_page(business):
    #check if the person has been vaccinated
    # and change the image and text based on their vaccine status
    image = "OpenVaxxDB/img/fullyvaxxed.png"
    text = "This customer is fully vaccinated and can be let in without worry."

    businessOut = [[sg.Column([[sg.Text("Welcome " + business, font="Arial", size=(45, 1), text_color=textColor1, background_color=bgColor2, pad=(100, 1))]], background_color=bgColor2, size=(500, 30), justification="left", element_justification="left"),
                sg.Column([[sg.Button("Exit", button_color=buttonBgColor, font="Arial")]], justification="right", background_color=bgColor1, pad=(25,1))],
                [sg.Column([[sg.Image(image, size=(320,320), background_color=fullVaxxColor)]], justification="center", element_justification="center", background_color=bgColor1)],
                [sg.Column([[sg.Text(text, text_color=textColor1, background_color=bgColor2)]], justification="center", element_justification="center", background_color=bgColor2)],
                [sg.Column([[sg.Button("Close", button_color=buttonBgColor, font="Arial")]], justification="center", element_justification="center", background_color=bgColor2)]]
    window = sg.Window("Welcome " + business, businessOut, modal=True, background_color=bgColor1)
    while True:
        eventLocale, values = window.read()
        if eventLocale == "Exit" or eventLocale == sg.WIN_CLOSED:
            break
        elif eventLocale == "Close":
            window.close()
            open_business_main_page("{{ business }}")
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
                [sg.Text("Distribution Site:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Distribution Site", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
                [sg.HorizontalSeparator(pad=(1, 10))],
                [sg.Text("Password:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("", background_color=bgColor1, text_color=textColor2, password_char="*", size=(23,1))]], background_color=bgColor2)],
                [sg.Column([[sg.Button("Signup As Distributor", button_color=buttonBgColor)]],background_color=bgColor1,  element_justification="center", justification="center", pad=((0, 45), (5,5)))]]

    businessSignup = [[sg.Text("Signup as a Business", background_color=bgColor2, text_color=textColor1, font="Arial", size=(23,1))], 
                [sg.HorizontalSeparator(pad=(5, 2))],
                [sg.Text("Business Name:", text_color=textColor1, background_color=bgColor2, size=(25,1))],
                [sg.Column([[sg.Input("Business Name", background_color=bgColor1, text_color=textColor2, size=(23,1))]], background_color=bgColor2)],
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
        elif eventlocale == "Signup As Recipient":
            user_var = ovr.recipient(values[1], values[3], True)
            user_data = user_var.get_user_data()
            img = "OpenVaxxDB/qrcodes/" + user_data[0] + ".png"
            window.close()
            open_recipient_page(user_data[1], img)
            break
        elif eventlocale == "Signup As Distributor":
            user_var = ovd.distributor(values[6], values[8], True)
            window.close()
            open_distributor_main_page(user_var)
            break
        elif eventlocale == "Signup As Business":
            user_var = ovb.business(values[11], values[13], True)
            user_data = user_var.get_user_data()
            window.Close()
            open_business_main_page(user_data[1])
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
