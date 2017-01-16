from AbstractPipeLine import AbstractPipeLine

class PipeLine(AbstractPipeLine):

    preProcessorList = list()
    imageProcessorList = []
    outputGeneratorList = []
    camera = None

    def initPipeLine(self):
        global preProcessorList
        global imageProcessorList
        global outputGeneratorList
        preProcessorList = []
        imageProcessorList = []
        outputGeneratorList = []

    def addPreProcessor(self,preprocessor):
        global preProcessorList
        self.preProcessorList.append(preprocessor)

    def addImageProcessor(self,imageProcessor):
        global imageProcessorList
        self.imageProcessorList.append(imageProcessor)

    def addOutputGeneratorList(self,outputGenerator):
        global outputGeneratorList
        outputGeneratorList.append(outputGenerator)

    def addCamera(self,cam):
        global camera
        camera = cam

    def executePipeLine(self):
        global preProcessorList
        global imageProcessorList
        global camera
        for preProcessor in self.preProcessorList:
            camera.register(preProcessor)
            for imageProcessor in self.imageProcessorList:
                preProcessor.register(imageProcessor)
        camera.start()

