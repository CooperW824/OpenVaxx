import pandas as pd
import qrcode
import shutil
import os
import random
from pathlib import Path
import hashlib as hl
class recipient:

    _username = ""
    _password_hash = 0
    database = pd.DataFrame()
    loginConfirm = False
    userId = ""

    def __init__(self, username:str, password:str, new_user=False):
    
        self._username = username
        self._password_hash = hl.md5(password.encode()).hexdigest()
        self.database = self.__openDatabase("OpenVaxxDB/database.csv")

        if new_user == True:
            self.signup()
            self.loginConfirm = True
        else:
            self.loginConfirm = self.login()


    def save_qr_code(self, userID, path_to_save_to):
        src_path = os.getcwd() + "\\OpenVaxxDB\\qrcodes\\" + userID + ".png"
        shutil.copyfile(src_path, path_to_save_to)
        

    def signup(self):
        frontId = random.randrange(1111111111, 9999999999)
        backId = 1
        idVerified = False
        while(idVerified == False):
            for i in str(frontId):
                if i != "0":
                    backId *= int(i)
            self.userId = str(frontId) + "_" + str(backId)
            idList = self.__to_list(self.database, "userID")
            inList = idList.count(self.userId)
            if inList > 0:
                idVerified = False
            else:
                idVerified = True
        df = self.database
        df.loc[ len(df)] = [self.userId, "Recipient", self._username, self._password_hash, "no data", "no data", "no data", "no data"] 
        self.database = df
        self.__saveDatabase()
        self.__generate_qr(self.userId)
        #generate userID and add id, username, and password hash to DB
     
    
    def login(self): 
        usernames = self.__to_list(self.database, "username")
        passwords = self.__to_list(self.database, "passwordHash")
        userIDs = self.__to_list(self.database, "userID")
        for i in range(len(usernames)):
            if passwords[i] == self._password_hash and usernames[i] == self._username:
                self.userId = userIDs[i]
                return True

        return False
    
    def __openDatabase(self, path:str):
        #open and return the pandas dataframe containing the database
        return pd.read_csv(path)

    def __saveDatabase(self):
        #save the PD Dataframe to the CSV
        self.database.to_csv("OpenVaxxDB/database.csv", index=False)
    
    def __to_list(self, data, param):  # converts pandas dataframe to a standard list
        list1 = []
        for i in range(0, len(data[param])):
            list1.append(data[param][i])

        return list1

    def __generate_qr(self, userID):
        # Creating an instance of QRCode class
        qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
  
        # Adding data to the instance 'qr'
        qr.add_data(userID)
  
        qr.make(fit = True)
        img = qr.make_image(fill_color = 'black', back_color = 'white')

        
        str_path = "OpenVaxxDB/qrcodes/" + userID + ".png" 
        path = Path(str_path)

        img.save(path)

    def get_user_data(self):
        if self.loginConfirm == True:
            return [self.userId, self._username]
        else:
            return[False,False]
