# Udacity-IPND-S2-Project
S2, own quiz to be reviewed
t2.py is the latest. 

IPND Stage 2 Final Project

For this project, you'll be building a Fill-in-the-Blanks quiz.
Your quiz will prompt a user with a paragraph containing several blanks.
The user should then be asked to fill in each blank appropriately to complete the paragraph.
This can be used as a study tool to help you remember important vocabulary!

Note: Your game will have to accept user input so, like the Mad Libs generator,
you won't be able to run it using Sublime's `Build` feature.
Instead you'll need to run the program in Terminal or IDLE.
Refer to Work Session 5 if you need a refresher on how to do this.

To help you get started, we've provided a sample paragraph that you can use when testing your code.
Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lamb da functions.'''

The answer for ___1___ is 'function'. Can you figure out the others?


Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
How can you adapt that design to work with numbered blanks?

If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

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
