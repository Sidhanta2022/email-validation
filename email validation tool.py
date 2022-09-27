email = input("enter your email address = ") #sidhanta2022@gmail.com
b,c,d = 0,0,0
if len(email) >= 12:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".")  ^ (email[-3] == "."):
                for a in email:
                    if a == a.isspace():
                        b = 1
                    elif a.isalpha():
                        if  a == a.upper():
                            c = 1
                    elif a == "_" or a == "." or a == "@" or a.isdigit() :
                         continue
                    else:
                        d = 1
                if b == 1 or c == 1 or d == 1:
                    print("error 5")
            else:
                print("error 4")      
        else:
            print("error 3")
    else:
        print("error 2")
else:
    print("error 1")
