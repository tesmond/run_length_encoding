# Run length encoding

Run length encoding is an algorithm for performing lossless data compression. Lossless data compression refers to compressing the data in such a way that the original form of the data can then be derived from it. When a character occurs a large number of times consecutively in a sequence, then we can represent the same consecutive subsequence using only a single occurrence of that character and its count. Using run length encoding, we can save memory space while transmitting data and preserving its original form. It is useful when we want to store or transmit large sequences of data.

For example if the sequence is : AACCCBBBBBAAAAFFFFFFFFZ

Then, using run length encoding, we can represent it as: A2C3B5A4F8Z

The 23 length sequence was compressed to a 11 length sequence.

The functions `encode` and `decode` in `main.py` use regex to parse the input strings in to the appropriate groups of characters and then output the respected encoded and decoded strings.

To run the tests install pytest `pip install pytest` and run `pytest test.py`