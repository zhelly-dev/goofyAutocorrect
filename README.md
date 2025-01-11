# An Autocorrect
This project is an implementation of a simple autocorrect feature using a text corpus. The provided Python code reads a text file, builds a vocabulary, and then uses [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) to suggest the most probable corrections for <ins>**misspeled**</ins> words.

## How it works
The autocorrect algorithm works as follows:
  1. **Read the text file**: The script reads a text file ('alice_in_wonderland.txt' by default) and extracts words to build a vocabulary.
  2. **Build vocabulary and word frequencies**: The Script constructs a set of unique words (vocabulary) and calculates the frequency of each word.
  3. **Calculate probabilities**: Each word's probability is computed based on its frequency in the text.
  4. **Compute similarities**: For an input word, Jaccard similarity is calculated between the input word and each word in the vocabulary.
  5. **Generate suggestions**: The script sorts the words by similarity and probability to suggest the most probable corrections.

## Dependencies
* pandas
* numpy
* textdistance

## Usage
1. Ensure you have a text file to build the vocabulary. By default, the code uses 'books/alice_in_wonderland.txt'.
2. Run the Python script: `python main.py`
3. Enter a word when prompted to see the autocorrect suggestions.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a PR (pull request)
