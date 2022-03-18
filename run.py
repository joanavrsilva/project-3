import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fortune_teller')


def welcome_message():
    """
    Welcome message
    """
    print("Welcome child to the Best Fortune Teller!")
    print("You can ask me everything you want")
    print("...but if you want better results,")
    print("I advice you to ask questions with Yes or No responses")
    questionsMade = 0

    # Ask user name
    print("Let's start with your name")

    name = input ("Please type your name here:")
    print(f"So {name} what do you want to know?")

    # Ask user question
    question = input("Please type your question here:")
    questionsMade += 1
    print (f"So you ask this '{question}'.")
    print ("Let me see what my magic eight ball says...")
    print("ups...I mean...my crystal ball.")
    print("The awnswer is...")

    # Give user an answer
    answers = ["It is certain.","It is decidedly so.",
    "Without a doubt.","Yes definitely.","You may rely on it.",
    "As I see it, yes.","Most likely.","Outlook good.","Yes.",
    "Signs point to yes.","Reply hazy, try again.","Ask again later.",
    "Better not tell you now.","Cannot predict now.",
    "Concentrate and ask again.","Don't count on it.",
    "My reply is no.","My sources say no.","Outlook not so good.",
    "Very doubtful."]
    print(random.choice(answers))

    # Ask if user wants to continue or leave
    print (f" {name} Do you want to ask me anything else?")
    
    anotherQuestion = input("Please type Yes or No here: ")

    if anotherQuestion.lower() != "yes":
        print(f"Bye {name} you ask me " +str(questionsMade) + " question(s)!")
        quit()
    
    print("Okay! What do you want to know now?")
    newQuestion = input ("Please type your new question here: ")
    questionsMade += 1


welcome_message()