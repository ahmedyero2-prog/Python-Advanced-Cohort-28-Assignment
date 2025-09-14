print("Welcome the Visitors' log Program")

with open("visitors.txt","x", encoding="utf-8") as visitors:
    try:
        visitor_name = input("Enter the name of the visitor: ")
        visitorz = visitors.readlines()
        for visitor in visitorz:
            if visitor_name not in visitorz:
                appending = open("visitors.txt","a", encoding= "utf-8")
                appending.write(visitor)
                appending.close()
            else:
                pass
    except:
        print("DuplicateVisitorError")


