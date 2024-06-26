from guest import guest
class  guestUI:
    def addGuest():
            Gid = int(input("\nenter the id of the guest:"))
            name = input("\nenter the name of the guest:")
            addres = input("\nenter the address of guest:")
            contact = input("\nenter the contact of the guest:")
            email = input("\nenter the email address of the guest:")
            gender = input("\nenter the gender OF The guest:")
            s =  guest(Gid , name  , addres, contact , email , gender )
            return s