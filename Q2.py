from typing import List
#import matplotlib.pyplot as plt

#This class will calculate the weighted average 
class WeightedAverage:
    #def __init__(self, w: List[float]): Contsructor method for the WeightedAveraage class, takes one parameter w, which is a list of floating-point numbers representing the weights for the weighted average.
    def __init__(self, w: List[float]):
        self.weights = w #assigns the provided list of weights w to the instance variable
        self.entries = [] #stores the weights which will be used later for calculations

#this process method takes the x as input and returns the weighted average as a float.
    def process(self, x: float) -> float:
        # Add the new entry to the list of recent entries...
        #By  inserting the new input x at the beginning (index 0) of the entries list.
        self.entries.insert(0, x)
        
        # Ensure the list doesn't grow beyond the number of weights
        if len(self.entries) > len(self.weights):
            self.entries.pop()  # Remove the oldest entry, ensuring that the list only contains as many entries as the list of weights.
        
        # Calculate the weighted sum
        #sum() calculates the total sum of these products, which is the weighted sum.
        #zip(self.weights, self.entries) combines the weights and entries lists element by element, creating pairs of corresponding weights and entries
        weighted_sum = sum(w * e for w, e in zip(self.weights, self.entries))
        
        # Calculate and return the weighted average
        return weighted_sum / len(self.weights)



weights = [ 1, 2, 3, 4, 5]# list weights containing five elements, representing the weights used in the weighted average.
signal = [1, 2, 3, 4, 5]#signal values that will be processed through the WeightedAverage class to compute the weighted averages.




#creating an instance of the WeightedAverage class,
wa = WeightedAverage(weights)

#loop that iterates over each value in the signal list
for x in signal:
    #computes the weighted average using the current values in entries and the fixed weights
    result = wa.process(x)
    print(f"Weighted average for input {x}: {result}")

#

#