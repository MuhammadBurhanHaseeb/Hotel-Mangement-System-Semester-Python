from checkIn import checkIn
class  checkInUI:
    def addCheckIn():
            TCIGid = int(input("\nenter the  transaction id of the guest.."))
            TCIname = input("\nenter the name of the guest...")
            TCIaddres = input("\nenter the address of guest... ")
            TCIcontact = input("\nenter the contact of the guest..")
            TCIemail = input("\nenter the email address of the guest")
            TCIgender =input ("\nenter the gender OF The guest..")
            TCIa = int(input("\nenter the no of adult with guets..."))
            TCIc = int(input("\nenter the no of childre with the guest.."))
            TCIdate = input("\nenter the check in date of the guest...")
            TCIodate = input("\nenter the check out date of the guest..")
            Idays = int(input("\nenter the no of days"))
            TCIroomNO = int(input("\nenter the the room no ...")) 
            TCITroom =input("\nenter the room type....")
            TCISroom = input("\nenter the room status....")
            TCIroomRate = int(input("\nenter the room rate...."))
            TCISdiscount = input("\nenter the discount status...")
            TCITdiscount = input("\nenter the discount type ...")
            TCIdiscountRate = int(input("\nenter the discount rate ...."))
            balance = TCIroomRate * Idays
            discount = (TCIroomRate * Idays) * (TCIdiscountRate / 100.0)
            balance = balance - discount
            Ibalance = balance
            s = CheckIn(TCIGid, TCIname, TCIaddres, TCIcontact, TCIemail, TCIgender, TCIa, TCIc, TCIdate, TCIodate, Idays, TCIroomNO, TCITroom, TCISroom, TCIroomRate, TCISdiscount, TCITdiscount, TCIdiscountRate, Ibalance)
            return s
