# EMAIL VALIDATION USING STRING

email = input("Enter your Email: ")      #g@g.in    # abcd1234@gmail.com
d, j, k = 0, 0, 0

if len(email) >= 6:       # 1
    if email[0].isalpha():       # 2
        if ("@" in email) and (email.count("@")==1):       # 3
            if (email[-4]==".") ^ (email[-3]=="."):       # XOR Operation - ^       #4
                for i in email:
                    if i==i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d = 1

                if d==1 or j==1 or k==1:
                    print("Wrong Email 5 ")
                else:
                    print("Correct Email ")
            else:
                print("Wrong Email 4 ")
        else:
            print("Wrong Email 3 ")
    else:
        print("Wrong Email 2 ")
else:
    print("Worng Email 1 ")
