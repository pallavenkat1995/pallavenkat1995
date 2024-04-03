import json

def lambda_handler(event, context):
    intent_name = event['request']['intent']['name']
    dialog_state = event['sessionState']['dialogAction']['type']
    session_attributes = event['session']['attributes']

    if dialog_state == 'ElicitIntent':
        return elicit_intent_response(session_attributes)
    elif dialog_state == 'ElicitSlot':
        return elicit_slot_response(session_attributes, event['sessionState']['dialogAction'])
    else:
        if intent_name == 'GreetIntent':
            return greet_intent_handler(session_attributes)
        elif intent_name == 'BookFlightIntent':
            return book_flight_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'CancelFlightIntent':
            return cancel_flight_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'CheckFlightStatusIntent':
            return check_flight_status_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'GetWeatherIntent':
            return get_weather_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'OrderPizzaIntent':
            return order_pizza_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'BookHotelIntent':
            return book_hotel_intent_handler(session_attributes, event['request']['intent']['slots'])
        elif intent_name == 'CheckMovieTimesIntent':
            return check_movie_times_intent_handler(session_attributes, event['request']['intent']['slots'])
        # Add more intent handlers as needed
        else:
            return handle_unknown_intent()

def elicit_intent_response(session_attributes):
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": "I'm sorry, I didn't understand. Can you please provide more information?"
                }
            }
        }
    }
    return response

def elicit_slot_response(session_attributes, dialog_action):
    slot_to_elicit = dialog_action['slotToElicit']
    intent_name = dialog_action['intentName']

    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "ElicitSlot",
                "slotToElicit": slot_to_elicit,
                "intentName": intent_name,
                "message": {
                    "contentType": "PlainText",
                    "content": f"What is your {slot_to_elicit}?"
                }
            }
        }
    }
    return response

def greet_intent_handler(session_attributes):
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
    departure_city = slots['DepartureCity']['value']
    destination_city = slots['DestinationCity']['value']

    # Your logic for booking a flight goes here

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

def cancel_flight_intent_handler(session_attributes, slots):
    # Your logic for canceling a flight goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Your flight has been canceled successfully."
                }
            }
        }
    }
    return response

def check_flight_status_intent_handler(session_attributes, slots):
    # Your logic for checking flight status goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Your flight is on time."
                }
            }
        }
    }
    return response

def get_weather_intent_handler(session_attributes, slots):
    # Your logic for getting weather information goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "The weather in your area is sunny with a high of 75°F."
                }
            }
        }
    }
    return response

def order_pizza_intent_handler(session_attributes, slots):
    # Your logic for ordering pizza goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Your pizza has been ordered successfully."
                }
            }
        }
    }
    return response

def book_hotel_intent_handler(session_attributes, slots):
    # Your logic for booking a hotel goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Your hotel has been booked successfully."
                }
            }
        }
    }
    return response

def check_movie_times_intent_handler(session_attributes, slots):
    # Your logic for checking movie times goes here
    response = {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "The movie times are as follows..."
                }
            }
        }
    }
    return response

def handle_unknown_intent():
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "ElicitIntent",
                "message": {
                    "contentType": "PlainText",
                    "content": "I'm sorry, I didn't understand. Can you please provide more information?"
                }
            }
        }
    }
    return response