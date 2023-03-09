## IROC
 - This is a simple project to understand how OpenCv works and what can be done using this library.

## How to use
 - Make sure that you have pip3 installed by running `pip3 --version`
 - Install dependencies by running
    - `pip3 install -r requirements.txt`

 - After installing the requirements run the project with:
    - `python3 main.py`
 - Your webcam will open and the app will be running.
 - To close just hit "q" on your keyboard.

 ## Webcam not working?
  - Maybe your webcam will not work, try changing the number at `main.py` `cv2.VideoCapture(x)` x can be -1, 0, 1.

 ## Weird issue not letting you start the application complaining about "GTK+ 2.x or Cocoa support...."?
  - First install libgtk2.0-dev and pkg-config
  - If the message keep showing up:
    - Verify if you have installed `opencv-python-headless`
    - If yes this is probably your problem, uninstall it using `pip3 uninstall opencv-python-headless`
    - This should solve the problem, run the project with `python3 main.py` and everything should work.
