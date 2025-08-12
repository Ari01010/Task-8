import random

def rule_based_chatbot():
    """
    A simple function to simulate a rule-based chatbot.
    """
    print("Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")

    # This creates an infinite loop, so the conversation can continue.
    while True:
        # Get user input and convert it to lowercase for easier matching.
        user_input = input("You: ").lower()

        # Rule 1: Check for a specific keyword to end the conversation.
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break  # This keyword exits the loop.

        # Rule 2: Check for greetings.
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            responses = ["Hello there!", "Hi!", "Hey! How can I help you?"]
            print(f"Chatbot: {random.choice(responses)}")

        # Rule 3: Check for questions about the chatbot's name.
        elif "what is your name" in user_input:
            print("Chatbot: I am a simple chatbot created to demonstrate Python.")

        # Rule 4: Check for questions about how the user is doing.
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly! Thanks for asking.")

        # Rule 5: Check for questions about the chatbot's capabilities.
        elif "what can you do" in user_input or "help" in user_input:
            print("Chatbot: I can respond to simple greetings and questions. Try asking me 'what is your name' or 'how are you'. Type 'bye' to end our chat.")

        # Default Rule: If no other rule matches.
        else:
            responses = ["I'm not sure how to respond to that. Could you try rephrasing?", "Sorry, I didn't understand that. You can ask for 'help'.", "My apologies, that's beyond my current knowledge."]
            print(f"Chatbot: {random.choice(responses)}")

# This line ensures the chatbot function runs when the script is executed.
if __name__ == "__main__":
    rule_based_chatbot()
