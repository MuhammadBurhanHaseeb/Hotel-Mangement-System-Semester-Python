from room import room
import os.path
class  roomDL:
        RoomList = []
        @staticmethod
        def addIntoList( roo):
            roomDL.RoomList.append(roo)
        
        @staticmethod
        def addIntoFile(rom , path ):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+rom.rid + "," + rom.roomNO + "," + rom.troom + "," + rom.sroom + "," + rom.roomRate)
                fileVariable.close()
               
               
            else:
                print("FILE PATH DOES NOT EXIST")
           

   
        @staticmethod            
        def viewRoomList():
                print("\nROOMID      ROOMNO      ROOMTYPE      ROOMSTATUS     ROOMRATE")
                a = len(RoomList)
                for i in range(0,a,1):
                    print("\n"+RoomList[i].rid + " " + RoomList[i].roomNO + "  " + RoomList[i].troom + "        " + RoomList[i].sroom + "         " + RoomList[i].roomRate)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3],r[4]

        @staticmethod
        def readRoomFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    roomId,no,roomType,status,roomRate = roomDL.parseData(i)
                    rom = room(roomId,no,roomType,status,roomRate)
                    roomDL.addIntoList(rom)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")            