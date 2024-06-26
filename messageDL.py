from message import message
import os.path
class  messageDL:
        MessageList =[]

        @staticmethod  
        def addIntoList( m):
           messageDL.MessageList.append(m)

        @staticmethod  
        def addIntoFile(s , path):
            if(os.path.exists(path)):
            
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+s.Messag+","+s.Index)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST")
        
        @staticmethod
        def addMessage(name ,message , userList):
            count = 0
            a = len(userList)
            for  x  in range(0,a,1):
                if (name == userList[x].UserName):
                    s = message(message,x)
                    return s
                    break
                else:
                    count = count + 1
            if (count == a):
                 return False 

        @staticmethod             
        def searchMessage(userList):
            a = len(userList)
            b = len(MessageList)
            for x in range(0,a,1):
                for y in MessageList:
                    if (y.index == x):
                        return y.mesage
                        break      

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1]

        @staticmethod
        def readMessageFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    msg,idx = messageDL.parseData(i)
                    mesg = message(msg,idx)
                    messageDL.addIntoList(mesg)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")                              
