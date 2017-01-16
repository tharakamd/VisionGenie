from ImageProcessors.BinacularVisionImageProcessor import BinacularVisionImageProcessor
from Cameras.PiCam import PiCam
from PreProcessors.GBRtoGRAYpreProcessor import  GBRtoGRAYpreProcessor
from PipeLine import PipeLine


class Core:

    # creating instances
    pre = GBRtoGRAYpreProcessor()
    cam = PiCam()
    imagePro = BinacularVisionImageProcessor()
    pipeline = PipeLine()

    # creating and executing pipeline
    pipeline.addCamera(cam)
    pipeline.addPreProcessor(pre)
    pipeline.addImageProcessor(imagePro)
    pipeline.executePipeLine()


