import os
import yaml


for question_file in os.scandir('questions'):
    if question_file.name.endswith('.yml'):
        with open(question_file.path) as f:
            data = yaml.safe_load(f)

        for question in data:
            if question['id'] is None:
                raise ValueError('Missing ID in {}'.format(question))
            if question['question'] is None:
                raise ValueError('Missing question in {}'.format(question))
            if question['answer'] is None and question['answer'] not in (True, False):
                raise ValueError('Missing answer in {}'.format(question))
            if question['active'] is None:
                raise ValueError('Missing answer in {}'.format(question))
            if question['weight'] is None:
                raise ValueError('Missing answer in {}'.format(question))
    
