from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#1st param = name, 2nd param = if the bot wants to learn,
#3rd param = gives the chatbot build its logic upon

#chatterbot.logic.BestMatch --> Respond with simple chat strings
omar_bot = ChatBot("Omar-Bot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

#Training list
#First element is a question, successive element is answer
#Going to be an even list, because we don't a question without answer
training_list = [
    "Hey",
    "Hey there.",
    "What's your name?",
    "I'm a Omar-Bot",
    "How old are you?",
    "I was born on Sept 14, 2023"
]
#Train the chatbot
list_trainer = ListTrainer(omar_bot)
list_trainer.train(training_list)