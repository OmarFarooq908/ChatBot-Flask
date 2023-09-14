from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#1st param = name, 2nd param = if the bot wants to learn,
#3rd param = gives the chatbot build its logic upon

#chatterbot.logic.BestMatch --> Respond with simple chat strings
omar_bot = ChatBot("Omar-Bot", read_only=False, logic_adapters=[
    {
        "import_path":"chatterbot.logic.BestMatch",
        "default_response":"I don't have answer to this. Ask something else.",
        "maximum_similarity_threshold":0.9 #If similarity < 0.9, return default response
    }
    ])

#Training list
#First element is a question, successive element is answer
#Going to be an even list, because we don't a question without answer
training_list = [
    "Hey",
    "Hey there.",
    "What's your name?",
    "I'm a Omar-Bot",
    "How old are you?",
    "I was born on Sept 14, 2023",
    "Are you mad?",
    "No! I'm not",
    "Do you have Android?",
    "Haha, I have everything :)",
    "What's your favorite food?",
    "I don't eat",
    "What's your job?",
    "I'm here to answer your questions"
]
#Train the chatbot
list_trainer = ListTrainer(omar_bot)
list_trainer.train(training_list)

#Prompt the user for input
while True:
    user_input = input("Human: ")
    #Tells the chatbot to pick out appropriate response to the input
    print("Chatterbot: " + str(omar_bot.get_response(user_input)))