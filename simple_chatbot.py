# Define a dictionary of possible user inputs and their corresponding responses
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing well, thanks for asking. How about you?",
    "good": "Glad to hear it!",
    "not good": "Sorry to hear that. Is there anything I can do to help?",
    "bye": "Goodbye!",
    "see you later": "See you later!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!"
}


# Define a function to handle user input and generate a response
def respond(user_input):
    for key in responses:
        if key == user_input.lower():
            return responses[key]
    return "I'm sorry, I don't understand what you're saying."


# Define a loop to continuously prompt the user for input and respond to it
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    bot_response = respond(user_input)
    print("Bot: " + bot_response)
