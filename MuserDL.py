from Muser import Muser
import os.path
class  MuserDL:
        userList = []

        @staticmethod 
        def addIntoList(user):
            MuserDL.userList.append(user)

        @staticmethod
        def isExist( usr):
            count = 0 
            for u in MuserDL.userList:
                if(usr.UserName == u.UserName):
                    return True
                else:
                    count= count + 1
            if(count == userList.Count):
                return False

            return False

        @staticmethod 
        def addIntoFile( a,  path):
            if(os.path.exists(path)):
            
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+a.UserName + "," + a.UserPassword + "," + a.UserRole)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST")   

           
 
        @staticmethod 
        def search( name):
            count = 0
            a = len(MuserDL.userList)
            for s in MuserDL.userList:
                if(s.UserName == name):
                    return s
                    break
                else:
                    count = count +1

            if (count == a):
                return False

            return False

        @staticmethod         
        def addDataIntoFile(path):
            if(os.path.exists(path)):
            
                fileVariable = open(path, 'w')
                for a in MuserDL.userList:
                    fileVariable.print("\n"+a.UserName + "," + a.UserPassword + "," + a.UserRole)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST") 


        @staticmethod   
        def dellUser( user):
            a = len(MuserDL.userList)
            for index in range(0,a,1): 
                if (user.UserName == MuserDL.userList[index].UserName and user.UserPassword == MuserDL.userList[index].UserPassword):
                    MuserDL.userList.pop(index)

        @staticmethod 
        def editUserFromList( previous,  update):
            for s in MuserDL.userList:
                if (previous.UserName == s.UserName and previous.UserPassword == s.UserPassword and previous.UserRole == s.UserRole):
                    s.UserName = update.UserName
                    s.UserPassword = update.UserPassword
                    s.UserRole = update.UserRole

        @staticmethod
        def changepassword(previous , new):
            for s in Muser.userList:
                if (s.UserPassword == previous):
                    s.UserPassword = new                 

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2]

        @staticmethod
        def readUsersFromFile(path):
            if(os.path.exists(path)):
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    username,password,role = MuserDL.parseData(i)
                    user = Muser(username,password,role)
                    MuserDL.addIntoList(user)
            else:
                print("FILE PATH DOES NOT EXIST")                   