user_name = 'python'
pass_word = 'rules'


print("Write a program that asks the user for a username and password."
      " If either or both are incorrect, the program ask the user to enter the username and password again."
      " This continues until the login information is correct or wrong credentials have been entered five times."
      " If the information is correct, the program prints out Welcome."
      " After five failed attempts the program prints out Access denied."
      " The correct username is python and password rules.")

give_username = None
give_password = None

wrong = 2

give_username = input(" hey give me your username")
give_password = input(" hey give me your password")

if user_name != give_username or pass_word != give_password and pass_word != give_password:
    while 6 > wrong:
        give_username = input(" hey give me your username")
        give_password = input(" hey give me your password")

        if user_name == give_username and pass_word == give_password:
            print("Welcome.")
            break

        if wrong == 5:
            print("Access denied.")
            break

        wrong = wrong + 1


