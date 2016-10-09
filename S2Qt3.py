

#The following are some of the question strings to pass into play game function.
question_string_easy = "Tony ___1___ his ___2___ suit to ___3___ evils."
question_string_medium = "Iron man's suit is powered by ___1___, one of its elements, ___2___ was poisioning Tony and he had to ___3___ a new reactor to save himself in Iron Man 2"
question_string_hard = "In The ___1___ series, Tony used a new massive Arc Reactor to power ___2___. ___3___ later used it to power his wormhole device."
chosen_question = ""
#The following are answers that will need to pass in to check_answer strings. 
answer_list_easy = ["invented", "iron", "battle"]
answer_list_medium = ["Arc Reactor", "palladium", "create"]
answer_list_hard = ["Avengers", "Stark Tower", "Loki"]
chosen_answer_list = []

#A list of replacement blanks to be passed in to play game function
answer_blank = ["___1___", "___2___", "___3____"]


def get_level():
	print "GAME SETTING for IRON MAN starring Tony Stark & others"
	level = raw_input("Please select the level of difficulty (easy, medium, or hard):")
	return level

#Input as level taken from get_level(). 
#outputs are the returned strings (namely, chosen_answer_list & chosen_question) for the chosen level of difficulty. 
#outputs are to be used to replace global values and to be called in play_game().
def select_quiz(level):
	if level == "easy":
		print "easy question:" + question_string_easy
		chosen_question = question_string_easy
		chosen_answer_list = answer_list_easy
		check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif level == "medium":
		print "medium question:" + question_string_medium
		chosen_question = question_string_medium
		chosen_answer_list = answer_list_medium
		check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	elif level == "hard":
		print "hard question:" + question_string_hard
		chosen_question = question_string_hard
		chosen_answer_list = answer_list_hard
		check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
	else:
		print "you can only type in either easy, medium, or hard. Try again"
		return select_quiz(Level)

#This is to check if the user inputs match the pre-defined answers
#inputs are answer_list, question_string, answer_blank chosen by user's input from get_level() passing through select_quiz()
def check_answer(answer_list,question_string,answer_blank):
	#q_count is the number of trial that one has keyed in incorrectly.
	p_count = 0
	#q_count is the number of answer that is answered correctly.
	q_count = 0
	#trial is number of trial left that one can try to it's a game over.
	trial = 0
	#max_trial is the maximum number of trials that one can guess. 
	max_trial = 3
	while q_count < len(answer_blank):
		if answer_list[q_count] == raw_input("what is the answer for:" + answer_blank[q_count] + "?"):
			print "You have answered this correctly!"
			q_count += 1
			if q_count == 3:
				print "Congratulations! You have answered all questions correctly."
		else:
			p_count += 1
			trial = max_trial - p_count
			print "Wrong! try again! You have", trial, "more trials before the game is over."
			if p_count == max_trial:
				print "Game Over!"
				break

#Checks if a blank in answer_blank is a substring of the blank passed in
#the inputs are blank, and answer_blank, output is either poab (parts of answer blank) or none. 
# If there is a blank in answer_blank,  that is a substring of the variable word, then return that word in parts_of_speech [...]
def blank_in_poab(word, answer_blank):
	for poab in answer_blank:
		if poab in word:
			return poab
		return None

def play_game():
	chosen_level = get_level()
	chosen_answer_list, chosen_question = select_quiz(chosen_level)
	a_count = 0
	replaced = []
	chosen_question_list = chosen_question.split()
	for word in chosen_question_list:
		replacement = blank_in_poab(word, answer_blank)
		if replacement != None:
			word = word.replace(replacement, chosen_answer_list[a_count])
			replaced.append(word)
			a_count += 1
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	print replaced
	print "---- Iron Man is very pleased to get to know you! -----The End ------"

play_game()

