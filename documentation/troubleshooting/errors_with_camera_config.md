# Errors with Camera Configuration

## Overview

If you are encounter issues when using a camera, follow this troubleshooting guide for possible solutions.

When setting up your camera for the Jetson Nano, attach/plug in the camera before turning on the Jetson Nano.  Never unplug the camera when your Jetson Nano is turned on and wait until the Jetson Nano is completely off, to prevent damaging the camera.

## Flir Lepton 3.5

The Lepton camera is using a PureThermal mini USB breakout board to connect to Jetson Nano. 

The PureThermal mini, when plugged into micro-usb power and a Lepton is inserted in the socket LED will flash slowly.  When the video is being transmitted to the viewing program, LED will flash more rapidly.  This will tell you if the PureThermal mini board is working.

Follow the USB troubleshooting steps to troubleshoot the Lepton 3.5 camera.

However, if this does not fix the problem, make sure that you have all prerequisites libraries installed (including `flirpy`).  Instructions for downloading and installing `flirpy` are in guide [here](documentation/manual/environment_setup/jeston_nano_env_setup.md).

## USB

For USB cameras, you can use a g-streamer pipeline to access a camera feed.  A possible issue is that the Jetson Nano has not got the compatible video and image libraries/codecs installed.  To verify this, run the following commands:

```
$ sudo apt-get install libtbb2 libtbb-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install libxvidcore-dev libavresample-dev
$ sudo apt-get install libtiff-dev libjpeg-dev libpng-dev
$ sudo apt-get install libv4l-dev libdc1394-22-dev
$ sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

Restart the Jetson Nano and run this simple OpenCV script to test the camera:

```
import cv2

for i in range(10):
    print (f"Testing for presense of camera #{i}...")
    
    cap = cv2.VideoCapture(i)
    cap.open(i, cv2.CAP_V4L)
    if cap.isOpened():
        print(f"Camera opened at {i}")
        break

if not cap.isOpened():
    print ("[!] Camera cannot be found [!]")
    exit(1)


while(True):
    # capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows() 
```

A camera feed should now show and the specific ID to open the `cv2.videocapture(id)`.  Whenever you need to open the capture in the future. use that ID to open the video capture.

If you receive the error message "Camera can not be found!", that means that the Jetson Nano cannot identify the camera.  In this case, try unplugging the camera, restart the Jetson Nano, and plug the camera back in.

This could also mean the camera is not getting enough power to run.  You could solve this by having a more powerful power supply. NVIDIA suggests [Adafruit's 5V 2.5A](https://www.adafruit.com/product/1995) as a good power supply.  A good quality power supply that can deliver 5V⎓2A at the developer kit’s Micro-USB port.

If neither of these methods sorts your issue, there is a good chance the camera is broken.