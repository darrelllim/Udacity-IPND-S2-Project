

# The following are some of the question strings to pass into play game function.
question_string_easy = "In the movie of ___1___, Tony ___2___ his ___3___ suit to ___4___ evils."
question_string_medium = "Iron man's suit is powered by ___1___, one of its elements, ___2___ was poisioning Tony. ___3___ had to ___4___ a new reactor to save himself in the movie of Iron Man 2."
question_string_hard = "In The ___1___ series, Tony used a new massive Arc Reactor to power ___2___. ___3___ later used it to power his ___4___ device."
chosen_question = ""
# The following are answers that will need to pass in to check_answer strings. 
answer_list_easy = ["Iron Man", "invented", "iron", "battle"]
answer_list_medium = ["Arc Reactor", "palladium", "Tony", "build"]
answer_list_hard = ["Avengers", "Stark Tower", "Loki", "wormhole"]
chosen_answer_list = []

# A list of replacement blanks to be passed in to play game function
answer_blank = ["___1___", "___2___", "___3___", "___4___"]
poab = ""

# this is to prompt the player to choose a level of difficulty for the game. 
# Input is the raw_input to be keyed in by the player. Output is the level that keyed in by the uder. 
def get_level():
	print "GAME SETTING for IRON MAN starring Tony Stark & others"
	chosen_level = raw_input("Please select the level of difficulty (easy, medium, or hard):")
    #print "Please select the level of difficulty (easy, medium, or hard): "
    #level = input().rstrip()
	if chosen_level == "easy":
		print "Your chosen level is " + chosen_level
	elif chosen_level == "medium":
		print "Your chosen level is " + chosen_level
	elif chosen_level == "hard":
		print "Your chosen level is " + chosen_level
	else:
		print "you can only type in either easy, medium, or hard. Try again"
		return get_level()
	return chosen_level

# Input as level taken from get_level(). 
# Outputs are the returned strings (namely, chosen_answer_list & chosen_question) for the chosen level of difficulty. 
# Outputs are to be used to replace global values and to be called in play_game().
def select_quiz(chosen_level):
	if chosen_level == "easy":
		print "Please answer the following question: " + question_string_easy
		chosen_question = question_string_easy
		chosen_answer_list = answer_list_easy
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif chosen_level == "medium":
		print "Please answer the following question: " + question_string_medium
		chosen_question = question_string_medium
		chosen_answer_list = answer_list_medium
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif chosen_level == "hard":
		print "Please answer the following question: " + question_string_hard
		chosen_question = question_string_hard
		chosen_answer_list = answer_list_hard
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question

def play_game():
	# This is to start the game
	chosen_level = get_level()
	chosen_answer_list, chosen_question = select_quiz(chosen_level)
	w_count = 0
	# w_count is the number of trial that one has keyed in incorrectly. 
	max_trial = 4
	print "you only have " + str(max_trial) + " trials to complete the whole game. Good luck!"
	# max_trial is the maximum number of trials that one can guess.
	index = 0
	while index < len(answer_blank):
		if chosen_answer_list[index] == raw_input("what is the answer for:" + answer_blank[index] + "?"):
			print "Well done!"
			chosen_question = chosen_question.replace(answer_blank[index], chosen_answer_list[index])
			print "Your " + chosen_level + " quiz: " + chosen_question
			index += 1
		else:
			w_count += 1
			trial = max_trial - w_count
			print "Wrong! try again! You have " + str(trial) + " more trials left before the game is over."
			if w_count == max_trial:
				print "Game Over!"
				break 

	print  "---- Iron Man is very pleased to get to know you! -----The End ------"

play_game()
