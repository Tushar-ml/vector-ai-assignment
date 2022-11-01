import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.utils.np_utils import to_categorical


class Preprocess_Image:
    """
    This Class will be Preprocessing Feature based on differnt Different Models and Differnt Methods for custom image 

    training

    Attributes:
    -----------
            num_classes --> 2(Default) Number of Classes or Number of Objects to Process 
            batch_size --> 32 (default)
            target_image_size --> (224,224,3) (default)

    Methods:
    --------
           Get_Images_from_Directory --> Taking Images from Data Directory
           Get_Data_from_Array                --> Taking values x_train,y_train

    """

    def __init__(self, num_classes=2, batch_size=32, target_image_size=(224, 224, 3)):

        if num_classes == 2:
            # Creating Class Mode for Image Data Processing
            self.class_mode = 'binary'
        else:
            self.class_mode = 'categorical'
        self.batch_size = batch_size
        self.target_image_size = target_image_size

    def Get_Images_from_Directory(self, training_images_directory=None, validation_images_directory=None, test_image_directory=None, training=True):
        """
        This Function will Take images from image Directory and convert them to desired

        shape and Configurations.

        Arguments:

            training_images_directory --> Directory Containing Images from Training Folder for Preprocessing

            Validation_images_directory --> None (Defalult)--No Validation will be occur.

            batch_size --> Batch Size for Data Generator

            target_image_size --> Contains Target Size for conversion of Model including 3 channel

        Output:

            Training_Data_Generator,Validation_data_Generator

        """

        target_image_size = self.target_image_size
        if len(target_image_size) != 3:
            raise ValueError(
                'Required 3 Arguments --- {} are given'.format(len(target_image_size)))

        # Data Generator Function for preprocessing Function
        data_generator = ImageDataGenerator(rescale=1./255,
                                            shear_range=0.2,
                                            zoom_range=0.2,
                                            horizontal_flip=True)

        if training:
            if training_images_directory is None:
                raise ValueError(
                    'For Training Image Directory is Must, or put training mode to False and use test_image_directory')
            # Train Data Generator for Training
            train_data_generator = data_generator.flow_from_directory(directory=training_images_directory,
                                                                      target_size=(
                                                                          target_image_size[0], target_image_size[1]),
                                                                      batch_size=self.batch_size,
                                                                      class_mode=self.class_mode,
                                                                      color_mode='grayscale' if target_image_size[2] == 1 else 'rgb')
            # Checking Validation Data Directory , If exists return train and validation data generator
            if validation_images_directory is not None:
                validation_data_generator = data_generator.flow_from_directory(directory=validation_images_directory,
                                                                               target_size=(
                                                                                   target_image_size[0], target_image_size[1]),
                                                                               class_mode=self.class_mode,
                                                                               color_mode='grayscale' if target_image_size[2] == 1 else 'rgb')
                return train_data_generator, validation_data_generator

            else:
                return train_data_generator, None
        else:
            if test_image_directory is None:
                raise ValueError(
                    'Test Image Directory Required for Prediction')
            # Data Generator Function for preprocessing Function
            data_generator = ImageDataGenerator(
                rescale=1./255)
            test_data_generator = data_generator.flow_from_directory(directory=test_image_directory,
                                                                     target_size=target_image_size,
                                                                     shuffle=False,
                                                                     batch_size=1,
                                                                     color_mode='grayscale' if target_image_size[
                                                                         2] == 1 else 'rgb'
                                                                     )
            return test_data_generator

    def Get_Data_from_Array(self, x_train=None, y_train=None, x_test=None, y_test=None, train=True):
        """
        This Function will take value from arrays containing Data and Labels

        Arguments:
            x_training --> Containg Image Data in form of arrays
            y --> Containg Labels for Image Data

        Output:
            Train Data generator , Validation Data Generator

        """

        # Data Generator Function for preprocessing Function
        data_generator = ImageDataGenerator(rescale=1./255)
        if len(x_train.shape) == 3:
            x_train = np.expand_dims(x_train, axis=-1)
            x_test = np.expand_dims(x_test, axis=-1)

        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        if train:
            # Train Data Generator for x_train,y_train
            if y_train is None:
                raise ValueError('For Training, Classes are required')
            train_data_generator = data_generator.flow(x=x_train,
                                                       y=y_train,

                                                       batch_size=self.batch_size)
            validation_data_generator = data_generator.flow(x=x_test,
                                                            y=y_test,

                                                            batch_size=self.batch_size)
            return train_data_generator, validation_data_generator

        else:
            test_data_generator = data_generator.flow(x=x_test,
                                                      y=y_test
                                                      )

            return test_data_generator
