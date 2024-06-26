from checkOut import checkOut
class  checkOutUI:
     def addCheckIn():
          TCOGid = int(input("\nenter the  transaction id of the guest.."))
          TCOname = input("\nenter the name of the guest...")
          TCOaddres = input("\nenter the address of guest... ")
          TCOcontact = input("\nenter the contact of the guest..")
          TCOemail = input("\nenter the email address of the guest")
          TCOgender =input ("\nenter the gender OF The guest..")
          TCOa = int(input("\nenter the no of adult with guets..."))
          TCOc = int(input("\nenter the no of childre with the guest.."))
          TCOdate = input("\nenter the check in date of the guest...")
          TCOidate = input("\nenter the check out date of the guest..")
          Odays = int(input("\nenter the no of days"))
          TCOroomNO = int(input("\nenter the the room no ...")) 
          TCOTroom =input("\nenter the room type....")
          TCOSroom = input("\nenter the room status....")
          TCOroomRate = int(input("\nenter the room rate...."))
          TCOSdiscount = input("\nenter the discount status...")
          TCOTdiscount = input("\nenter the discount type ...")
          TCOdiscountRate = int(input("\nenter the discount rate ...."))
          balance = TCOroomRate * Idays
          discount = (TCOroomRate * Odays) * (TCOdiscountRate / 100.0)
          balance = balance - discount
          Obalance = balance
          s = CheckOut(TCOGid, TCOname, TCOaddres, TCOcontact, TCOemail, TCOgender, TCOa, TCOc, TCOdate, TCOidate, Odays, TCOroomNO, TCOTroom, TCOSroom, TCOroomRate, TCOSdiscount, TCOTdiscount, TCOdiscountRate, Obalance)
          return s
          
     def name():
          TCOname = input("\nEnter the name of the guest...")
          return TCOname
          
     def display(s):
          print(s.TCOGid + " " + s.TCOname + " " + s.TCOaddres + " " + s.TCOcontact + " " + s.TCOemail + " " + s.TCOgender + " " + s.TCOa + " " + s.TCOc + " " + s.TCOdate + " " + s.TCOidate + " " + s.Odays + " " + s.TCOroomNO + " " + s.TCOTroom + " " + s.TCOSroom + " " + s.TCOroomRate + " " + s.TCOSdiscount + " " + s.TCOTdiscount + " " + s.TCOdiscountRate + " " + s.Obalance)     