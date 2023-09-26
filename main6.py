mon = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July ",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
day = int(input("type day "))
if day > 31 :
    print("Invalid")
    exit()
mt = int(input("type month number "))
if mt > 13 :
    print("Invalid")
    exit()

yr = input("type year ")
print("",mon.get(mt), day, yr)
