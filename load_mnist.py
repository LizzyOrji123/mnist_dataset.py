from tensorflow.keras.datasets import mnist

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Check the shape of the data
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)
