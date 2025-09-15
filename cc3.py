email = "akolangto"
pwd = "mamamo"

x = input("Email --> ")
y = input("Password --> ")
if x.lower() == email and y.lower() == pwd:
    print("Access Granted!")
else:
    print("Access Denied!")