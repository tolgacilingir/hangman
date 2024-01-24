name = input("Enter User Name: ")
print("Welcome " + name + " it's time to play hangman.")

secret_word = "alive"

lives = 10

guess_string = ""

while lives > 0:

	character_left = 0

	for character in secret_word:


		if character in guess_string:
			print(character)
		else:
			print("-")
			character_left += 1
	
	if character_left == 0:
		print("You won!!")
		break







	guess = input("Guess a letter:")
	guess_string += guess 

	if guess not in secret_word:
		lives -= 1 
		print("Wrong Guess!")
		print(f"You have {lives} left")

		if lives == 0:
			print("You died!")