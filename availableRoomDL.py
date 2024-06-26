from availableRoom import availableRoom
import os.path
class  availableRoomDL:
        availabelRoomList = []
        @staticmethod
        def addIntoList( roo):
            availableRoomDL.availabelRoomList.append(roo)
        
        @staticmethod
        def addIntoFile(rom , path ):
            if(os.path.exists(path)):
            
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+rom.ARid + "," + rom.AroomNO + "," + rom.ATroom + "," + rom.ASroom + "," + rom.AroomRate)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST") 
  
        @staticmethod
        def viewAvailableRoom():
            print("\nID            ROOM NO               ROOM TYPE                 ROOM STATUS              ROOM rate")
            a = len(availabelRoomList)
            for i in range(0,a,1): 
                print("\n"+availabelRoomList[i].ARid + " " + availabelRoomList[i].AroomNO + "   " + availabelRoomList[i].ATroom + "           " + availabelRoomList[i].ASroom + "         " + availabelRoomList[i].AroomRate)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3],r[4]

        @staticmethod
        def readAvailableRoomFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    roomId,no,roomType,status,roomRate = availableRoomDL.parseData(i)
                    room = availableRoom(roomId,no,roomType,status,roomRate)
                    availableRoomDL.addIntoList(room)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")            