# 2019 FRC Vision Challenge

<!-- TOC depthFrom:2 -->

- [Deliverables](#deliverables)
    - [A fast video feed for drivers](#a-fast-video-feed-for-drivers)
    - [Vision analysis for automatic driver assist](#vision-analysis-for-automatic-driver-assist)
- [Open questions](#open-questions)
- [Delivery schedule](#delivery-schedule)
    - [Week 3](#week-3)
    - [Week 4](#week-4)
    - [Week 5](#week-5)
    - [Week 6 (Length of 1.5 weeks)](#week-6-length-of-15-weeks)
- [Configuring](#configuring)
- [The field elements](#the-field-elements)
    - [On Field Retro-Reflective Tape](#on-field-retro-reflective-tape)
    - [On Ground Gaffers Tape](#on-ground-gaffers-tape)
- [Resources](#resources)

<!-- /TOC -->

## Deliverables

### A fast video feed for drivers

- _how many?_
 1 camera that can be rotated, with a wide field of view.
- _what is fast?_
 A low latency stream (under 150ms lag), with a decent framerate (likely 30fps)
- _required software + hardware_
 Rotation on button press for the servo mounting the camera, changing which way the feed is displaying (vflip)
 Hardware is required for mouting, a moter routed to the top of the robot, where you can rotate to see both the intake and the output. 
- _where to mount for optimum driver experience?_
 Previously mentioned. 

NOTE: We have encounted issues with getting a display while running Mozilla Firefox as the browser hosting the driver dashboard. Chrome seems to work reliably.

### Vision analysis for automatic driver assist

- _choose one or more deliverables_
  1. target relative heading (yaw)
  1. target x,y (in _field_ or _robot_ coordinates?)
  1. target x,y + perpendicular
  1. target/track floor lines?
  1. something else?

- _required software + hardware_
  1. raspis? camera?
  1. leds? infrared?
  1. power requirements?
  1. python, opencv, opencv modules?

- _choose techniques_
  1. distance:  area vs height
  1. color-range + LED/infrared
  1. angle of target markers to disambiguate adjacent targets?

- _specify protocols_
  1. driver-control of camera view
  1. driver-control over vision target and LEDs

## Open questions

The answers to some of these questions will allow us to fill in sections
above.

- how many cameras, how many raspis?
  - 4? (front+back,vision+driver)
  - 2? (shared vision)
  - _conflict between vision and driver requirements?_
  - _is a dual-cam raspi viable?_

- what vision lighting solution? (overlaps with how many cameras)
  - LEDs?
  - infra-red

- if distance detection is required, how will we compute it? How
  will the chosen technique constrain camera positioning?
  - target against a known height
  - target area against a known area
  - other range sensor?

- how best to manage vision latency?
  - convert to robot-relative coordinates at start of path?
  - work in continuous robot-relative coordinates?
  - broadcast IMU heading from robot to vision?

- how will the targeting data be used by robot code?
  - can we operate in robot-relative mode?
  - use path planner?
  - lower-level access to spline and motion-profiles?
  - custom wanted-states with limelight-like control?
  - custom gyro-based pid-loop to rapidly acquire heading?

- how does operator specify target? enter targeting mode?

- can we do vision on the driver station? What are the tradeoffs
  with this option?

- should we worry about field lines/gaffer tape? What is their
  relative priority and return on investment?

## Delivery schedule

### Week 3
 - Work on geometry math
 - End of week three:
    - Spend time working through required trig math to calculate perpindicular bisector
    - Given data(rectangle points) input, have full trig operations completed with correct outputs

### Week 4
 - Receive light test system from Riyadth
 - Spend time working on rectangle extraction from frame input
 - End of week four:
    - Isolate  a rectangle from a frame input
    - Deliver theta, dx, and dy of the perpindicular point between the two rectangles over networktables

### Week 5
  - Test 3d printed / plastic mount of raspicam on test chassis
  - End of week five:
    - Be able to drive to perpindicular bisector point on test chassis
    - Get robot at end of week 5

### Week 6 (Length of 1.5 weeks)
  - In event of dead time (highly likely):
    - Spend time analyzing other team's code
    - Documentation
  - Integration with final robot chassis
  - Plug in correct offset values for final camera placement
  - End of week six:
    - Be able to drive to perpindicular bisector between targets on main chassis

## Configuring

- [Raspi Build Notes](../BuildRaspi.md)
- how to setup/install uv4l
  - choice of framerate, codec, bitrate, port, etc.
- how to setup/install custom vision scripts
  - recipe for uploading scripts from where, which port
    are services operating on, how to test/validate networktables.

## The field elements

[2019VisionImages.zip](https://github.com/wpilibsuite/allwpilib/releases/download/v2019.1.1/2019VisionImages.zip)

### On Field Retro-Reflective Tape

From section 4.10 of the game manual:

A vision target is a pair of 5½ in. (~14 cm) long by 2 in. (~5 cm) wide strips
of 3M 8830 Scotchlite Reflective Material. Strips are angled toward each
other at ~14.5° and such that there’s an 8-in. (~20 cm) gap at their closest
points.

Vision targets on the "front" face of the ROCKET highlight the top of the lowest
PORT and are 39 1/8" above the carpet at their highest point.

Vision targets on the "side" facess of the ROCKET highlight the location of the
top of the lowest HATCH and are 2'7.5" (31.5") above the carpet at their highest point.
This the SAME height as the top of the HATCH opening.

Vision targets also highlight the locations of the tops of each CARGO SHIP HATCH
and the tops of each LOADING STATION HATCH - and at the SAME height as the
ROCKET HATCH targets. (31.5" above the carpet).

HATCH/FUEL delivery stations are separated by 22".  A side of the the cargo ship
contains 3 stations while the "front" has 2 stations.  As stated above, vision
tape is separated by an 8" gap at their closest points at the top.  A very
similar gap occurs between adjacent stations but at the bottom and relative
to the opposite/outside corners.

### On Ground Gaffers Tape

- length, positioning,
- _how close to target before we can acquire line?_
- _what sensors would we need?_

## Resources

- [DeepSpace Vision Target Video](https://www.youtube.com/watch?v=BSihm6xzbWA)
- [Jaci's vision video](https://youtu.be/d9WSAfzA6fc)
  - [discussion of latency & gyro](https://youtu.be/d9WSAfzA6fc?t=2835)
- [ChickenVision](https://github.com/team3997/ChickenVision/blob/master/ChickenVision.py)
- [picamera docs](https://picamera.readthedocs.io)
- [opencv docs](https://docs.opencv.org/3.4.5)
- [opencv pose estimation](https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib)
- [frc distance to known object](https://wpilib.screenstepslive.com/s/currentCS/m/vision/l/682952-2017-vision-examples)
  - does this work for off-axis views? Consider: known height of object/shape
    doesn't suffer as much from off-axis since robot is stuck on the ground.
  ``` java
    distance = targetHeight * YRes / (2*PixelHeight*tan(viewAngle of camera))
  ```
- [pyimagesearch distance to known object](https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/)
  - some formulations use arctan... how does this one avoid that?
- [camera calibration](https://hackaday.io/project/12384-autofan-automated-control-of-air-flow/log/41862-correcting-for-lens-distortions)
