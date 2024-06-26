class  messageUI:
    def userName():
        name = input("\nEnter the name of the user which you want to send message:")
        return name

    def inputMessage():
        Message = input("enter the message you want to send:")
        return Message
        
    def displayMessage(msg):
        print("\n Message is:",msg)