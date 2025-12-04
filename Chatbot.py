import re

patterns_responses = {
    r'\b(hi|hello|hey)\b': "Hello! How can I help you today?",
    r'good (morning|afternoon|evening)': "Good day! How can I assist you?",
    r'how are you': "I am just a rule-based bot, but I am doing great!",
    r'what is you name | who are you': "I am a simple Chatbot who responses according to some predifiend rules.",
    r'what can you do|what is your purpose': "I can respond to basic greetings and simple questions using predefined rules.",
    r'Chat Related help': "You can say hi, ask my name, ask how I am, or type bye to exit.",
    r'thank you|thanks': "You are most welcome!",
    r'bye|goodbye|see ya': "Good night it was nice talking to you.",
    r'are you real': "I am a program, not a human, but I can still chat with you.",
}

default_response = "Sorry, I did not understand that. Could you please rephrase?"


def get_response(user_input: str) -> str:
    """
    Match user_input against predefined regex patterns and
    return the corresponding response. If nothing matches,
    return a default response.
    """
    text = user_input.strip()

    for pattern, response in patterns_responses.items():
        if re.search(pattern, text, re.IGNORECASE):
            return response

    return default_response

def run_chatbot():
    print("Chatbot: Hi! I am your rule-based chatbot.")
    print("Chatbot: You can talk to me, and type 'bye' or 'exit' to end the chat.")

    while True:
        user_input = input("You: ")

        if re.search(r'\b(bye|exit|quit)\b', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break

        bot_reply = get_response(user_input)
        print("Chatbot:", bot_reply)

if __name__ == "__main__":
    run_chatbot()
