import time
from sorting_character import Extract_Letters
from keras.models import load_model, model_from_json
import numpy as np
from PIL import Image
import keras
import tensorflow as tf
import difflib
import os
from String_error import hamming_distance, string_letter_error

os.chdir("/Users/aerrowfar/Desktop/WritingRecognition")

with open('./test_files/shazam_test.txt', 'r') as file:
    data = file.read().replace('\n', '')
t=0
cleaned_text = ''.join(e for e in data if e.isalnum())

start_time = time.time()

#specify the image source to be extracted:
training_file = './test_files/shazam.png'
model = tf.keras.models.load_model('cnn_model_computer_chars.h5')

#defining class object for extractor
extract = Extract_Letters()

#this gives us an array of the chars images extracted 
characters = extract.extractFile(training_file)

#define preditc function
def predict(model=None, image=None, correct_label=None):
    class_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    image = np.expand_dims(image, axis=2)
    prediction = model.predict(np.array([image]))
    predicted_class = class_names[np.argmax(prediction)]
    if correct_label == None:
        return predicted_class
    else:
        show_image(image, class_names[correct_label], predicted_class)

#looping through array of char images:

text_output= ''
for i in characters:

    j= (predict(model=model,image=i))
    text_output+= j 
  


accuracy_model = difflib.SequenceMatcher(None, text_output, cleaned_text).ratio()
string_distance = hamming_distance(text_output,cleaned_text)
string_letter_error_value = string_letter_error(text_output, cleaned_text)

print (text_output)
#print (cleaned_text)  #For comparison if necessary
print (time.time() - start_time, "seconds" )
print("clean text length is :", len(cleaned_text))
print("predicted text length is :", len(text_output))
print ('Accuracy is:', accuracy_model)
print ('Hamming distance is:', string_distance)
print ('String Letter Error is:', str(string_letter_error_value))