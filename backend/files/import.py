from pydub import AudioSegment
import vlc

# Load your two songs
song1 = AudioSegment.from_file("././audio/bobby.mp3")
song2 = AudioSegment.from_file("././audio/sheff.mp3")

crossfade_duration = 3000  # 3 seconds

# Create a mix: append song2 to song1 with crossfade
mixed = song1.append(song2, crossfade=crossfade_duration)
mixed.export("mixed_output.mp3", format="mp3")
