while True:
    sEmail = input("Email to be checked: ")
    
    if sEmail.find("@") != -1 and sEmail.find(".") != -1:
        if sEmail.index(".") > sEmail.index("@"):
            print("Email looks good enough")
        else:
            print("Email is not functioning")  
    else:
        print("Email is not functioning")
 
