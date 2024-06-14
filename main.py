from ultralytics import YOLO
import cv2
import os


model = YOLO("yolov8n-face.pt")  

video_path = "la_cabra.mp4"


if not os.path.isfile(video_path):
    print(f"Error: Caminho do video '{video_path}' não encontrado.")
    exit()

cap = cv2.VideoCapture("la_cabra.mp4")


if not cap.isOpened():
    print("Error: Não foi possível abrir o vídeo.")
    exit()


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('xablau.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break


    # Afim de evitar Falsos positivos e não sobrecarregar o processamento, foi utilizado um threshold de 0.7 de confiança para a detecção de faces. Ou seja, apenas as faces com confiança maior que 0.7 serão detectadas e desenhadas na imagem. 
    results = model.predict(frame, conf=0.7)  

    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy() 
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)


    out.write(frame)

    cv2.imshow("xablau", frame)

    if cv2.waitKey(1) == 13: 
        break




cap.release()
out.release()
cv2.destroyAllWindows()
