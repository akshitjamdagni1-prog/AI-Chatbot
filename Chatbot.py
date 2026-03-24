print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Kaise ho?")
    elif user == "hi":
        print("Bot: Hi! Kya haal hai?")
    elif user == "name":
        print("Bot: Mera naam AI Bot hai 😄")
    elif user == "course":
        print("Bot: Aap BCA AIML kar rahe ho 🔥")
    elif user == "career":
        print("Bot: Aapka future bright hai 💯")
    elif user == "bye":
        print("Bot: Bye! Have a great day 👋")
        break
    else:
        print("Bot: Sorry, mujhe samajh nahi aaya 😅")
