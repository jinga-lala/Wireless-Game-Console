# WIRELESS GAME CONSOLE

### Yash Jain           yash.jain3599@gmail.com
### Ritik Roongta       roongta.ritik20@gmail.com

## Description


Our​ project basically focuses on gesture-controlled movement of
the cursor on the desktop screen (in short, a basic prototype of
wii remote).
The device appearance is of a small remote (as small as possible)
equipped with left and right click buttons (similar to a computer
mouse) and thus moving the remote subsequently moves the
cursor on the screen in front of you. Also the information of
pitch and bank of the remote (with respect to original state) also
gets recorded and transmitted to provide a better gaming
experience.
We are using a camera on our remote with a marker consisting
of a big “Green circle” placed on the top of the computer screen.
Using the relative change in position of “Green Circle” perceived
by the camera (processed by image processing) we infer the
relative change in the position of the remote and then those data
is sent to a Raspberry Pi which further passes it on to the
computer via remote desktop connection (SSH).


## Technical Aspect of the Project:

**Raspberry Pi** - It was the brain of the remote. We used it to process
all the information according to our needs and help us to perform
desired functions.

**MPU6050** - It was used to get the accelerometer and gyrometric
values. Using them, we could detect how fast the remote move and
accordingly move the cursor.

**PiCamera** - ​ It was used to detect the Green Circle and using its
relative position w.r.t. camera, the cursor was accordingly moved.

## Implementation:

● Signal generation - We used a marker as a “Green Circle”
placed at the top of the computer screen to help us determine
the relative change in the position of our remote.

● Chassis and remote development - the basic skeleton of the
Remote consisted of a simple Raspberry Pi case which various
other equipments attached to it.

● Signal capturing - ​ A Camera was attached at the nose of the
remote to record the position of the “Green Circle” and we used
the opencv functions (image processing) to move the cursor of
the mouse accordingly.

● Signal processing ​ - The​ information received from the
accelerometer (attached in MPU 6050) helped us to detect how
fast that change in position has occurred.

● Signal transport - ​After processing these two data sets, by the
Raspberry Pi, the precise movement of cursor was mimicked
and sent to the computer via a remote desktop connection.

● Further variations - Left and right buttons was also
subsequently synced with Raspberry Pi using GPIO pins.

● The tilting part  - The gyroscope (present in MPU 6050) gave
signals to the Raspberry PI which was further perceived by the
computer wherever required.

## Theory Involved:

#### 1) HOUGH TRANSFORM

This is the image processing algorithm that we be used in our
camera. 
Using the above technique, we processed the image of the
“Green Circle” ( our marker) perceived by the Camera.
This technique used the  **voting procedure** carried out in a defined
**parameter space** (a N-dimensional space, where N is the number of
unknown variables).
In our project, we focussed on CIRCLE HOUGH TRANSFORM
**(CHT)** because of the “Green Circle” that appears as a ​ **circular
spot** ​ in the image captured by the IR Camera.
Finally, using **Accumulator** ​ **matrix** (obtained by processing the
image) and ​ **voting procedure** ​, final image signal is forwarded.

#### 2) ​ RED FILTERING

Red filter needs to be applied to the image for **better** ​ **clarity** ​. For this,
we converted the **RGB** ​ (Red,​ Green and Blue) image​ into ​ **HSV**
(Hue-Saturation-Value) ​image. Then the color information of HSV
image was used to filter out a specific range of colors.

#### 3) ​ THRESHOLDING

We needed **SIMPLE** ​ as well as **ADAPTIVE** ​ Thresholding depending
upon the image quality and precision of measurement.
In Simple Thresholding, we needed a **grayscale** ​ **image** and a ​ **global
threshold pixel value** ​, which was used to​ classify the pixel values.
Using this, we assigned a value to every pixel depending on whether
its pixel value is more than the threshold value.

In Adaptive Thresholding, instead of having a global threshold value
for the entire image, we have, a **particular** ​ **threshold** value for **small** ​
**regions** in the image resulting in different thresholds for different
regions and it gave better results for images with **varying** ​
**illumination** ​.


## Materials
```
● Raspberry Pi 3 Model B+ ( x2)

● MPU 6050

● Infrared Pi Camera_

● Power Bank (didn’t purchased)

● Jumper Wires_

● Breadboard ( didn’t purchased)

● PCB Board

● San Disk 16 gb Memory Card

● Raspberry Pi case_

● HDMI cable (MHI cable kit)
```
**_For cost, refer to the following bills_**
https://drive.google.com/open?id=10lKkKuCMHKuxaIgdV7GdnbmPDKMzqA


## Project Repository and Video:

https://www.youtube.com/watch?v=UF_NtYICshQ

https://github.com/jinga-lala/Wireless-Game-Console

## Reference Links:

These websites played a pivotal role in our understanding of the
project and helped us to implement even little technicalities with
proper precision.

https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

http://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with

http://pyautogui.readthedocs.io/en/latest/mouse.html

https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/

https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

https://www.youtube.com/watch?v=ETAKfSkec6A&feature=youtu.be&t=2m29s




