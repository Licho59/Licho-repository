import numpy as np
from matplotlib import pyplot as plt


def plot_line(y_prediction, features, color):
    x_values = [i for i in range(
        int(min(features)) - 1, int(max(features)) + 1)]
    y_values = [y_prediction(x) for x in x_values]
    plt.plot(x_values, y_values, color)


def predicted_y(features, weight, bias):
    return np.dot(features, weight) + bias


def error_bias_calculation(features, targets, weight, bias):
    error = sum(predicted_y(features, weight, bias) - targets)
    return error / len(features)


def error_weight_calculation(features, targets, weight, bias):
    error = sum((predicted_y(features, weight, bias) - targets) * features)
    return error / len(features)


def update_weights(features, targets, weight, bias, alpha):
    error_bias = error_bias_calculation(features, targets, weight, bias)
    error_weight = error_weight_calculation(features, targets, weight, bias)
    weight = weight - alpha * error_weight
    bias = bias - alpha * error_bias
    return weight, bias


def cost_calculation(features, targets, weight, bias):
    sum_of_square_errors = sum(
        np.square(predicted_y(features, weight, bias) - targets))
    cost = sum_of_square_errors / (2 * len(features))
    return cost


def gradient_descent(features, targets, epochs, alpha):
    # Initialize random weight and random bias
    weight = 0
    bias = 0
    # Line at initial position (in blue)

    def y_prediction(x): return weight * x + bias
    plot_line(y_prediction, features, 'b')
    plt.plot(features, targets, 'bo')
    plt.show()

    for i in range(epochs):
        # Update weight and bias of the line
        weight, bias = update_weights(features, targets, weight, bias, alpha)
        # every 10 iteration, print Cost for each epoch
        # and a doted green line for the updated line
        if i % 10 == 0:
            plot_line(y_prediction, features, 'g--')
            print("\n========== Epoch", i, "==========")
            print("Cost: ", cost_calculation(features, targets, weight, bias))
    # draw the last line in red
    plot_line(y_prediction, features, 'r')
    plt.plot(features, targets, 'bo')
    plt.show()


# Create small dataset
features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
targets = [2, 4, 2, 4, 6, 6, 5, 8, 9, 8]
plt.plot(features, targets, 'bo')
plt.show()

gradient_descent(features, targets, epochs=100, alpha=0.001)
