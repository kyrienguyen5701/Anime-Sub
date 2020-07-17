from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 0
end_time = int(input())
ffmpeg_extract_subclip("Kimiiro Subliminal.mp4", start_time, end_time, 
    targetname="Kimiiro Subliminal t={}s.mp4".format(end_time))