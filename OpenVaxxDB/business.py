import pandas as pd
import random
import hashlib as hl
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
