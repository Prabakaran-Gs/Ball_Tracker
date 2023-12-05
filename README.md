  <h1>Ball Tracking with OpenCV</h1>

  <p>This repository contains Python code for tracking a colored ball in a video using OpenCV. The script reads a video file, isolates the ball based on its color in the HSV color space, and tracks its position over time. The detected ball is marked with a green circle, and its trajectory is displayed as a red line.</p>

  <h2>Usage</h2>

  <p>1. Make sure you have Python and OpenCV installed on your system.</p>
  <p>2. Run the provided Python script:</p>

  ```bash
  python ball_tracking.py
  ```

  <h2>Configuration</h2>

  <p>Before running the script, you may need to adjust the following parameters:</p>

  <ul>
      <li>Video file: Change the file path in the script to the video you want to analyze.</li>
      <li>Ball color: Define the RGB color of the ball in the script.</li>
      <li>Color range: Adjust the HSV color range based on your ball's color. Fine-tune the lower_color and upper_color values.</li>
      <li>Trajectory length: Set the maximum length of the displayed trajectory.</li>
  </ul>

  <h2>Controls</h2>

  <p>Press 'q' to exit the video playback and close the application.</p>

  <h2>Dependencies</h2>

  <p>The script uses the OpenCV library for computer vision tasks. Make sure to install it using:</p>

  ```bash
  pip install opencv-python
  ```


  <h2>Author</h2>

  <p>Prabakaran GS</p>

