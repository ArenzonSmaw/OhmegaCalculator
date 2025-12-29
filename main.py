import calculator

def calc_help():
    print(
        "Operators list:\n"
        "\n + : Addition. format X + Y, example: 4+50"
        "\n - : Subtraction. format X - Y, example: 10-9"
        "\n * : Multiplication. format X * Y, example: 5*8"
        "\n / : Division. format X / Y, example: 60/5"
        "\n ^ : Power. format X ^ Y, example: 4^2"
        "\n % : Modulu: format X % Y, example: 5%2"
        "\n $ : Maximum: format X $ Y, example: 40$60"
        "\n & : Minimum: format X & Y, example: 40&60"
        "\n ! : Factorial: format X!, example: 40!"
        "\n ~ : Negation: format ~Y, example ~5"
        "\n"
    )
def main():
    print("Welcome to my calculator!\nHave fun calculating your boredom away!\n")
    input_expression = ''
    while (input_expression != "quit"):
        try:
            input_expression = input("\nEnter your arithmetic expression: \n")
            if len(input_expression) == 0 :
                print("\nneed help? enter :help for a display of available operators and their use!\n\n")
            elif ":help" in input_expression:
                calc_help()
            elif "quit" in input_expression:
                input_expression = input("Are you sure? (enter yes / no)\n")
                if input_expression == "yes": break
                else: input("good boy. press ENTER to continue")
            else:
                try:
                    print(calculator.calculate(input_expression))
                except (RecursionError):
                    print("number is too big to calculate. please be considerate.")
                except Exception as e:
                   print(e)
        except (KeyboardInterrupt, SystemExit):
            print("\nwhoah there buddy! no need to attack me, if you wish to exit the program just type quit...")
        except (EOFError):
            print("You have found my true one weakness, I must now concede... have a blessed day!")
            raise SystemExit
    try:
        input("you actually thought you could quit THE ULTIMATE CALCULATOR PROGRAM OF ALL TIMES???")
        input("you were right...")
        input("i guess that's what you wanted all along")
        input("farewell my human entertainer...")
    except (SystemExit,KeyboardInterrupt,EOFError):
        pass

if (__name__ == "__main__"):
    main()