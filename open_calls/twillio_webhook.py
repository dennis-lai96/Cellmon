import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger

import random
import json

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def handle_request():
    logger.debug(request.form)

    message = g.sms_client.messages.create(
                     body="Enter the world of Cellmon? (Y/N)",
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

    sent_input = str(request.form['Body']).lower()

    if sent_input == 'y':
        response = "This would start the game."
    elif sent_input == 'n':
        response = "This would quit the server."
    else:
        response = "Invalid Input."

    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    return json_response( status = "ok" )
