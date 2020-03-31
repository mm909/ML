from dataGen import *
import tracemalloc

file = 'sample.txt'
file = 'D:/Predictive-Text/data/trump/speeches/clean/cleanSpeech.txt'
tracemalloc.start()
generator = DataGenerator(file)

for value in range(10000):
    X, y = generator.__getitem__()
    pass


current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
