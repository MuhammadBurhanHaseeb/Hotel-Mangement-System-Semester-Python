from checkOut import checkOut
import os.path
class  checkOutDL:
        checkOutList =[]

        @staticmethod    
        def addIntoList( r):
            checkOutDL.checkOutList.append(r)

        @staticmethod    
        def addIntoFile( s , path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+s.TCOGid + "," + s.TCOname + "," + s.TCOaddres + "," + s.TCOcontact + "," + s.TCOemail + "," + s.TCOgender + "," + s.TCOa + "," + s.TCOc + "," + s.TCOdate + "," + s.TCOidate + "," + s.ODays + "," + s.TCOroomNO + "," + s.TCOTroom + "," + s.TCOSroom + "," + s.TCOroomRate + "," + s.TCOSdiscount + "," + s.TCOTdiscount + "," + s.TCOdiscountRate + "," + s.OBalance)
                fileVariable.close()
                
                
            else:
                print("FILE PATH DOES NOT EXIST")

        @staticmethod
        def isExist( s):
                count = 0
                b=len(checkOutDL.checkOutList)
                for a in checkOutDL.checkOutList:
                    if(a.TCOname == s.TCOname):
                        return True
                    else:
                        count = count +1

                if (count == b):
                    return False

                return False

        @staticmethod
        def searchUser(name):
                for a in checkOutDL.checkOutList:
                    if(a.TCOname == name):
                        return a
                        break
        @staticmethod
        def sortList():
            checkOutDL.checkOutList.sort()          

        @staticmethod
        def viewCheckOutList():
                a = len(checkOutList)
                print("\nID            NAME         ADDRESS           CONTACT           EMAIL           GENDER           NO ADULT          NO CHILD          CHK IN DATE        CHK OUT DATE         NO DAYS        ROOM NO        ROOM TYPE       ROOM STATUS            ROOM RATE            DISCOUNT TYPE          DISCOUNT STATUS           DISCOUNT RATE           BALANCE")
                for  i  in  range(0,a,1):
                    print("\n"+checkOutList[i].TCOGid + " " + checkOutList[i].TCOname + " " + checkOutList[i].TCOaddres + " " + checkOutList[i].TCOcontact + " " + checkOutList[i].TCOemail + " " + checkOutList[i].TCOgender + " " + checkOutList[i].TCOa + " " + checkOutList[i].TCOc + " " + checkOutList[i].TCOdate + " " + checkOutList[i].TCOidate + " " + checkOutList[i].Odays + " " + checkOutList[i].TCOroomNO + " " + checkInList[i].TCOTroom + " " + checkInList[i].TCOSroom + " " + checkInList[i].TCOroomRate + " " + checkInList[i].TCOSdiscount[i] + " " + checkInList[i].TCOTdiscount + " " + checkInList[i].TCOdiscountRate + " " + checkOutList[i].Obalance)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3] ,r[4] , r[5],r[6] ,r[7] , r[8],r[9] ,r[10] , r[11],r[12] ,r[13] ,r[14] ,r[15] , r[16],r[17] ,r[18]

        @staticmethod
        def readCheckOutFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE = checkOutDL.parseData(i)
                    user = checkOut(ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE)
                    checkOutDL.addIntoList(user)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")              

            