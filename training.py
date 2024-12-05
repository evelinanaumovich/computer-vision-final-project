import os 

# import I3D model
from tensorflow.keras.models import InceptionI3d

# Load a model
model = InceptionI3d('yolov8n-cls.pt') 

# Train the model
model.train(data='./Images', epochs=5)

# Validate the model
metrics = model.val()
metrics.top1 # top1 accuracy
metrics.top5 # top5 accuracy

results = model.predict('./Images/test/fire/frame209.jpg')

probs = result.probs
print(probs.data)