from ultralytics import YOLO

def train_game_detector(data_path, epochs=50, imgsz=640):
    """
    Treina um modelo YOLOv8 para detectar jogos com base em HUDs e personagens.
    """
    model = YOLO('yolov8n.pt') 
    model.train(data=data_path, epochs=epochs, imgsz=imgsz)
    print("Treinamento concluído!")
