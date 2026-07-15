from moviepy import VideoFileClip, vfx

clip = VideoFileClip("airplanes.mp4")
trimmed_clip = clip.subclipped(1*60+50, 9*60+50) # in seconds
trimmed_clip.write_videofile("airplanes_out.mp4")
clip.close()
trimmed_clip.close()

# Default 854 x 480
clip = VideoFileClip("./images/airplanes_out.mp4")
cropped_clip = clip.cropped(x1=120, y1=0, x2=734, y2=400)
cropped_clip.write_videofile("./images/airplanes_out_cropped.mp4")
clip.close()
