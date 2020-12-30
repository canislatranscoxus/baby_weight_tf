'''
This library consume the classifier model from the static folder.
We load the model from file, then we make predictions.
This is just a demo to test a tensorflow model.

For production environment, we must deploy the model to cloud exposing an api url and
have another script that consume the model using that url.



references:
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/06_structured/3_keras_dnn.ipynb

'''
from baby_weight import settings
from os import path
import tensorflow as tf
from tensorflow.keras.models import load_model

model_h5_path = path.join(settings.STATICFILES_DIRS[0], 'predict', 'baby.h5')
h5_model      = load_model( model_h5_path )

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