import random

# Create number range 1 - 100
# Select and save a random number from that range
target_number = random.randint(1,100)

# While number entered by user is not equal to target_number
# Loop continues to run until it is broken manually
while True:
    
    # continue to request an integer until user enters it
    # Print"Guess the number: n" expecting an integer in place of n
    try: 
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid integer")
        continue
    
    # If number is not between 1 and 100
    if guess < 1 or guess > 100:
        # Tell user to choose a number within range
        print("Please enter a number between 1 and 100.")
        continue
        
    # If guess > target: tell user it's too high
    if guess > target_number:
        print("Too high!")

    # If guess < target: tell user it's too low
    elif guess < target_number:
        print("Too low!")

    # If guess == target: congratulate and break loop
    else:
        print("Correct! You guessed the number.")
        break
