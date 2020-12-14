import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

train_letters = '/Users/aerrowfar/Desktop/WritingRecognition/training_type'

#create tensor images with data augumentation.
train_datagen = ImageDataGenerator(
    #RGB 0 to 255, so multiply by 1/255 to process between 0 and 1.
    rescale=1./255,
)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_letters,
    color_mode="grayscale",
    #size for letters and numbers image cutouts
    target_size=(20, 20),
    batch_size=6000,
    #return 1D numpy array of integer labels
    class_mode="sparse",
)

#variables such as kenel_size, actiatio
def create_model():
    model = Sequential()
    #kernel size is 3 because RGB has 3 dimensions
    #ReLU speeds up training, all negative values are set to 0.
    model.add(Conv2D(64, kernel_size=3,
                     activation="relu", input_shape=(20, 20, 1)))
    model.add(Conv2D(32, kernel_size=3, activation="relu"))
    model.add(Flatten())
    #softmax normalizes outputs between 0 and 1.
    model.add(Dense(35, activation="softmax"))

    return model


model = create_model()
#variables here, including number of epochs have to be optimized experimentally.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(
    train_generator,
    epochs=40,
)

model.save('cnn_model_computer_chars.h5')

def predict(model=None, image=None, correct_label=None):
    class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    prediction = model.predict(np.array([image]))
    predicted_class = class_names[np.argmax(prediction)]
    if correct_label == None:
        return predicted_class
    else:
        show_image(image, class_names[correct_label], predicted_class)

def show_image(img, label='None', guess='None'):
    plt.figure()
    plt.imshow(img, cmap=plt.cm.binary)
    print("Expected:" + label)
    print("Guessed:" + guess)
    plt.tight_layout()
    plt.show()

def get_number():
    while True:
        num = input("pick number:")
        if num.isdigit():
            num = int(num)
            if 0 <= num <= 1000:
                return int(num)
        else:
            print("Bad input")


