# AI Reel Generator 🎬

An AI-powered web application that generates short vertical reels from images and text using Flask, ElevenLabs, and FFmpeg.

## Features
- Upload images and a text prompt
- Generate AI voiceover using ElevenLabs
- Create Instagram-style reels (1080x1920)
- View generated reels in a gallery

## Tech Stack
- Python
- Flask
- ElevenLabs API
- FFmpeg

## How It Works
1. User uploads images and text
2. Text is converted to speech
3. Images + audio are merged into a reel
4. Final video is saved and displayed

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Create a `.env` file with:
5. Run `main.py`
6. Run `generate.py`

## Security
API keys are stored securely using environment variables and are not committed to the repository.

## Author
Soubhagya Yashvardhan-https://www.linkedin.com/in/soubhagya-yashvardhan-19514634a/
