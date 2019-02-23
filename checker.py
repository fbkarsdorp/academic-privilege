import os
import yaml


for question_file in os.scandir('questions'):
    if question_file.name.endswith('.yml'):
        with open(question_file.path) as f:
            data = yaml.load(f)

        for question in data:
            if question['id'] is None:
                raise ValueError('Missing ID in {}'.format(question))
            if question['question'] is None:
                raise ValueError('Missing question in {}'.format(question))
            if question['privileged answer'] is None:
                raise ValueError('Missing answer in {}'.format(question))
    
