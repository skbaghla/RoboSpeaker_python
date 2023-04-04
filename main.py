import os

if __name__ == '__main__':

    print("Welcome to Robo Speaker Created by Sanjeev")
    name = input("Please enter your name : ")
    os.system(f"say Hi my name is {name}. Robo speaker will speak on behalf of me.")
    while True:
        x = input("Enter what you want to speak : ")

        if x == "Exit Robo":
            os.system(f"say Bye Bye everyone from {name}")
            break
        command = f"say {x}"
        os.system(command)
