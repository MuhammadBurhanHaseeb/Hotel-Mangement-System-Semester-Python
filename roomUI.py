from room import room
class  roomUI:
    def addRoom():
            Rid = int(input("\nenter the id of the room:"))
            roomNO = int(input("\nenter the room no:"))
            Troom =  input("\nenter the room type:")
            Sroom =  input("\nenter the room status:")
            roomRate = int(input("\nenter the room rate:"))
            s = room(Rid, roomNO, Troom, Sroom, roomRate)
            return s