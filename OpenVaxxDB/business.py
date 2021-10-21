import datetime as dt
import pandas as pd
import random
import hashlib as hl
import numpy as np
import cv2
from pyzbar.pyzbar import decode
class business:

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
        df.loc[ len(df)] = [self.userId, "Business", self._username, self._password_hash, "not applicable", "not applicable", "not applicable", "not applicable"] 
        self.database = df
        self.__saveDatabase()
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

    def get_user_data(self):
        if self.loginConfirm == True:
            return [self.userId, self._username]
        else:
            return[False,False]
    def __decoder(self, image) -> str:
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            return barcodeData


    def __validate_data(self, data:str) -> bool:
        if data != None:
            dataArr = data.split("_")
            checksum = 1
            for i in dataArr[0]:
                if i != "0":
                    checksum *= int(i)
            if str(checksum) == dataArr[1]:
                return True
            else:
                return False 
        else:
            return False

    def scan_qrcode(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        dataValid = False

        while not dataValid:
            ret, frame = cap.read()
            data = self.__decoder(frame)
            cv2.imshow('Image', frame)
            dataValid = self.__validate_data(data)
            if dataValid:
               self.scannedID = data
            code = cv2.waitKey(10)
            if code == ord('x'):
                break
        cv2.destroyAllWindows()

    def read_vaccine_info(self):
        df = self.database
        userIDs = self.__to_list(self.database, "userID")
        for i in range(len(userIDs)):
            if userIDs[i] == self.scannedID:
                return [df["vaccineType"][i], df["firstDose"][i], df["secondDose"][i], df["thirdDose"][i]]
        return False

    def get_vaxx_status(self, vaxxInfo: list[str, str, str, str]) -> int:

        if vaxxInfo[0] == "Pfizer" or vaxxInfo[0] == "Moderna":
            if vaxxInfo[1] != "no data" and vaxxInfo[2] == "no data":
                return 1
            else: 
                d1 = vaxxInfo[2].split("/")
                d1 = dt.datetime(d1[2], d1[0], d1[1])
                now = dt.datetime.now()
                delta = now - d1
                if delta.days >= 14:
                    return 2
                else:
                    return 1
        else:
            if vaxxInfo[1] == "no data":
                return 0
            else:
                d1 = vaxxInfo[1].split("/")
                d1 = dt.datetime(d1[2], d1[0], d1[1])
                now = dt.datetime.now()
                delta = now - d1
                if delta.days >= 14:
                   return 2
                else:
                   return 1 