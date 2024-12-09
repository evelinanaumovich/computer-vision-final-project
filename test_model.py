from ultralytics import YOLO

loaded_model = YOLO('yolov8n-cls-trained.pt')
loaded_model.predict('test.jpg')

# Extract probabilities
# probs = results.probs
# print(results)
# print(probs.data)
