# Write your solution here
def read_input(prompt: str, x: int, y: int) -> int:
    while True:
        
        try:
            number=int(input(prompt))
            if x < number and number < y:
                print(f"You typed in: {number}")
                return number
            else:
                print(f"You must type in an integer between {x} and {y}")
        except ValueError:
            print(f"You must type in an integer between {x} and {y}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
