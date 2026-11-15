import sys
from moviepy import ImageSequenceClip, AudioFileClip
# 1. Import the specific AudioLoop effect class for MoviePy v2
from moviepy.audio.fx import AudioLoop

# 2. Collect all your frame_XX.png image arguments from the terminal
images = [arg for arg in sys.argv[1:]]

# 3. Set the frame rate to 5 (0.2 seconds per frame)
clip = ImageSequenceClip(images, fps=1)

# 4. Load your song 
audio = AudioFileClip("song.mp3")

# 5. Use with_effects and AudioLoop to handle the infinite repetition matching the video length
audio_looped = audio.with_effects([AudioLoop(duration=clip.duration)])

# 6. Bind the audio to the clip using with_audio (replaces old set_audio)
clip = clip.with_audio(audio_looped)

# 7. Output the file directly as an MP4 video
clip.write_videofile("battle_sequence.mp4", fps=24)
