import json
import boto3


def lambda_handler(event, context):
    # Extract necessary information from the event
    session_attributes = event['session']['attributes']
    dialog_state = event['sessionState']['dialogAction']['type']
    
    # Handle different dialog states
    if dialog_state == 'ElicitSlot':
        return elicit_slot_handler(session_attributes, event['sessionState']['dialogAction'])
    elif dialog_state == 'ElicitIntent':
        return elicit_intent_handler(session_attributes, event['sessionState']['dialogAction'])
    else:
        return handle_unknown_dialog_state()

def elicit_slot_handler(session_attributes, dialog_action):
    # Extract necessary information from the dialog action
    slot_to_elicit = dialog_action['slotToElicit']
    
    # Your logic for handling elicit slot
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "ElicitSlot",
                "slotToElicit": slot_to_elicit,
                "intentName": dialog_action['intentName'],
                "message": {
                    "contentType": "PlainText",
                    "content": f"What is your {slot_to_elicit}?"
                }
            }
        }
    }
    return response

def elicit_intent_handler(session_attributes, dialog_action):
    # Your logic for handling elicit intent
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": "I'm not sure what you're asking. Can you please provide more information?"
                }
            }
        }
    }
    return response

def handle_unknown_dialog_state():
    # Your logic for handling unknown dialog states
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Failed",
                "message": {
                    "contentType": "PlainText",
                    "content": "I'm sorry, there was an issue processing your request."
                }
            }
        }
    }
    return response