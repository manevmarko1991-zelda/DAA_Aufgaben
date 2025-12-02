
portstatus=input("which portstatus ?\n")

match portstatus: #uberprüfe die variable
        case "open":#fall 21 +ausfurung
            print("erfolgerice verbingung!")
        case "block ": #fall 2
            print ("keine verbingung moglich")
        case ("filtered"):#fall 3
            print("timeout")
        case _:             #default fall
            print ("keine gulgiter portstatus")
