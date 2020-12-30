'''
This library consume the classifier model.
We load the model from file, then we make predictions.

references:
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/06_structured/3_keras_dnn.ipynb

'''
from baby_weight import settings
from os import path
import tensorflow as tf
from tensorflow.keras.models import load_model

#model_h5_path = path.join( settings.STATICFILES_DIRS, 'predict', 'baby.h5' )
model_h5_path = 'C:/Users/artur/git/baby_weight_tf/baby_weight/static/predict/baby.h5'
print( 'model_h5_path: {}'.format( model_h5_path ) )
h5_model = load_model( model_h5_path )

def get_weight( j_input ):
    try:
        tf_dic        = {name: tf.convert_to_tensor([value]) for name, value in j_input.items()}
        predictions   = h5_model.predict( tf_dic )
        weight_pounds = predictions[0][0]
        weight_kilos  = weight_pounds * 0.45359237

        result        = {
                            'weight_pounds' : predictions[0][0],
                            'weight_kilos'  : weight_pounds * 0.45359237
                        }

        return result

    except Exception as e:
        print( 'predict.api_baby.get_weight(), error:  {}'.format( e ) )
        raise