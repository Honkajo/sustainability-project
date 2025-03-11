import numpy as np
import math

class NeuralNetwork:
    LEARNING_RATE = 0.5

    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        self.weights_ih = np.random.rand(num_inputs, num_hidden)
        self.weights_ho = np.random.rand(num_hidden, num_outputs)
        self.bias_hidden = np.zeros((1, num_hidden))
        self.bias_output = np.zeros((1, num_outputs))

    def feed_forward(self, inputs):
        hidden_layer_outputs = np.dot(inputs, self.weights_ih) + self.bias_hidden
        output_layer_outputs = np.dot(hidden_layer_outputs, self.weights_ho) + self.bias_output
        return output_layer_outputs

    def train(self, training_inputs, training_outputs):
        hidden_layer_outputs = self.feed_forward(training_inputs)
        output_layer_outputs = np.dot(hidden_layer_outputs, self.weights_ho) + self.bias_output
        errors = training_outputs - output_layer_outputs
        self.weights_ho += self.LEARNING_RATE * np.dot(hidden_layer_outputs.T, errors)
        self.bias_output += self.LEARNING_RATE * np.sum(errors, axis=0, keepdims=True)

    def calculate_total_error(self, training_sets):
        total_error = 0
        for training_inputs, training_outputs in training_sets:
            output_layer_outputs = self.feed_forward(training_inputs)
            errors = training_outputs - output_layer_outputs
            total_error += np.sum(errors ** 2)
        return total_error

# Beispiel-Verwendung:
nn = NeuralNetwork(2, 2, 2)
training_sets = [
    [[0, 0], [0]],
    [[0, 1], [1]],
    [[1, 0], [1]],
    [[1, 1], [0]]
]
for i in range(10000):
    training_inputs, training_outputs = random.choice(training_sets)
    nn.train(training_inputs, training_outputs)
    nn.calculate_total_error(training_sets)

