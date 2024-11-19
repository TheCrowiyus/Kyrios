import threading
import Audio_Recording
import Audio_Transcription
import LLM_Generation



def voicechat():
    print("Start talking with the bot. Press Enter to start user input (type 'quit' to stop)!")
    while True:
        user_input = input("")
        if user_input.lower() == "quit":
            break
        recording_thread = threading.Thread(target=Audio_Recording.start_recording)
        recording_thread.start()
        input("Press Enter to stop recording...")
        Audio_Recording.stop_recording()
        recording_thread.join()  # Wait for the recording thread to finish

        transcription = Audio_Transcription.transcribe_audio("output.wav")
        print('User:', transcription)

        response = LLM_Generation.generate_response(transcription)
        print('LLM Agent:', response)


if __name__ == "__main__":
    voicechat()

