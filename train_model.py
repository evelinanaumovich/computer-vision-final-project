from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-cls.pt') 

# Train the model
model.train(data='./images', epochs=5)

# Save the trained weights
model.save('yolov8n-cls-trained.pt')  # Save the model's weights

# Validate the model
metrics = model.val()
print("Top1 Accuracy:", metrics.top1)  # Top1 accuracy
print("Top5 Accuracy:", metrics.top5)  # Top5 accuracy

# Perform inference on a test image
results = model.predict('test.jpg')

# Extract probabilities
probs = results.probs
print(results)
print(probs.data)

# Later, you can reload the model with the saved weights
# loaded_model = YOLO('yolov8n-cls-trained.pt')
