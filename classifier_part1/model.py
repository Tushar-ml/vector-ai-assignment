from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, MaxPooling2D, Conv2D
import numpy as np


def generate_model(target_size, classes):
    nclass = 1 if classes == 2 else classes
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu',
              input_shape=tuple(target_size)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100))
    model.add(Dense(nclass, activation='softmax' if nclass >= 2 else 'sigmoid'))
    # compile model
    loss = 'categorical_crossentropy' if classes > 2 else 'binary_crossentropy'
    model.compile(optimizer='adam', loss=loss, metrics=['accuracy'])
    return model


def predict_model(model, data, n_class):

    ypred = model.predict(data)
    threshold = 0.5
    ypred = np.where(ypred > threshold, 1,
                     0) if n_class == 2 else np.argmax(ypred, axis=1)

    return ypred
