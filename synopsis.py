#Defines the synopsis data structure that will represent each stream
#Two parts:
#1. Equiwidth Histogram, which in the paper, is 1 dimensional from PAA dimensionality reduction
#Will store 2 things: The frequency of data intervals as an integer, and then will also contain a Bloom Filter for each interval
#2. A Bloom Filter, which a probabilistic data structure to binarily check for the existence of values in a stream
