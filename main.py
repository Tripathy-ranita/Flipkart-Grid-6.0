import cv2
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()
    
cap.set(3, 1280)    # Set width
cap.set(4, 720)     # Set height


while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    cv2.imshow("Image", img)
    
    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
