from AbstractPipeLine import AbstractPipeLine

class PipeLine(AbstractPipeLine):

    preProcessorList = []
    imageProcessorList = []
    outputGeneratorList = []

    def initPipeLine(self):
        global preProcessorList
        global imageProcessorList
        global outputGeneratorList
        preProcessorList = []
        imageProcessorList = []
        outputGeneratorList = []

    def addPreProcessor(self,preprocessor):
        global preProcessorList
        preProcessorList.append(preprocessor)

    def addImageProcessor(self,imageProcessor):
        global imageProcessorList
        imageProcessorList.append(imageProcessor)

    def addOutputGeneratorList(self,outputGenerator):
        global outputGeneratorList
        outputGeneratorList.append(outputGenerator)

    def executePipeLine(self):
        return

