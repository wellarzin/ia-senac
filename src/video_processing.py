import cv2

def process_stream(stream_url, process_frame):
    """
    Processa um stream de vídeo e aplica uma função aos frames.
    """
    cap = cv2.VideoCapture(stream_url)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Processar o frame com a função fornecida
        process_frame(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()