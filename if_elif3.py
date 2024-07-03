day=int(input("Enter the day of your birthdate"))
month=int(input("Enter the month of your birthdate"))

if day>31 or day<=0 or month>12 or month<=0:
    print("Invalid choice")
elif (month==3 and day>=21) or (month==4 and day<=19):
    print("Aries")
