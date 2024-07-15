import create_data
import time
import numpy as np
import matplotlib.pyplot as plt
import math

import bplustree

def fill_bplustree(bptree, keys, values):
    assert len(keys) == len(values)

    for i in range(0, len(keys)):
        bptree.insert(keys[i], values[i])
    return

def index_similarity_join(qset, bptrees, threshold, sw_size):
    assert len(bptrees) > 0

    answer = []

    candidate_offsets = []
    for bptree in bptrees:
        #Get first point in qset
        qset_index = 0
        for point in qset:
            #print(point)
            in_range = bptree.range_query(point[0] - threshold, point[0] + threshold)
            #print(in_range)
            for p in in_range:
                #print("p", p, "point", point)
                if math.dist(p, point) <= threshold:
                    candidate_offsets.append(p)
            #print(candidate_offsets, len(candidate_offsets))
            
            for c in candidate_offsets:
                #print(c)
                node = bptree.find(c[0])
                #print("keys", node.keys)
                offset = node.keys.index(c[0])
                #print(offset)
                sw = []
                for i in range(0, sw_size):
                    if offset < len(node.keys):
                        x = node.keys[offset]
                        y = node.values[offset]
                        sw.append((x, y))
                        offset += 1
                    else:
                        if node.next == None: return answer
                        node = node.next
                        offset = 0
                        x = node.keys[offset]
                        y = node.values[offset]
                        sw.append((x, y))
                        offset += 1
                #print(sw)
                qset_sw = qset[qset_index: qset_index + sw_size]

                distance = np.sqrt(np.sum((sw - qset_sw) ** 2))
                if distance <= threshold:
                    
                    answer.append((tuple(sw), tuple(qset_sw)))
                
            
            qset_index += 1
            
    return answer

            
        #Perform a range search on that point to see if its elibigle for sliding window
        #If yes, incrementally test sequence. If sum of sequence is less than theshold, add it to answer
        #If no, move on to the next point in qset, until you reach pass point len(qset)-sw_size

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


    set2Keys = set2[:, 0]
    set2Values = set2[:, 1]
    bplustree = bplustree.BPlusTree()
    
    fill_bplustree(bplustree, set2Keys, set2Values)

    #bplustree.show()

    #bplustree.range_query(start, end)

    #Start timer for evaluation
    start = time.time()

    #Perform function on static series
    result = index_similarity_join(set1, [bplustree], threshold, sw_size)  


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