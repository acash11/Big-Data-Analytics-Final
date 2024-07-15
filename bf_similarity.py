import numpy as np
import matplotlib.pyplot as plt
import time
import create_data

def bf_similarity_join(query_set, sets, threshold, sliding_win_size) -> list:

    #Get all subsequences of the query set
    q_subsequences = sliding_window(query_set, sliding_win_size)
    
    #Will hold all the subset answers to the query
    answer = []

    for set in sets:
        #Make sure the window fits in the set
        assert sliding_win_size <= len(set)

        subsequences = sliding_window(set, sliding_win_size)

        for points1 in q_subsequences:
            for points2 in subsequences:
                distance = np.sqrt(np.sum((points1 - points2) ** 2))
                if distance <= threshold:
                    answer.append((tuple(points1), tuple(points2)))

    return answer

#Returns a list of sub-sequences from moving a sliding window across a sequence
def sliding_window(sequence, sw_size) -> list:
    if sw_size > len(sequence): return []

    result = []
    start = 0
    end = sw_size

    while end != len(sequence) + 1:
        sw = sequence[start:end]
        
        result.append(sw)
        start += 1
        end += 1

    return np.array(result)


if __name__ == '__main__':

    ########### TEST VALUES ###############

    #Threshold variable for testing
    threshold = 0.5

    #Amount of data points to be generated
    points_generated = 200

    #Noise factor for data
    noise_factor = 0.5

    #Sliding Window size
    sw_size = 9

    #######################################

    #Creates 2 sets of random values to perform a similarity join on.
    #Values are 2D points
    #Index [0] is necessary to unpack the array surrounding the list of data
    set1 = [coord for coord in create_data.create_random_sine_data(noise_factor, points_generated)][0]
    set2 = [coord for coord in create_data.create_random_sine_data(noise_factor, points_generated)][0]

    #Start timer for evaluation
    start = time.time()

    #Perform function on static series
    result = bf_similarity_join(set1, [set2], threshold, sw_size)
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
    for pair in result:
        #print("pair: ", pair)
        i = 0
        for subseq in pair:
            if i == 0: col = 'green'
            else: col = "pink"
            for p in subseq:
                #print(f"{col} point:", p)
                plt.scatter(p[0], p[1], c=col)
            i = 1

    # Labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Similarity Join of 2D Points')
    plt.legend()
    plt.grid(True)
    plt.show()

