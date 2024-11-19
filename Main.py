import LLM_Chat
import LLM_Voicechat


def main():
    while True:
        print(
            "\nWelcome to LLM Chat!\n"
            "Would you like to chat or voice chat?\n"
            "1. Chat\n"
            "2. Voice Chat\n"
            "3. Exit"
        )
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            LLM_Chat.chat()
        elif choice == "2":
            LLM_Voicechat.voicechat()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
