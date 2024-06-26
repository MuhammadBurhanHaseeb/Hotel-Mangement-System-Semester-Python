class Muser:
        UserName=""
        UserPassword=""
        UserRole=""

        def __init__( self , userName , userPassword,userRole):
            self.UserName=userName
            self.UserPassword=userPassword
            self.UserRole=userRole
        
        @staticmethod
        def isValid(user):
            count = 0
            for s in MuserDL.userList:
                if (s.UserName == user.UserName and user.UserPassword == s.UserPassword):
                    return True
                else:
                    count = count +1
            if (count == MuserDL.userList.Count):
                return False
            return False

        @staticmethod
        def isAdmin(user):
            for s in MuserDL.userList:
                if (s.UserName == user.UserName and user.UserPassword == s.UserPassword):
                    return s
            return None
           

    
