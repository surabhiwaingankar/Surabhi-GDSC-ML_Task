import random
import string

if __name__ == "__main__":
    part1 = string.digits
    part2 = string.punctuation
    part3 = string.ascii_lowercase
    part4 = string.ascii_uppercase

    length = int(input("Enter the length of the password \n"))

    password=[]

    password.extend(list(part1))
    password.extend(list(part2))
    password.extend(list(part3))
    password.extend(list(part4))

    random.shuffle(password)

    print("".join(password[0:length]))
