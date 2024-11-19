import wave
import pyaudio
import threading

def record_audio(output_filename='output.wav', chunk_size=1024, format=pyaudio.paInt16, channels=2, rate=44100, stop_event=None):
    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)

        #print("Recording started")
        frames = []

        while not stop_event.is_set():
            data = stream.read(chunk_size, exception_on_overflow=False)
            frames.append(data)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save the recorded data to a WAV file
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

# Global stop event and recording thread
stop_event = threading.Event()
recording_thread = None

def start_recording():
    global stop_event, recording_thread
    stop_event.clear()
    recording_thread = threading.Thread(target=record_audio, args=('output.wav', 1024, pyaudio.paInt16, 2, 44100, stop_event))
    recording_thread.start()

def stop_recording():
    global stop_event, recording_thread
    stop_event.set()
    recording_thread.join()  # Wait for the recording thread to finish
    #print("Recording stopped and file saved.")


if __name__ == "__main__":
    input("Press Enter to start recording...")
    start_recording()
    input("Press Enter to stop recording...")
    stop_recording()





