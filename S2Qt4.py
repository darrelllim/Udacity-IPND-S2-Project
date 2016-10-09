

# The following are some of the question strings to pass into play game function.
question_string_easy = "In the movie of ___1___, Tony ___2___ his ___3___ suit to ___4___ evils."
question_string_medium = "Iron man's suit is powered by ___1___, one of its elements, ___2___ was poisioning Tony. ___3___ had to ___4___ a new reactor to save himself in Iron Man 2"
question_string_hard = "In The ___1___ series, Tony used a new massive Arc Reactor to power ___2___. ___3___ later used it to power his ___4___ device."
chosen_question = ""
# The following are answers that will need to pass in to check_answer strings. 
answer_list_easy = ["Iron Man", "invented", "iron", "battle"]
answer_list_medium = ["Arc Reactor", "palladium", "Tony", "build"]
answer_list_hard = ["Avengers", "Stark Tower", "Loki", "wormhole"]
chosen_answer_list = []

# A list of replacement blanks to be passed in to play game function
answer_blank = ["___1___", "___2___", "___3____", "___4___"]

# this is to prompt the player to choose a level of difficulty for the game. 
# Input is the raw_input to be keyed in by the player. Output is the level that keyed in by the uder. 
def get_level():
	print "GAME SETTING for IRON MAN starring Tony Stark & others"
	level = raw_input("Please select the level of difficulty (easy, medium, or hard):")
	if level == "easy":
		print "Your chosen level is " + level
	elif level == "medium":
		print "Your chosen level is " + level
	elif level == "hard":
		print "Your chosen level is " + level
	else:
		print "you can only type in either easy, medium, or hard. Try again"
		return get_level()
	return level

# Input as level taken from get_level(). 
# Outputs are the returned strings (namely, chosen_answer_list & chosen_question) for the chosen level of difficulty. 
# Outputs are to be used to replace global values and to be called in play_game().
def select_quiz(level):
	if level == "easy":
		print "Your quiz:" + question_string_easy
		chosen_question = question_string_easy
		chosen_answer_list = answer_list_easy
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif level == "medium":
		print "Your quiz:" + question_string_medium
		chosen_question = question_string_medium
		chosen_answer_list = answer_list_medium
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif level == "hard":
		print "Your quiz:" + question_string_hard
		chosen_question = question_string_hard
		chosen_answer_list = answer_list_hard
		#check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question

# the inputs are blank, and answer_blank, output is either poab (parts of answer blank) or none. 
# If there is a blank in answer_blank,  that is a substring of the variable word, then return that word in parts_of_speech [...]
def blank_in_poab(word, answer_blank):
	'''Checks if a blank in answer_blank is a substring of the blank passed in'''
	for poab in answer_blank:
		if poab in word:
			return poab
		return None

def play_game():
	"""This is to start the game"""
	chosen_level = get_level()
	chosen_answer_list, chosen_question = select_quiz(chosen_level)
	chosen_question_list = chosen_question.split()
	replaced = []
	# q_count is the number of trial that one has keyed in incorrectly.
	p_count = 0
	# q_count is the number of answer that is answered correctly.
	q_count = 0
	# trial is number of trial left that one can try to it's a game over.
	trial = 0
	# max_trial is the maximum number of trials that one can guess. 
	max_trial = 3
	for word in chosen_question_list:
		replacement = blank_in_poab(word, answer_blank)
		if replacement != None:
			if chosen_answer_list[q_count] == raw_input("what is the answer for:" + answer_blank[q_count] + "?"):
				word = word.replace(replacement, chosen_answer_list[q_count])
				replaced.append(word)
				to_show_answered_sentence = " ".join(replaced)
				print to_show_answered_sentence
				q_count += 1
			else:
				p_count += 1
				trial = max_trial - p_count
				print "Wrong! try again! You have", trial, "more trials before the game is over."
				if p_count == max_trial:
					print "Game Over!"
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced
	print replaced
	print "---- Iron Man is very pleased to get to know you! -----The End ------"

play_game()


