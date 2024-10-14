import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename



def classify_fruit(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_rotten = np.array([0, 0, 0])
    upper_rotten = np.array([180, 255, 80])
    
    mask_rotten = cv2.inRange(hsv, lower_rotten, upper_rotten)
    
    rotten_area = cv2.countNonZero(mask_rotten)
    total_area = image.shape[0] * image.shape[1]
    
    rotten_percentage = (rotten_area / total_area) * 100

    threshold = 10
    
    if rotten_percentage > threshold:
        return "Rotten", rotten_percentage
    else:
        return "Fresh", rotten_percentage
    

Tk().withdraw()



file_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

if file_path:
    image = cv2.imread(file_path)

    resized_image = cv2.resize(image, (600, 600))

    status, rotten_percent = classify_fruit(resized_image)

    cv2.putText(resized_image, f"Status: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(resized_image, f"Rotten Area: {rotten_percent:.2f}%", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Fresh Produce Inspection', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Status: {status}")
    print(f"Rotten Area: {rotten_percent:.2f}%")
else:
    print("No file selected.")
