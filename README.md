# ML-Text-Recognition

This is part one of a bigger machine learning project I undertook. In this part, I train a convolutional neural network (CNN) to recognize printed text of any font in an image. 

sorting_characters.py is used to create a training and testing dataset from images of characters A to Z and numbers 1 to 9 in multiple fonts. It is then used to extract characters from a desired image.

neural_network_cnn.py uses the created training dataset to train a CNN for recognizing printed text.

NN-Extractor.py then uses sorting_characters.py to break up an image of a paragraph into individual characters, and then translates the text using the created CNN model. There are various metrics considered for accuracy including a propietary string_error.py method.

Other supervised learning methods such as SVM and ANN were also employed and tested but for the sake of simplicity, I only included the most promising method.
