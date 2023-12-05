import cv2
import numpy as np

# Load your video
cap = cv2.VideoCapture("testing.mp4")

# Define your ball color in RGB format
ball_color_rgb = np.array([208, 204, 42])  # RGB color

# Convert RGB to HSV
ball_color_hsv = cv2.cvtColor(np.uint8([[ball_color_rgb]]), cv2.COLOR_RGB2HSV)[0][0]

# Define a color range based on your ball color in HSV format
# You may need to adjust these values based on your ball's color
lower_color = np.array([ball_color_hsv[0] - 10, ball_color_hsv[1] - 30, ball_color_hsv[2] - 30])
upper_color = np.array([ball_color_hsv[0] + 10, ball_color_hsv[1] + 30, ball_color_hsv[2] + 30])

# Initialize variables to store the ball's trajectory
max_trajectory_length = 10  # Maximum length of the trajectory
trajectory = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask to isolate the ball based on color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through detected contours
    for contour in contours:
        # Calculate the center and radius of the enclosing circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw a circle around the detected ball
        cv2.circle(frame, center, radius, (0, 255, 0), 2)

        # Append the current position to the trajectory
        trajectory.append(center)

    # Draw the trajectory as a line connecting previous positions
    for i in range(1, len(trajectory)):
        cv2.line(frame, trajectory[i - 1], trajectory[i], (0, 0, 255), 2)

    # Ensure the trajectory list does not exceed the maximum length
    if len(trajectory) > max_trajectory_length:
        del trajectory[0]

    # Display the frame with the detected ball and trajectory
    cv2.imshow("Ball Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
