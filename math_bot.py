from chatterbot import ChatBot

math_bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("--------Math-Bot---------")
while True:
    math_eq = input("Type a math equation: ")
    print("Math-Bot: " + str(math_bot.get_response(math_eq)))