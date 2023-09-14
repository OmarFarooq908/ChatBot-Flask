from chatterbot import ChatBot

#1st param = name, 2nd param = if the bot wants to learn,
#3rd param = gives the chatbot build its logic upon

#chatterbot.logic.BestMatch --> Respond with simple chat strings
omar_bot = ChatBot("Omar-Bot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

#Train the chatbot