import sys, random

print("Welcome to the psych 'sidekick name picker.'\n")
print("a name just like sean would pick for gus:\n\n")

first = ('赵','钱','孙','李')
last = ('琴','棋','书','画')

while True:
    first_name = random.choice(first)
    
    last_name = random.choice(last)
    
    print("\n\n")
    print(f"{first_name}{last_name}",file=sys.stderr)
    print("\n\n")
    
    try_again = input("\n\nTry again? (press enter else n to quit)\n")
    if try_again.lower() == 'n':
        break
    
input("\nPress enter to exit.")