import numpy as np

def create_random_sine_data(noise_factor, points_generated):
    # Create 100 random X values from 0 to 6pi
    x_values = np.linspace(0, 6 * np.pi, points_generated)

    # Compute the corresponding y-values using the sine function
    y_values = np.sin(x_values)

    # Introduce some variation (e.g., a small random noise)
    y_values += np.random.uniform(-noise_factor, noise_factor, y_values.shape)

    #Return a numpy array of pairs
    return np.dstack((x_values, y_values))