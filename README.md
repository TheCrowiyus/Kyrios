# Kyrios

**Kyrios** is a simple voice chat app that uses AI to hold conversations. Built with Python, it combines real-time voice interaction, audio transcription, and AI-generated responses.

## Features
- **Voice Chat**: Engage in real-time conversations with the AI.
- **Audio Recording and Transcription**: Record your voice and convert it into text seamlessly.
- **AI Responses**: Receive intelligent replies from the AI.

## Technologies Used
- **Python**: Core programming language, utilizing:
  - `Requests`: For handling HTTP requests to Ollama and FasterWhisper Servers.
  - `PyAudio`: For recording audio.
  - `Threading`: Enables simultaneous recording and processing.
- **Ollama**: AI model for generating intelligent responses.
- **FasterWhisper Server**: For efficient audio transcription.

## Getting Started

### Option 1: Self-Hosting

If you'd like to self-host the required servers:

1. **Faster-Whisper Server**  
   - For GPU support:
     ```bash
     docker run --gpus=all --publish 8000:8000 --volume ~/.cache/huggingface:/root/.cache/huggingface fedirz/faster-whisper-server:latest-cuda
     ```
   - For CPU support:
     ```bash
     docker run --publish 8000:8000 --volume ~/.cache/huggingface:/root/.cache/huggingface fedirz/faster-whisper-server:latest-cpu
     ```

2. **Ollama Server**  
   - Using Docker:
     ```bash
     docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
     ```
   - Alternatively, download the binaries from [Ollama Releases](https://ollama.com/).

### Option 2: Use Pre-Configured Servers

If you’d prefer not to self-host:
1. Download a binary from the [Releases](https://github.com/your-username/Kyrios/releases) section of this repository.
2. Use the pre-configured public servers I’m offering for a limited time:
   - **FasterWhisper Server**: Preconfigured for transcription.
   - **Ollama Server**: Preconfigured for AI responses.
3. After downloading the binary, simply run it, and the app will automatically connect to the public servers.

### Basic Setup

For self-hosting:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Kyrios.git
   cd Kyrios
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python Main.py
   ```

## Usage

1. Start the app by running:
   ```bash
   python Main.py
   ```
2. Choose an Option and Enjoy!

## Contributing

This is a simple CLI project I created, but contributions are always welcome!  

To contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

Thank you for helping make Kyrios better!

## License

This project is licensed under the [MIT License](LICENSE).
