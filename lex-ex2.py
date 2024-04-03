import json

def lambda_handler(event, context):
    # Extract necessary information from the event
    intent_name = event['request']['intent']['name']
    session_attributes = event['session']['attributes']
    slots = event['request']['intent']['slots']
    
    # Handle different intents
    if intent_name == 'GreetIntent':
        return greet_intent_handler(session_attributes, slots)
    elif intent_name == 'BookFlightIntent':
        return book_flight_intent_handler(session_attributes, slots)
    else:
        return handle_unknown_intent()

def greet_intent_handler(session_attributes, slots):
    # Your logic for handling the greet intent
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Hello! How can I assist you today?"
                }
            }
        }
    }
    return response

def book_flight_intent_handler(session_attributes, slots):
    # Your logic for booking a flight
    # Example: Get slot values
    departure_city = slots['DepartureCity']['value']
    destination_city = slots['DestinationCity']['value']
    # Example: Book the flight using departure and destination cities
    
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": f"I have booked a flight from {departure_city} to {destination_city}."
                }
            }
        }
    }
    return response

def handle_unknown_intent():
    # Your logic for handling unknown intents
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": "I'm sorry, I didn't understand that. Can you please provide more information?"
                }
            }
        }
    }
    return response