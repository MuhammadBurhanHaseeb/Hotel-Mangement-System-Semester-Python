from reservation import reservation
import os.path
class  reservationDL:
        reservationList =[]

        @staticmethod    
        def addIntoList( r):
            reservationDL.reservationList.append(r)

        @staticmethod    
        def addIntoFile( s , path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+s.RGid + "," + s.Rname + "," + s.Raddres + "," + s.Rcontact + "," + s.Remail + "," + s.Rgender + "," + s.Ra + "," + s.Rc + "," + s.Ridate + "," + s.Rodate + "," + s.Days + "," + s.RroomNO + "," + s.RTroom + "," + s.RSroom + "," + s.RroomRate + "," + s.RSdiscount + "," + s.RTdiscount + "," + s.RdiscountRate + "," + s.RBalance)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST")
   
        @staticmethod
        def isExist( s):
            count = 0
            a=len(reservationDL.reservationList)
            for a in reservationDL.reservationList:
                if(a.Rname == s.Rname):
                    return True
                else:
                    count = count +1

            if (count == a):
                return False

            return False

        @staticmethod
        def viewReservationList():
            a= len(reservationList)
            print("\nID        NAME      ADDRESS      CONTACT         EMAIL       GENDER       NO ADULT      NO CHILD           CHK IN DATE          CHK OUT DATE       NO DAYS           ROOM NO          ROOM TYPE      ROOM STATUS      ROOM RATE          DISCOUNT TYPE         DISCOUNT STATUS         DISCOUNT RATE        BALANCE")
            for i in range(0,a,1):
                print("\n"+reservationList[i].RGid + " " + reservationList[i].Rname + " " + reservationList[i].Raddres + " " + reservationList[i].Rcontact + " " + reservationList[i].Remail + " " + reservationList[i].Rgender + " " + reservationList[i].Ra + " " + reservationList[i].Rc + " " + reservationList[i].Ridate + " " + reservationList[i].Rodate + " " + reservationList[i].Rdays + " " + reservationList[i].RroomNO + " " + reservationList[i].RTroom + " " + reservationList[i].RSroom + " " + reservationList[i].RroomRate + " " + reservationList[i].RSdiscount + " " + reservationList[i].RTdiscount + " " + reservationList[i].RdiscountRate + " " + reservationList[i].Rbalance)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3] ,r[4] , r[5],r[6] ,r[7] , r[8],r[9] ,r[10] , r[11],r[12] ,r[13] ,r[14] ,r[15] , r[16],r[17] ,r[18]

        @staticmethod
        def readreservationFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE = reservationDL.parseData(i)
                    user = reservation(ID,NAME,ADDRESS,CONTACT,EMAIL,GENDER,NOaDULT,NOcHILD ,CHKiNdATE,CHKoUTdATE,NOdAYS,ROOMnO ,ROOMtYPE,ROOMsTATUS,ROOMrATE ,DISCOUNTtYPE ,DISCOUNTsTATUS ,DISCOUNTrATE,BALANCE)
                    reservationDL.addIntoList(user)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")        