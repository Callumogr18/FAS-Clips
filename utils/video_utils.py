import cv2

def read_video(video_path):
    # Captures specified video
    cap = cv2.VideoCapture(video_path)
    frames = []
    # Continuously loop
    while True:
        # ret = bool value, frame = Reads individual frames from video over loop
        ret, frame = cap.read()
        # If there is not another frame, break from while loop
        if not ret:
            break
        # Else, append frame to list of frames
        frames.append(frame)
    return frames


def save_video(output_video_frames, output_video_path):
    # Define the output format, XVID 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    """
    Then define a video writer. It takes the video path, 
    output video type, number of frames p/s and frame width and height
    """
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    # Loop over each frame and write it to the video writer
    for frame in output_video_frames:
        out.write(frame)
    return out.release()