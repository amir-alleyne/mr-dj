# Mr-DJ

Mr-DJ is a monolithic DJ mixing application that automatically analyzes and mixes songs based on their BPM and beat similarity. Whether you're a casual music enthusiast or a budding DJ, Mr-DJ makes it easy to create seamless mixes by matching songs with similar tempos and applying smooth transitions.

# Features
Song Upload: Easily add multiple audio tracks.
BPM Detection: Automatically analyze each track using Librosa to detect its BPM.
Beat Tracking: Identify beat positions for precise alignment.
Audio Mixing: Use crossfades and time-stretching (via Pydub and other libraries) to create smooth transitions between songs.
Modern UI: Enjoy an intuitive interface built with React and TypeScript.

# Technologies
Backend: Python, Flask, Librosa, Pydub
Frontend: React with TypeScript
Audio Processing: Librosa for BPM detection and beat tracking; Pydub for audio mixing
