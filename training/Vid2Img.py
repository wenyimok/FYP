import os
import cv2

folder_path="D:\GIT-Mine(DONTINIT)\A-FYP\moktrial2\Working"
# List all files in the folder
files = os.listdir(folder_path)

# Filter out only the video files (you can add more video file extensions if needed)
# video_files = [f for f in files if f.endswith((".mp4", ".avi", ".mov"))]
video_files = ['VID_20240106_140050.mp4']

count = 0
# Loop through each video file
for video_file in video_files:
    # Construct the full path to the video file
    video_path = os.path.join(folder_path, video_file)

    # path of video
    vidcap = cv2.VideoCapture(video_path)
 
    frame_count=0
    while vidcap.isOpened:
        ret, frame = vidcap.read()
        total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count += 1
        
        if frame_count==total_frames:
            break

        if frame_count % 20 == 0:
            # cv2.imwrite("D:\Work\FYP\Image\sawi%d.png" % count, frame )
            cv2.imwrite("D:\GIT-Mine(DONTINIT)\A-FYP\moktrial2\Vid2Img\VID_20240106_140050\Pred%d.png" % count, frame )
            resized_frame=cv2.resize(frame,(450,600))
            cv2.imshow('frame', resized_frame)
            count+=1

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

vidcap.release()
cv2.destroyAllWindows() 

# Annotation is done using Make Sense Ai