try:
    age=int(input("whats your age?"))
    if age<18:
        print("you are underage")
    else:
        print("you are allowed")
except:
    print("numbers only")