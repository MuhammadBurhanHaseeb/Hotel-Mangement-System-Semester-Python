from discount import discount
class  discountUI:
    def addDiscount():
            Did = int(input("\nenter the id of the discount:"))
            Tdiscount = input("\nenter the discount type:")
            Sdiscount = input("\nenter the discount status:")
            discountRate = input("\nenter the discount  rate:")
            s =  discount(Did, Tdiscount, Sdiscount, discountRate)
            return s
