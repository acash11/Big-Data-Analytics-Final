#Test main
#Used to test a brute force similarity join on a static set of random data
#Data is two sets of coordinate pairs, which follow a sine wave with random variation
#Will (hopefully) be compared to the ARES method implemented

import numpy as np
import time
import matplotlib.pyplot as plt

def similarity_join(set1, set2, threshold) -> list:
    """
    Perform a similarity join on two sets of 2D numerical data based on a threshold.

    Parameters:
    set1 (np.ndarray): First set of 2D points.
    set2 (np.ndarray): Second set of 2D points.
    threshold (float): The distance threshold for similarity.

    Returns:
    List of tuples: Each tuple contains a point from set1 and a point from set2 that are within the threshold distance.
    """
    similar_pairs = []

    for point1 in set1:
        for point2 in set2:
            distance = np.linalg.norm(point1 - point2)
            if distance <= threshold:
                similar_pairs.append((tuple(point1), tuple(point2)))

    return similar_pairs

def create_random_sine_data(noise_factor, points_generated):
    # Create 100 random X values from 0 to 6pi
    x_values = np.linspace(0, 6 * np.pi, points_generated)

    # Compute the corresponding y-values using the sine function
    y_values = np.sin(x_values)

    # Introduce some variation (e.g., a small random noise)
    y_values += np.random.uniform(-noise_factor, noise_factor, y_values.shape)

    #Return a numpy array of pairs
    return np.dstack((x_values, y_values))


if __name__ == '__main__':

    ########### TEST VALUES ###############

    #Threshold variable for testing
    threshold = 0.1

    #Amount of data points to be generated
    points_generated = 100

    #Noise factor for data
    noise_factor = 0.5

    #######################################

    ###FOR TESTING
    # test_static_series = [x for x in create_random_sine_data(1)]
    # print(test_static_series)
    # plt.scatter(*zip(*test_static_series))
    # plt.title('100 2D Points Following A Sine Wave, With Variation')
    # plt.show()
    ###

    #Creates 2 sets of random values to perform a similarity join on.
    #Values are 2D points
    #Index [0] is necessary to unpack the array surrounding the list of data
    set1 = [coord for coord in create_random_sine_data(noise_factor, points_generated)][0]
    set2 = [coord for coord in create_random_sine_data(noise_factor, points_generated)][0]

    #Start timer for evaluation
    start = time.time()

    #Perform function on static series
    result = similarity_join(set1, set2, threshold)
    #Print pairs; For testing
    print("Similar pairs:", result)

    #Stop timer
    end = time.time()
    print("Time taken to process: ", end - start)

    # Plotting the points and similar pairs
    plt.figure(figsize=(10, 8))

    # Plot set1
    plt.scatter(set1[:, 0], set1[:, 1], c='blue', label='Set 1')

    # Plot set2
    plt.scatter(set2[:, 0], set2[:, 1], c='red', label='Set 2')

    # Plot similar pairs
    for (point1, point2) in result:
        plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--')

    # Labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Similarity Join of 2D Points')
    plt.legend()
    plt.grid(True)
    plt.show()