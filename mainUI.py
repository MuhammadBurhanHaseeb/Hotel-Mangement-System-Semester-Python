class MainUI:
    def loginHeader():
        print("\n*****************************************************************************")
        print("\n*******************       LOGIN SCREEN             **************************")
        print("\n*****************************************************************************")

    def systemHeader():
        print("\n*****************************************************************************")
        print("\n*******************   BHB HOTEL MANAGEMENT SYSTEM  **************************")
        print("\n*****************************************************************************")

    def managerMenu():
       MainUI.systemHeader()
        print("\nMAIN MENU >>")
        print("\n--------------")
        print("\nselect one of the followings options...")
        print("\n1. add the new guest..")
        print("\n2. view the guest list..")
        print("\n3. add the new room type..")
        print("\n4. view the list of room type..")
        print("\n5. add the discount type..")
        print("\n6. view the list of discount type..")
        print("\n7. add check in form.....")
        print("\n8. view the check in form list...")
        print("\n9. add the check out form....")
        print("\n10. view the list of check out form list")
        print("\n11. add the available room...")
        print("\n12. view the reservation form ...")
        print("\n13. add users...")
        print("\n14. change passwords")
        print("\n15. sorting check out form list according to high balance")
        print("\n16. aleret msg send to user")
        print("\n17.  delete user ")
        print("\n18.  Search the user record ")
        print("\n19.  LOGOUT ")
        option = input("enter the one of the options:")
        return option

    def userMenu():
        systemHeader()
        print("\nMAIN MENU >>")
        print("\n--------------")
        print("\nSelect one of the followings options...")
        print("\n1. view the room type list ..")
        print("\n2. view the discount type list..")
        print("\n3. view the available room list ..")
        print("\n4. add the reservation form ...")
        print("\n5. mannager alert message..")
        print("\n6. change password..")
        print("\n7. log out")
        option = input("enter the one of the options:")
        return option
        
    def output():
        print("\n NO MANAGER OR NO USER")

    def invalid():
        print("\n Invalid User Name")