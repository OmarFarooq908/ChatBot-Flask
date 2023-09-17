from chatterbot import ChatBot

units_bot = ChatBot("units", logic_adapters=['chatterbot.logic.UnitConversion'])

while True:
    user_units = input("Unit conversion: ")
    chatbot_response = str(units_bot.get_response(user_units))
    print(chatbot_response)