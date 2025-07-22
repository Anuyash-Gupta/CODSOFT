import random

a = ['rock', 'paper', 'scissors']
b = 0
c = 0
d = 0

while True:
    e = input("Choose rock, paper, or scissors: ").strip().lower()
    if e not in a:
        print("That is not a valid option. Please try again.")
        continue

    f = random.choice(a)
    print("Computer picked:", f)

    if e == f:
        print("Draw!")
        d += 1
    elif (e == 'rock' and f == 'scissors') or \
         (e == 'scissors' and f == 'paper') or \
         (e == 'paper' and f == 'rock'):
        print("You win!")
        b += 1
    else:
        print("Computer wins!")
        c += 1

    print(f"Score -> You: {b} | Computer: {c} | Draws: {d}")

    g = input("Do you want to play again? (y/n): ").strip().lower()
    if g != 'y':
        print("Thanks for playing!")
        print(f"Final Score -> You: {b} | Computer: {c} | Draws: {d}")
        break
