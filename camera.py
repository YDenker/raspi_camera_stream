from picamera import PiCamera
from time import sleep
import io

class VideoCamera(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24

    def get_frame(self):
        frame = io.BytesIO()
        self.camera.capture(frame, 'jpeg', use_video_port=True)
        return frame.getvalue()
