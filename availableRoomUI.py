from availableRoom import availableRoom
class  availableRoomUI:
    def addAvailabelRoom():
            ARid =int( input("\nenter the id of the available  room:"))
            AroomNO = int(input("\nenter the available room no: "))
            ATroom = input("\nenter the available  room type:")
            ASroom =  input("\nenter the available room status:")
            AroomRate = int(input("\nenter the available  room rate:"))
            s = availableRoom(ARid, AroomNO, ATroom, ASroom, AroomRate)
            return s