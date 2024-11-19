import LLM_Generation

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        response = LLM_Generation.generate_response(user_input)
        print('LLM Agent:', response)

if __name__ == "__main__":
    chat()

