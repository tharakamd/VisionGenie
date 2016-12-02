from PipeLine import PipeLine
from WebCamera import WebCamera
from EdgeMatchObjectDetector import EdgeMatchObjectDetector
from BinacularVisionImageProcessor import BinacularVisionImageProcessor

class Core:

    pre = EdgeMatchObjectDetector()
    cam = WebCamera()
    imagePro = BinacularVisionImageProcessor()
    pipeline = PipeLine()
    pipeline.addCamera(cam)
    pipeline.addPreProcessor(pre)
    pipeline.addImageProcessor(imagePro)
    pipeline.executePipeLine()


