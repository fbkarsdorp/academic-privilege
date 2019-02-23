import os
import yaml


for question_file in os.scandir('questions'):
    if question_file.name.endswith('.yml'):
        with open(question_file.path) as f:
            data = yaml.load(f)

        for question in data:
            if question['id'] is None:
                raise ValueError(f'Missing ID in {question}')
            if question['question'] is None:
                raise ValueError(f'Missing question in {question}')
            if question['privileged answer'] is None:
                raise ValueError(f'Missing answer in {question}')
    
