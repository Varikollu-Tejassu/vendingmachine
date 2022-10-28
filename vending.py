
money=0
sample={}
def buy_action():
    coffee_type = input("What do you want to buy? \nEnter 1 for 'Espresso', 2 for 'cappuccino', 3 for 'Latte' \nand 'exit' to main menu:")
    global money
    global sample

    if coffee_type == "1":
        Addon_type = input("What do you want to Add_on?\nEnter 1 for 'Milk', 2 for 'cream', 3 for 'Latte' and 'back' to menu:")
        if Addon_type =="1":
            money+=60
            sample["expresso with Milk"]="60"
            print("your order Expresso with Milk is ready! collect it")
        if Addon_type=="2":
            money+=75
            sample["expresso with Cream"]="75"
            print("your order Expresso with Cream is ready! collect it")
        if Addon_type=="3":
            money+=100
            sample["expresso with Latte"]="100"
            print("your order Expresso with Latte is ready! collect it")
        if Addon_type=="back":
            buy_action()
            
        
            
    elif coffee_type == "2":

        Addon_type = input("What do you want to Add_on? \nEnter 1 for 'Milk', 2 for 'cream', 3 for 'Latte' and 'back' to menu:")
        if Addon_type =="1":      
            money+=80
            sample["Capuccino with Milk"]="80"
            print("your order Capuccino with Milk is ready! collect it")
        if Addon_type=="2":
            money+=90
            sample["Capuccino with Cream"]="90"
            print("your order Capuccino with Cream is ready! collect it")
        if Addon_type=="3":
            money+=125
            sample["Cappucino with Latte"]="125"
            print("your order Capuccino with Latte is ready! collect it")
        if Addon_type=="back":
            buy_action()
    
    elif coffee_type == "3":
        Addon_type = input("What do you want to Add_on? \nEnter 1 for 'Milk', 2 for 'cream', 3 for 'Latte' and 'back' to menu:")
        if Addon_type =="1":
            money+=100
            sample["Latte with Milk"]="100"
            print("your order Latte with Milk is ready! collect it")
        if Addon_type=="2":
            money+=125
            sample["Latte with Cream"]="125"
            print("your order Latte with Cream is ready! collect it")
        if Addon_type=="3":
            money+=150
            sample["Latte with Latte"]="150"
            print("your order Latte with Latte is ready! collect it")
        if Addon_type=="back":
            buy_action()
   
    print("pay the amount of:",money)


def price_list():
    d={1:["Expresso","60","75","100"],
    2:["Capuccino","80","90","125"],
     3:["Latte","100","125","150"]
    }
    print("-------------------------------------------------------------------------------")
    print (" {:<8} {:<18} {:<10} {:<10} {:<10}".format('ProductNo',"product",'Milk','Cream','Latte'))
    print("-------------------------------------------------------------------------------")
    for k, v in d.items():
      product, lang, perc, change = v
      print (" {:<10} {:<19} {:<10} {:<10} {:<10}".format(k,product, lang, perc, change))
    


def bill():
    print("---------------------------------------------------------------------")
    if len(sample)==0:
        print("No items bought till now. please order something from menu")
    else:
        print (" {:<10}                                {:59}".format("Item","Price"))
        print("---------------------------------------------------------------------")
        for k, v in sample.items():
            change = v
            print (" {:<10}                        {:59}".format(k,change))
    
    
    print("-----------------------------------------------------------------------")
    print("Total:",money)
    
    
    print("-----------------------------------------------------------------------")
    
def exit():
    print("-----------Thankyou for using coffee machine.--------------")
    print("-------------------Have a nice day.------------------------")
    print("---------------------See you soon...------------------------")
    





while True:
    print("WELCOME TO COFFEE MACHINE DESIGNED BY TEJASSU FOR JALAN TECHNOLOGIES..")
    print("FOLLOW BELOW INSTRUCTIONS TO ORDER SOMETHING..")
    input_ = input("Write action  \npress 1 for 'order_Coffee', 2 for 'price_list', \n3 for 'bill', 4 for 'exit':")
    print()
    if input_ == "1":
        buy_action()
        print()
    elif input_ == "2":
        price_list()
        print()
    elif input_ == "3":
        bill()
        print()
    elif input_ == "4":
        exit()
        print()
        break
    else:
        break


    