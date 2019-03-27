#a troubleshoot program
print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans,etc.)")
choice = input("or show any lights? (y/n):")
#troubleshooting control logic
if choice == "n": #computer does not have power
    choice = input("Is it plugged in? (y/n):")
    if choice == "n": #if not plugged in, plug in.
        print("Plug it in. If the problem persists,")
        print("please run this program again.")
    else: #it is plugged in
        choice = input("Is switch in \"on\" position? (y/n):")
        if choice == "n": #the switch is off, turn it on
            print("Plug it in. If the problem persists,")
            print("please run this program again.")
        else: #the switch is on
            choice = input("Does computer have a fuse? (y/n):")
            if choice == "n": #no fuse
                choice = input("Is the outlet OK? (y/n):")
                if choice == "n": #fix outlet
                    print("Check the outlet circuit")
                    print("breaker or fuse. Move to a")
                    print("new outlet, if necessary.")
                    print("If problem persist,")
                    print("please run program again.")
                else: #will need technician
                    print("Please consult a service technician.")
            else: #fuse check  
                print("Check the fuse. Replace if")
                print("necessary. If the problem,")
                print("persist, then")
                print("please run this program again.")
else: #there is power
    print("Please consult a service technician.")
        
            
        
    
