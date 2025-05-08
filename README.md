<h1 size="35px"><b>Face Detecting Laser Turret</b></h1>

<b>Keywords: Arduino, pyfirmata, Python, OpenCV, Numpy, Computer Vision, Face Detection, Servo Operations</b>

<br>
<p>This project brings together computer vision (via a webcam of your PC), servo motors, and an Arduino to create a face-tracking system. The goal is to detect a person’s face using the webcam and move two servo motors to "follow" that face automatically while pointing its laser.

Think of it like a robotic camera that tries to keep a moving person in its view by adjusting its position left-right and up-down using servos</p>
<br>
<h2>Components</h2>
<ul>
<li>Webcam – Captures real-time video.</li>
<li>Arduino (with servos) – Controls two motors to move in horizontal and vertical directions.</li>
<li>Python libraries – OpenCV for face detection, PyFirmata for Arduino communication.</li>
<li>FaceDetector Module – Used for detecting faces in the video (assumed as part of the code).</li>
</ul>

!Arduino(arduino.jpg)
!Turret(turret.jpg)
<br>
<h2>Connecting to Arduino</h2>
<ol>
<li>The Arduino is connected on COM8 (you can change the port if needed).</li>
<li>Two servos are connected to pins 10 and 12 of the Arduino.</li>
<li>The laser Enable / Signal is also connected to Arduino using pin 11.</li>
<li>Do the necessary wiring between the rest.</li>
</ol><br>
<h2>How Main Loop Works ?</h2>

<h3>It works in the following sequence</h3>
<ol>
<li>Main Loop: Continuously reads frames from the camera.</li>
<li>Detect Face: Uses "detector.findFaces()" to look for faces in each frame. If a face is found, it extracts the coordinates (fx, fy) of the first detected face.</li>
<li>Convert Coordinates to Servo Angles: The face’s position is mapped to servo angles using `np.interp()` to make the servos move accordingly:
<ol>
<li>Horizontal (servoX): Maps `fx` to angles between 140 and 30 degrees.</li>  
<li>Vertical (servoY): Maps `fy` to angles between 55 and 125 degrees.</li>
</ol></li>
<li>Ensure Servo Angle Limits: Makes sure servo angles stay within 0 to 180 degrees to prevent any errors, just in case.</li>

<li>If Face Found:  
<ol>
<li>Update servo positions to align with the face.</li>
<li>Turn on the laser using "laser_pin.write(1)".</li>
<li>Display target locked message and draw a red circle on the face.</li>
</ol></li>

<li>If No Face Found:  
<ol>
<li>Reset servo to center (90,90).</li>  
<li>Turn off the laser using "laser_pin.write(0)".</li>
<li>Display "NO TARGET" message.</li>
</ol></li>

<li>Send Servo Values to Arduino: The new servo positions are sent to the X and Y servos via "servo_pinX" and "servo_pinY".</li>

<li>Show Image with Annotations: Displays the updated video feed with all markings using "cv2.imshow()".</li>

<p>This loop keeps running until you stop it, making the camera and servos track any detected face and align accordingly with the help of the laser.</P>

<br>

<h1> Thank You for considering this project </h1>

<h3>Made by:</h3>
<ul>
<li>Dhruv Singh           <br><b>N292 70472200318</b></li>
<li>Kabeer Choudhary      <br><b>N289 70472200315</b></li>
<li>Prakhar Agarwal       <br><b>N262 70472200256</b></li>
</ul>
