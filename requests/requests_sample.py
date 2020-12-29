
import json
import requests

## Example kenteken: 93JGJB

def ask_kenteken(): # -->
    kenteken = input("Please specify the kenteken you want to research: ")
    return kenteken

def main(kenteken):
    '''
    Please give a kenteken as input.
    The output is more information about the specific car.
    '''
    url = 'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=' + kenteken
    response = requests.get(url)

    # test for success
    if response.status_code == 200:  # successfull response
        print(response.json)  # json string
        data = json.loads(response.text) # convert to python dict with loads. Loads converts it from a JSON string. Load converts JSON from a file.
        print('You asked for information about kenteken ' + data[0]["kenteken"])
        print('The color of this car is: ' + data[0]["eerste_kleur"])
        print('The maximum amout of persons that can be in this car are: ' + data[0]["aantal_zitplaatsen"])

        # for object in data:  # iterate through the JSON data object
        #     for key, value in object.items():
        #         print(key)
    else:
        print("Could not fetch data from", url)

main(ask_kenteken())
