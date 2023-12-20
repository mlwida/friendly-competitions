import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-6, 6, 100)

def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_deriative(x):
    return sigmoid(x)*(1-sigmoid(x))


plt.figure()  # create a plot figure



# create the first of two panels and set current axis
plt.subplot(2, 1, 1)  # (rows, columns, panel number)
plt.plot(x_data,sigmoid(x_data))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x_data, sigmoid_deriative(x_data))