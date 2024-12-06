from training import train_game_detector
from detection import detect_game

if __name__ == "__main__":
    # Caminhos
    dataset_path = "datasets/dataset.yaml"
    model_path = "models/yolov8/best.pt"
    video_path = "datasets/videos/lol.mp4"

    # Treinar o modelo
    # train_game_detector(dataset_path)

    # Detectar o jogo em um vídeo
    detect_game(video_path, model_path)
