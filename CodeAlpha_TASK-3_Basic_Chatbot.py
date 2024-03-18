import random

# Define responses for different types of user inputs
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Nice to meet you!", "Hello again!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm fantastic!", "Feeling good!", "I'm feeling splendid!"],
    "good": ["That's great!", "Awesome!", "Good to hear!", "Fantastic!", "Wonderful!"],
    "hi": ["hi how are you ","hello how are you "],
    "fine": ["Awesome!", "Good to hear!",],
    "age": ["As an AI developed by OpenAI, I don't possess personal characteristics such as age. I'm here to assist you with your inquiries regardless of the time. How can I assist you further?"],
    "joke": ["Why don't skeletons fight each other?They don't have the guts!","Sure, here's a classic AI-themed joke for you:Why did the AI go to therapy?Because it had too many neural networks and needed to unwind!"],
    "bad": ["I'm sorry to hear that.", "That's unfortunate.", "Hope things get better soon.", "Hang in there!", "Sending positive vibes your way."],
    "bye": ["ok bye!", "See you later!", "Bye! Take care!", "Until next time!", "Farewell!"],
    "exit": ["Goodbye!", "See you later!", "Bye! Take care!", "Until next time!", "Farewell!"],
    "default": ["Sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure I follow.", "I'm still learning!", "Let's try something else!""search google or www",],
}

def chatbot():
    print("Hello! I'm a chatbot. You can start chatting with me. Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit"]:
            print(random.choice(responses["bye"]))
            break
        
        # Look for a response based on user input
        response = responses.get(user_input, responses["default"])
        print("chatbot: "+random.choice(response))

# Run the chatbot
chatbot()
