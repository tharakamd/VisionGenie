from PipeLine import PipeLine
from WebCamera import WebCamera
from EdgeMatchObjectDetector import EdgeMatchObjectDetector

class Core:

    pre = EdgeMatchObjectDetector()
    cam = WebCamera()
    pipeline = PipeLine()
    pipeline.addCamera(cam)
    pipeline.addPreProcessor(pre)
    pipeline.executePipeLine()


