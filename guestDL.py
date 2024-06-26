from guest import guest
import os.path
class  guestDL:
        guestList = []

        @staticmethod
        def addIntoFile( gust,  path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                fileVariable.print("\n"+gust.Gid + "," + gust.name + "," + gust.addres + "," + gust.contact + "," + gust.email + "," + gust.gender)
                fileVariable.close()
                
                
            else:
                print("FILE PATH DOES NOT EXIST")
           

        @staticmethod
        def addIntoFile( path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'w')
                for gust in guestDL.guestList:
                    fileVariable.print("\n"+gust.Gid + "," + gust.name + "," + gust.addres + "," + gust.contact + "," + gust.email + "," + gust.gender)
                fileVariable.close()
                
                
            else:
                print("FILE PATH DOES NOT EXIST")
            

        @staticmethod
        def addIntoList( gust):
            guestDL. guestList.append(gust)

    
        @staticmethod        
        def dellGuest(gust):
            a=len(guestDL.guestList) 
            for  idx in range(0,a,1):
                if (gust.name == guestDL.guestList[idx].name):
                    guestDL.guestList.pop(idx)

        @staticmethod        
        def isExist( gust ):
                a = len(guestDL.guestList)
                count = 0
                for g in guestList:
                    if(g.name == gust.name):
                        return True
                    else:
                        count= count+1
                        
                if(count==a):
                    return False

                return False

        @staticmethod         
        def viewguestlist():
            a=len(guestList)
            print("\nID       NAME          ADDRESS             CONTACT             EMAIL             GENDER")
            for i in range(0,a,1): 
                print("\n"+guestList[i].Gid + " " + guestList[i].name + " " + guestList[i].addres + " " + guestList[i].contact + " " + guestList[i].email + " " + guestList[i].gender)

        @staticmethod
        def parseData(line):
            r = line.split(",")
            return r[0] ,r[1] , r[2],r[3],r[4],r[5]

        @staticmethod
        def readGuestFromFile(path):
            if(os.path.exists(path)):
                
                fileVariable = open(path, 'r')
                record = fileVariable.read().split("\n")
                fileVariable.close()
                for i in record:
                    guestId,name,address,contact,email,gender = guestDL.parseData(i)
                    gust = guest(guestId,name,address,contact,email,gender)
                    guestDL.addIntoList(gust)
                
                
            else:
                print("FILE PATH DOES NOT EXIST")        