# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lamb da functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?


# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

#Set blank count to 0
#For answer in answers:
#blank string is equal to blanks list at index of blank count
#print question
#player guess equals input: print what is the answer to blank string
#while player guess isn't euqal to answe
#ask again
#if we're here, the question was answered correctly. Yay..
#replace the blank string in the question with the answer
#add one to blank counter
#if we're here for loop is done, all answers answered successfully.


#level = get_level()
#answer_list, question_string = select_quiz(level)
#play_game(answer_list, question_string)

#Select level of difficulty by typing into it. possible choics include easy, medium and hard. 


#The following are some of the question strings to pass into play game function.
question_string_easy = "In the movie of iron man, tony ___1___ his ___2___ suit to ___3___ evils"
question_string_medium = "Iron man's suit is powered by ___1___, one of its elements, ___2___ was poisioning Tony and he had to ___3___ a new reactor to save himself in Iron Man 2"
question_string_hard = "In The ___1___ series, Tony used a new massive Arc Reactor to power ___2___. ___3___ later used it to power his wormhole device."
chosen_question = ""
#The following are answers that will need to pass in to check_answer strings. 
answer_list_easy = ["invented", "iron", "fight"]
answer_list_medium = ["Arc Reactor", "palladium", "create"]
answer_list_hard = ["Avengers", "Stark Tower", "Loki"]
chosen_answer_list = []

#A list of replacement blanks to be passed in to play game function
answer_blank = ["___1___", "___2___", "___3____"]


def get_level():
	print "Game Setting"
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
		#return {"answer_list": answer_list_easy, "question_string": question_string_easy}
	elif level == "medium":
		print "medium question:" + question_string_medium
		chosen_question = question_string_medium
		chosen_answer_list = answer_list_medium
		check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
		#return {"answer_list": answer_list_medium, "question_string": question_string_medium}
	elif level == "hard":
		print "hard question:" + question_string_hard
		chosen_question = question_string_hard
		chosen_answer_list = answer_list_hard
		check_answer(chosen_answer_list, chosen_question, answer_blank)
		return chosen_answer_list, chosen_question
		#return {"answer_list": answer_list_hard, "question_string": question_string_hard}
	else:
		print "you can only type in either easy, medium, or hard. Try again"
		return select_quiz(Level)

#This is to check if the user inputs match the pre-defined answers
#inputs are answer_list, question_string, answer_blank chosen by user's input from get_level() passing through select_quiz()
def check_answer(answer_list,question_string,answer_blank):
	p_count = 0
	q_count = 0
	trial = 0
	while q_count < len(answer_blank):
		if answer_list[q_count] == raw_input("what is the answer for:" + answer_blank[q_count] + "?"):
			print "You have answered this correctly!"
			q_count += 1
			if q_count == 3:
				print "Congratulations! You have answered all questions correctly. --The End--"
		else:
			p_count += 1
			trial = 3 - p_count
			print "Wrong! try again! You have", trial, "more trials before the game is over."
			if p_count == 3:
				print "Game Over!"
				break

#Checks if a blank in answer_blank is a substring of the blank passed in
#the inputs are blank, and answer_blank, output is either ponb or none. 
def blank_in_ponb(blank, answer_blank):
	for ponb in answer_blank:
		if ponb in blank:
			return ponb
		return None

def play_game():
	chosen_level = get_level()
	select_quiz(chosen_level)
	#question_string = result["question_string"]
	replaced = []
	chosen_question_list = chosen_question.split()
	for word in chosen_question_list:
		replacement = blank_in_ponb(word, answer_blank)
		#if replacement is NOT equal to NONE
		if replacement != None:
			word = word.replace(replacement, answer_list)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced

play_game()

#Hi tutor, please kindly visit this page https://discussions.udacity.com/t/stage-2-project-couldnt-get-my-last-portion-of-code-to-run-help-needed/192103/3
#to help me to answer my inquary. Many thanks. 
