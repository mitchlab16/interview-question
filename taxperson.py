def tax_price(price,cat):
    price = int(price)
    nece=["food","gas","health_care","auto_care","house_keeping"]
    lux=["jewlry", "rolex", "prada", "luis_vuiton", "bmw", "mercedes"]
	
    tax=0
    if cat in nece:
        tax = price/100
    elif cat in lux:
        tax = price/100*9
    else: 
        print "Ask a cashier for the tax"
        price=str(price)
        tax="+tax"
	
    print "The total price is ",price+tax, "cents"
    
if __name__=='__main__':
    import re
    num = raw_input("Enter the price of the item in cent: ")
	
    if re.match(r'^[1-9]\d+$', num) :
        print "The price without the tax is " + num + " cents"
    else: 
        print "The price is not an integer."
        exit (1)
		
    item_cat = raw_input("Enter the category of the item: ")
    
    tax_price(num,item_cat)