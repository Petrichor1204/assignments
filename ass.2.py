#A program to request system password from user
user_name = "Rich Flex"
system_password = "ratsgetlaid"
user_input = input("Enter Password\n")
if user_input == system_password:
    print("Welcome" + " " + user_name)
else: 
    print("Wrong Password, please try again")
    