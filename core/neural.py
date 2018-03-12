import numpy as np


class NeuralNetwork(object):  
    def __init__(self, learning_rate=0.1):
        self.weights = np.random.normal(0.0, 2 ** -0.5, (1, 4))
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        self.learning_rate = np.array([learning_rate])

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def predict(self, inputs):
        inputs_1 = np.dot(self.weights, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        return outputs_1
    
    def train(self, inputs, expected_predict):
        inputs_1 = np.dot(self.weights, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)
        
        actual_predict = outputs_1[0]

        error_layer = np.array([actual_predict - expected_predict])
        gradient_layer = actual_predict * (1 - actual_predict)
        weights_delta_layer = error_layer * gradient_layer
        self.weights -= (np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer).T *
                         self.learning_rate)
