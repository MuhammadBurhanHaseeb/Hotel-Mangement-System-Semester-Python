from reservation import reservation
class  reservationUI:
    def addReservation():
            RGid = int(input("\nenter the  transaction id of the guest.."))
            Rname = input("\nenter the name of the guest...")
            Raddres = input("\nenter the address of guest... ")
            Rcontact = input("\nenter the contact of the guest..")
            Remail = input("\nenter the email address of the guest")
            Rgender =input ("\nenter the gender OF The guest..")
            Ra = int(input("\nenter the no of adult with guets..."))
            Rc = int(input("\nenter the no of childre with the guest.."))
            Ridate = input("\nenter the check in date of the guest...")
            Rodate = input("\nenter the check out date of the guest..")
            Rdays = int(input("\nenter the no of days"))
            RroomNO = int(input("\nenter the the room no ..."))   
            RTroom =input("\nenter the room type....")
            RSroom = input("\nenter the room status....")
            RroomRate = int(input("\nenter the room rate...."))
            RSdiscount = input("\nenter the discount status...")
            RTdiscount = input("\nenter the discount type ...")
            if ((RSdiscount == "vip" and RSroom == "vip") and (RTdiscount == "four" and RTroom == "four")):
                RdiscountRate = 50
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "vip" and RSroom == "vip") and (RTdiscount == "three" and RTroom == "three")):
                RdiscountRate = 45
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "vip" and RSroom == "vip") and (RTdiscount == "two" and RTroom == "two")):
                RdiscountRate = 40
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "vip" and RSroom == "vip") and (RTdiscount == "one" and RTroom == "one")):
                RdiscountRate = 35
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "regular" and RSroom == "regular") and (RTdiscount == "four" and RTroom == "four")):
                RdiscountRate = 30
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "regular" and RSroom == "regular") and (RTdiscount == "three" and RTroom == "three")):
                RdiscountRate = 25
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "regular" and RSroom == "regular") and (RTdiscount == "two" and RTroom == "two")):
                RdiscountRate = 20
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "regular" and RSroom == "regular") and (RTdiscount == "one" and RTroom == "one")):
                RdiscountRate = 15
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "none" and RSroom == "none") and (RTdiscount == "four" and RTroom == "four")):
                RdiscountRate = 10
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "none" and RSroom == "none") and (RTdiscount == "three" and RTroom == "three")):
                RdiscountRate = 5
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "none" and RSroom == "none") and (RTdiscount == "two" and RTroom == "two")):
                RdiscountRate = 1
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance
            elif ((RSdiscount == "none" and RSroom == "none") and (RTdiscount == "one" and RTroom == "one")):
                RdiscountRate = 0
                balance = RroomRate * Rdays
                discount = (RroomRate * Rdays) * (RdiscountRate / 100.0)
                balance = balance - discount
                Rbalance = balance

            s = reservation( RGid,  Rname,  Raddres, Rcontact, Remail,  Rgender,  Ra,  Rc,  Ridate,  Rodate, Rdays,  RroomNO,     RTroom,  RSroom,  RroomRate, RSdiscount,  RTdiscount, RdiscountRate,  Rbalance)
            return s 