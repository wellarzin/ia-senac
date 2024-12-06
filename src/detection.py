import cv2
import torch
from ultralytics import YOLO

def detect_game(video_path, model_path):
    """
    Detecta jogos em um vídeo com base no HUD ou outros elementos específicos.
    """

    # Carregar o modelo treinado
    model = YOLO(model_path)

    # Abrir o vídeo
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Erro ao abrir o vídeo!")
        return

    # tamanho desejado para a janela (exemplo: 640x360)
    window_width = 1000
    window_height = 600

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break 

        # Realizar a detecção
        results = model(frame)

        
        boxes = results[0].boxes.xywh  
        confidences = results[0].boxes.conf  
        class_ids = results[0].boxes.cls

        # Obter os nomes das classes 
        names = results[0].names  

        # Iterar sobre as detecções
        for i, box in enumerate(boxes):
            x1, y1, w, h = box  
            confidence = confidences[i]  
            class_id = int(class_ids[i]) 

            label = names[class_id]  

            # Desenhar a caixa de detecção
            cv2.rectangle(frame, (int(x1 - w/2), int(y1 - h/2)), (int(x1 + w/2), int(y1 + h/2)), (0, 255, 0), 2)

            # Adicionar o texto com o nome do jogo e a confiança
            cv2.putText(frame, f'{label} {confidence:.2f}', 
                        (int(x1 - w/2), int(y1 - h/2) - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Redimensionar o frame para o tamanho desejado (exemplo: 640x360)
        resized_frame = cv2.resize(frame, (window_width, window_height))

        # Exibir o vídeo com as detecções
        cv2.imshow('Game Detection', resized_frame)

        # Fechar a janela ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechar o vídeo e as janelas ao terminar
    cap.release()
    cv2.destroyAllWindows()
