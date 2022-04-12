print("Hello, this is a simple python program that stores your details")
answer = input("Do you want to provide your details to me? /(yes or no/) ")

if answer == "no" or answer == "n":
    print("Okay, so lets end this program")
    exit()
elif answer == "yes" or answer == "y":
    print("Okay, I am gonna ask you some questions")
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    gender_answer = input("Do you want me to ask you your gender? ")
    if gender_answer == "yes" or gender_answer == "y":
        user_gender = input("Enter your gender: ")
    elif gender_answer == "no" or gender_answer == "n":
        print("Okay, I am not gonna ask your gender")
print("So I know a some details  about you..")
print("Your name is " + user_name)
print("Your age is " + user_age)
if gender_answer == "yes" or gender_answer == "y":
    print("You are a " + user_gender)
elif gender_answer == "no" or gender_answer == "n":
    exit()
