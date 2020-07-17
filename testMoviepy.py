from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 0
end_time = int(input())
ffmpeg_extract_subclip("Kimiiro Subliminal.mp4", start_time, end_time, 
    targetname="Kimiiro Subliminal t={}s.mp4".format(end_time))

import moviepy.editor as mpe
video = mpe.VideoFileClip('Kimiiro Subliminal.mp4')
audio = video.audio
audio.write_audiofile('Kimiiro Subliminal.mp3')

from pydub import AudioSegment
from pydub.silence import split_on_silence

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

song = AudioSegment.from_mp3('Kimiiro-Subliminal.mp3')

# Split track where the silence is 2 seconds or more and get chunks using 
# the imported function.
chunks = split_on_silence (
    song,
    min_silence_len = 2000,
    # Consider a chunk silent if it's quieter than -16 dBFS.
    # (You may want to adjust this parameter.)
    silence_thresh = -16
)

for i, chunk in enumerate(chunks):
    # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    silence_chunk = AudioSegment.silent(duration=500)

    # Add the padding chunk to beginning and end of the entire chunk.
    audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk.
    normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

    # Export the audio chunk with new bitrate.
    print("Exporting chunk{}.mp3.".format(i))
    normalized_chunk.export(
        ".//chunk{}.mp3".format(i),
        bitrate = "192k",
        format = "mp3"
    )