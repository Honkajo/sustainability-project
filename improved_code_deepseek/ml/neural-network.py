import numpy as np

class NeuralNetwork:
    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        # Initialize weights and biases with random values
        self.weights_ih = np.random.randn(num_hidden, num_inputs)
        self.weights_ho = np.random.randn(num_outputs, num_hidden)
        self.bias_h = np.random.randn(num_hidden, 1)
        self.bias_o = np.random.randn(num_outputs, 1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feed_forward(self, inputs):
        # Convert inputs to a column vector
        inputs = np.array(inputs, ndmin=2).T

        # Hidden layer
        hidden_inputs = np.dot(self.weights_ih, inputs) + self.bias_h
        hidden_outputs = self.sigmoid(hidden_inputs)

        # Output layer
        final_inputs = np.dot(self.weights_ho, hidden_outputs) + self.bias_o
        final_outputs = self.sigmoid(final_inputs)

        return final_outputs

    def train(self, inputs, targets):
        # Convert inputs and targets to column vectors
        inputs = np.array(inputs, ndmin=2).T
        targets = np.array(targets, ndmin=2).T

        # Feed forward
        hidden_inputs = np.dot(self.weights_ih, inputs) + self.bias_h
        hidden_outputs = self.sigmoid(hidden_inputs)
        final_inputs = np.dot(self.weights_ho, hidden_outputs) + self.bias_o
        final_outputs = self.sigmoid(final_inputs)

        # Output layer error
        output_errors = targets - final_outputs
        output_gradients = self.sigmoid_derivative(final_outputs)
        output_gradients *= output_errors
        output_gradients *= 0.1  # Learning rate

        # Hidden layer error
        hidden_errors = np.dot(self.weights_ho.T, output_gradients)
        hidden_gradients = self.sigmoid_derivative(hidden_outputs)
        hidden_gradients *= hidden_errors
        hidden_gradients *= 0.1  # Learning rate

        # Update weights and biases
        self.weights_ho += np.dot(output_gradients, hidden_outputs.T)
        self.weights_ih += np.dot(hidden_gradients, inputs.T)
        self.bias_o += output_gradients
        self.bias_h += hidden_gradients

# Example usage
nn = NeuralNetwork(2, 2, 2)
training_inputs = np.array([[0.05, 0.1], [0.1, 0.2], [0.2, 0.3], [0.3, 0.4]])
training_outputs = np.array([[0.01, 0.99], [0.02, 0.98], [0.03, 0.97], [0.04, 0.96]])

for i in range(10000):
    for j in range(len(training_inputs)):
        nn.train(training_inputs[j], training_outputs[j])
