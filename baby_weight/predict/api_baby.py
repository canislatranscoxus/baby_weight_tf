'''

references:
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/06_structured/3_keras_dnn.ipynb

'''
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

credentials  = GoogleCredentials.get_application_default()
api          = discovery.build('ml', 'v1', credentials=credentials)
project      = PROJECT
model_name   = 'babyweight'
version_name = 'dnn'

def get_weight( input_data ):

    parent      = 'projects/%s/models/%s/versions/%s' % (project, model_name, version_name)
    prediction  = api.projects().predict(body=input_data, name=parent).execute()
    print(prediction)
    print(prediction['predictions'][0]['babyweight'][0])

    weight_pounds = prediction['predictions'][0]['babyweight'][0]
    weight_kilos  = weight_pounds / 2.2046

    result = {
        'weight_pounds' : weight_kilos,
        'weight_kilos'  : weight_pounds
    }
    return result