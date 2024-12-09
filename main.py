import cv2
from ultralytics import YOLO
import subprocess


# Load the trained YOLO classification model
model = YOLO('yolov8n-cls-trained.pt')

# Define class names (update with your actual class labels)
class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

# Open the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default webcam; change if necessary

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to exit.")

prev_letter = None
counter = 0

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image from webcam.")
        break

    # Resize the frame to the required input size (optional, but recommended for consistent results)
    resized_frame = cv2.resize(frame, (224, 224))  # Adjust to the input size of your model

    # Convert the frame to RGB (model expects RGB format)
    frame_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    # Predict the class of the image
    results = model.predict(frame_rgb, verbose=False)

    # Extract the top prediction
    if results:
        probs = results[0].probs  # Get the probabilities
        # print(probs.top1)
        # print(probs.top5)
        # print(probs)

        text = class_names[probs.top1]
        if (probs.top1conf.item() > 0.40):
            print(probs.top1conf, text)   
            if (prev_letter != text):
                # print(prev_letter, text)
                if (counter == 3):
                    counter = 0
                    prev_letter = text
                    subprocess.run(["espeak", text])
            elif (prev_letter == text):
                counter += 1

        else:
            text = ""

        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with the prediction
    cv2.imshow("Webcam - YOLO Classification", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
