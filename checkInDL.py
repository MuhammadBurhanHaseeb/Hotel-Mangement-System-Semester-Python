from checkIn import checkIn
import os.path
class  checkInDL:
        checkInList =[]

        @staticmethod    
        def addIntoList( r):
            checkInDLDL.checkInList.append(r)

        @staticmethod    
        def addIntoFile( s , path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+s.TCIGid + "," + s.TCIname + "," + s.TCIaddres + "," + s.TCIcontact + "," + s.TCIemail + "," + s.TCIgender + "," + s.TCIa + "," + s.TCIc + "," + s.TCIdate + "," + s.TCIodate + "," + s.IDays + "," + s.TCIroomNO + "," + s.TCITroom + "," + s.TCISroom + "," + s.TCIroomRate + "," + s.TCISdiscount + "," + s.TCITdiscount + "," + s.TCIdiscountRate + "," + s.IBalance)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST")
    

        @staticmethod
        def isExist( s):
            count = 0
            a=len( checkInDLDL.checkInList)
            for a in checkInDL.checkInList:
                if(a.TCIname == s.TCIname):
                    return True
                else:
                    count = count +1

            if (count == a):
                return False

            return False

        @staticmethod
        def viewCheckInList():
            a = len(checkInList)
            Console.WriteLine("ID            NAME         ADDRESS           CONTACT           EMAIL           GENDER           NO ADULT          NO CHILD          CHK IN DATE        CHK OUT DATE         NO DAYS        ROOM NO        ROOM TYPE       ROOM STATUS            ROOM RATE            DISCOUNT TYPE          DISCOUNT STATUS           DISCOUNT RATE           BALANCE")
            for  i  in  range(0,a,1):
                print("\n"+checkInList[i].TCIGid + " " + checkInList[i].TCIname + " " + checkInList[i].TCIaddres + " " + checkInList[i].TCIcontact + " " + checkInList[i].TCIemail + " " + checkInList[i].TCIgender + " " + checkInList[i].TCIa + " " + checkInList[i].TCIc + " " + checkInList[i].TCIdate + " " + checkInList[i].TCIodate + " " + checkInList[i].Idays + " " + checkInList[i].TCIroomNO + " " + checkInList[i].TCITroom + " " + checkInList[i].TCISroom + " " + checkInList[i].TCIroomRate + " " + checkInList[i].TCISdiscount[i] + " " + checkInList[i].TCITdiscount + " " + checkInList[i].TCIdiscountRate + " " + checkInList[i].Ibalance)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3] ,r[4] , r[5],r[6] ,r[7] , r[8],r[9] ,r[10] , r[11],r[12] ,r[13]  ,r[14] ,r[15] , r[16],r[17] ,r[18]

        @staticmethod
        def readCheckInFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE = checkInDL.parseData(i)
                    user = checkIn(ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE)
                    checkInDL.addIntoList(user)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")          