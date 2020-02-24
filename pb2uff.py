# Import TensorRT models
import tensorrt as trt
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)


model_file = 'model/blueA_VGG16.uff'

#with trt.Builder(TRT_LOGGER) as builder:
#    with builder.create_network() as network:
#        with trt.UffParser() as parser:
#            parser.register_input("dense/BiasAdd", (3, 224, 224))
#            parser.register_output("dense/Softmax")
#parser.parse(model_file, network)

builder = trt.Builder(TRT_LOGGER)
network = builder.create_network()
parser = trt.UffParser()
parser.register_input("vgg16_input", (3, 224, 224))
parser.register_output("dense/Softmax")
parser.parse(model_file, network)

