from discount import discount
import os.path
class  discountDL:
            DiscountList =[]

            @staticmethod
            def addIntoList( dis):
                discountDL.DiscountList.append(dis)

            @staticmethod
            def addIntoFile ( dis ,  path ):
                if(os.path.exists(path)):
                    
                    fileVariable = open(path, 'w')
                    fileVariable.print("\n"+dis.Did + "," + dis.Tdiscount + "," + dis.Sdiscount+ "," + dis.discountRate)
                    fileVariable.close()
                    
                    
                else:
                    print("FILE PATH DOES NOT EXIST")
           

            @staticmethod      
            def isExist( dis):
                    a = len(discountDL.DiscountList)
                    count = 0
                    for di in discountDL.DiscountList:
                        if(dis.Did == di.Did):
                            return true
                        else:
                            count=count +1

                    if(count == a):
                        return False
                    
                    return False
        
        
                
            @staticmethod
            def viewDiscountList():
                print("\nID               DISCOUNTTYPE               DISCOUNTSTATUS            DISCOUNTRATE")
                a = len(DiscountList)
                for i in range(0,a,1):
                    print("\n"+DiscountList[i].Did + " " + DiscountList[i].Tdiscount + "           " + DiscountList[i].Sdiscount + "        " + DiscountList[i].discountRate)

            @staticmethod
            def parseData(line):
                r = line.split(",")
                return r[0] ,r[1] , r[2],r[3]

            @staticmethod
            def readDiscountFromFile(path):
                if(os.path.exists(path)):
                    
                    fileVariable = open(path, 'r')
                    record = fileVariable.read().split("\n")
                    fileVariable.close()
                    for i in record:
                        discountId , disType , status , rate = discountDL.parseData(i)
                        dis = discount( discountId , disType , status , rate)
                        discountDL.addIntoList(dis)
                    
                    
                else:
                    print("FILE PATH DOES NOT EXIST")        
