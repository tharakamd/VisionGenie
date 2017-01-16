from BinacularVisionImageProcessor import BinacularVisionImageProcessor
from Cameras.WebCamera import WebCamera

from ImageProcessors.EdgeMatchObjectDetector import EdgeMatchObjectDetector
from PipeLine import PipeLine


class Core:

    pre = EdgeMatchObjectDetector()
    cam = WebCamera()
    imagePro = BinacularVisionImageProcessor()
    pipeline = PipeLine()
    pipeline.addCamera(cam)
    pipeline.addPreProcessor(pre)
    pipeline.addImageProcessor(imagePro)
    pipeline.executePipeLine()


