from Muser import Muser
class  MuserUI :
    @staticmethod
    def addUser():
        userName = input("\nEnter the name of the user :")
        userPassword = input("\nEnter the password of the user:")
        userRole = input("\nEnter the role of the user :")
        s = Muser(userName,userPassword,userRole)
        return s

    @staticmethod      
    def loginUser():
        userName = input("\nEnter the name of the user :")
        userPassword = input("\nEnter the password of the user:")  
        s = Muser(userName, userPassword,None)
        return s

    @staticmethod           
    def name():
        name = input("\nEnter the name of the user :")
        return name 

    @staticmethod       
    def previousPass():
        password = input("\nEnter the previous password of the user :")
        return password 

    @staticmethod     
    def newPass():
        password = input("\nEnter the new password  of the user :")
        return password              