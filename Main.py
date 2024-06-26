from MuserDL import MuserDL
from guestDL import guestDL
from roomDL import roomDL
from discountDL import discountDL
from checkInDL import checkInDL
from checkOutDL import checkOutDL
from reservationDL import reservationDL
from messageDL import messageDL
from availableRoomDL import availableRoomDL
from Muser import Muser
from guest import guest
from room import room
from discount import discount
from checkIn import checkIn
from checkOut import checkOut
from reservation import reservation
from message import message
from availableRoom import availableRoom
from MuserUI import MuserUI
from guestUI import guestUI
from roomUI import roomUI
from discountUI import discountUI
from checkInUI import checkInUI
from checkOutUI import checkOutUI
from reservationUI import reservationUI
from messageUI import messageUI
from availableRoomUI import availableRoomUI
import os.path


def main():
    path1 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\user.txt"
    path2 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\availableRoom.txt"
    path3 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\room.txt"
    path4 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\discount.txt"
    path5 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\guest.txt"
    path6 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\reservation.txt"
    path7 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\checkIn.txt"
    path8 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\checkOut.txt"
    path9 = "C:\\Users\\MUHAMMAD BURHAN\\OneDrive\\Desktop\\tasks2\\bhbProject\\files\\message.txt"
    MuserDL. readUsersFromFile(path1)
    availableRoomDL.readAvailableRoomFromFile(path2)
    roomDL.readRoomFromFile(path3)
    discountDL.readDiscountFromFile(path4)
    guestDL.readGuestFromFile(path5)
    reservationDL.readreservationFromFile(path6)
    checInDL.readCheckInFromFile(path7)
    checkOutDL.readCheckOutFromFile(path8)
    messageDLreadMessageFromFile(path9)
    while (true):
        who = MuserUI.loginUser()
        roll = Muser.isAdmin(who)
        if (roll.UserRole == "MANAGER"):
            while (true):
                option =MainUI.managerMenu()
                if (option == "1"):
                    s =  guestUI.addGuest()
                    guestDL.addIntoList(s)
                    guestDL.addIntoFile(s,path)
                elif (option == "2"):
                    guestDL.viewGuestList()
                elif (option == "3"):
                    s=roomUI.addRoom()
                    roomDL.addIntoList(s)
                    roomDL.addIntoFile(s,path)
                elif (option == "4"):
                    roomDL.viewRoomList()
                elif (option == "5"):
                    s= discountUI.addDiscount()
                    if(not (discountDL.isExist(s))):
                        discountDL.addIntoList(s)
                        discountDL.addIntoFile(s,path)
                elif (option == "6"):
                    discountDL.viewDiscountList()
                elif (option == "7"):
                    s=checInUI.addCheckIn()
                    if(not(checkInDL.isExist(s))):
                        checkInDL.addIntoList(s)
                        checInDL.addIntoFile(s,path)
                elif (option == "8"):
                    checInDL.viewCheckInList()
                elif (option == "9"):
                    s=checkOutUI.addCheckOut()
                    if(not(checkOutDL.isExist(s))):
                        checkOutDL.addIntoList(s)
                        checOutDL.addIntoFile(s,path)
                elif (option == "10"):
                    checkOutDL.viewCheckOutList()
                elif (option == "11"):
                    s =availableRoomUI.addAvailabelRoom()
                    availableRoomDL.addIntoList(s)
                    availableRoomDL.addIntoFile(s,path)
                elif (option == "12"):
                    reservationDL.viewReservationList()
                elif (option == "13"):
                    s = MuserUI.addUser()
                    if(not(MuserDL.isExist(s))):
                        MuserDL.addIntoList(s)
                        MuserDL.addIntoFile(s,path) 
                elif (option == "14"):
                    checkOutDL.sortList()
                    checkOutDL.viewCheckOutList()

                elif (option == "15"):
                    name = messageUI.userName()
                    mesge =messageUI.inputMessage()
                    s = messageDL.addMessage(name , mesge,MuserDL.userList)
                    messageDL.addIntoList(s)
                    messageDL.addIntoFile(s,path)
                elif (option == "16"):
                    name = MuserUI.name()
                    s = MuserDL.search(name)
                    MuserDL.dellUser(s)
                    MuserDL.addDataIntoFile(path)
                elif (option == "17"):
                    name = checkOutUI.name()
                    s=searchUser(name)
                    checkOutUI.display(s)
                elif (option == "18"):
                    break
        elif (roll == "USER"):
            while (true):
                    option =MainUI.userMenu()
                    if (option == "1"):
                        viewRoomList()
                    elif (option == "2"):
                        viewDiscountList()
                    elif (option == "3"):
                        viewAvailableRoom()
                    elif (option == "4"):
                        s =reservationUI.addReservation()
                        if(not(reservationDL.isExist(s))):
                            reservationDL.addIntoList(s)
                            reservationDL.addIntoFile(s,path)
                    elif (option == "5"):
                        msg =  messageDL.searchMessage(MuserDL.userList)
                        messageUI.displayMessage(msg)
                    elif (option == "6"):
                        a=MuserUI.previousPass()
                        b=MuserUI.newPass()
                        MuserDL.changepassword(a,b)
                        MuserDL.addDataIntoFile()
                    elif (option == "7"):
                        break
                    else:
                        MainUI.output()
            else:
                MainUI.invalid()  

if __name__ == "__main__":
    main()
