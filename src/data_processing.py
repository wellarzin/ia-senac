import cv2
import os

def extract_frames(video_path, output_folder, fps=1):
    """
    Extrai frames de um vídeo e os salva em uma pasta.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    interval = frame_rate // fps
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % interval == 0:
            output_path = os.path.join(output_folder, f'frame_{frame_id:04d}.png')
            cv2.imwrite(output_path, frame)
            frame_id += 1

    cap.release()
    print(f"Frames salvos em {output_folder}")