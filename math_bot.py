from chatterbot import ChatBot

math_bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("--------Math-Bot---------")
while True:
    math_eq = input("Type a math equation: ")
    try:
        math_response = math_bot.get_response(math_eq)
        print("Math-Bot: ", math_response)
    except Exception as e:
        print("Error: ", e)