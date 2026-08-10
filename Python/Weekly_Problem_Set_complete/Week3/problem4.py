import math
import random


secret_number = random.randint(1, 100)
guesses = []

print("=== ANIMAL GUESSING GAME ===")
print("A secret animal is waiting...")

while True:
    guess = int(input("\nGuess a number (1-100): "))
    guesses.append(guess)

    if guess == secret_number:
        print("CORRECT! The secret animal was: narwhal")
        print(f"You guessed it in {len(guesses)} tries.")

        minimum_guesses = math.ceil(math.log2(100))
        print(
            f"Minimum possible guesses (optimal): "
            f"{minimum_guesses}"
        )

        total = math.fsum(guesses)
        mean_guess = total / len(guesses)

        print(f"Mean of your guesses: {mean_guess:.2f}")
        break

    distance = math.fabs(guess - secret_number)

    if distance > 40:
        print("Hint: ICE COLD")
    elif distance > 20:
        print("Hint: COLD")
    elif distance > 10:
        print("Hint: WARM")
    else:
        print("Hint: HOT!")