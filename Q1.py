#Importing from libraries
from collections import defaultdict
from heapq import nlargest
from typing import List, Tuple

class WordFrequencyAnalyzer:
    # constructor method of the class. It gets called when a new instance of WordFrequencyAnalyzer is created.
    # n: int = 10 this will control how many top frequent words we want to retrieve.
    def __init__(self, n: int = 10):
       #Initialize with default n value (10) for top n words.
        # topfrequentwords is set to the value of n, which is the number of top frequent words to retrieve later.
        self.topfrequentwords = n
        #if a word is not found in the dictionary, it will be automatically initialized to 0.
        self.word_frequency = defaultdict(int)
        #the dictionary will store words as keys and their respective frequencies as values.

    #This method processes a word by updating its frequency count in the word_frequency dictionary.
    def process_word(self, word: str): 
        if word:  # Make sure word is not empty
            #This increments the frequency count of the word by 1 in the word_frequency dictionary. If the word is encountered for the first time,...
            #it is automatically initialized to 0 and then incremented to 1.
            self.word_frequency[word] += 1

            #retrieves the top n most frequent words from the word_frequency dictionary
            #return type is a list of tuples, where each tuple consists of a string (the word) and an integer (its frequency).
    def get_top_words(self) -> List[Tuple[str, int]]:
        #Use nlargest to get top n items sorted by frequency in descending order
        #self.word_frequency.items() returns the dictionary's items as a list of tuples ((word, frequency)).
        # key=lambda item: item[1] tells nlargest to sort by the second element of each tuple, the frequency of the word is in descending order...
        #so that the most frequent word are visible at the top of the list
        return nlargest(self.topfrequentwords, self.word_frequency.items(), key=lambda item: item[1])


# responsible for processing a given text.
def analyze_text(text: str, analyzer: WordFrequencyAnalyzer):
    #  process each word in the text array
    for word in text:
        #word.lower() converts the word to lowercase to ensure case-insensitivity.
        #word.strip(".,!?;") removes any common punctuation marks from the beginning and end of the word to clean it before processing.
        cleaned_word = word.lower().strip(".,!?;")  # Clean word of punctuation
        analyzer.process_word(cleaned_word)  #The cleaned word is passed to the process_word method of the analyzer object to update its frequency count.

# Usage Example
if __name__ == "__main__":
    # Sample text array containing multiple words, some of which repeat
    text = ["geeks","for","geeks","a","portal", "to","learn","can","be","computer","science","yup","fire","in","be","data","geeks"]

    # Create an analyzer with default topfrequentwords = 10
    analyzer = WordFrequencyAnalyzer()

    #processes the input text and updates the word frequencies in the analyzer object.
    analyze_text(text, analyzer)

    # Retrieve and print the top words
    top_words = analyzer.get_top_words()
    print("Top words:")
   #loop iterates over the top n most frequent words and their frequencies.
    for word, freq in top_words:
        #prints each word and its frequency
        print(f"{word}: {freq}")
