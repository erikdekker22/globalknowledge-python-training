
import json
import requests

## Example kenteken: 93JGJB
def construct_url():
    kenteken = input("Please specify the kenteken you want to research: ")
    url = 'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=' + kenteken
    return url

def http_get(url):
    response = requests.get(url)
    return response

def main():
    '''
    Please give a kenteken as input.
    The output is more information about the specific car.
    '''
    url = construct_url()
    response = http_get(url)

    if response.status_code == 200:  # successful response
        print("HTTP status code is: " + str(response.status_code))  # json string
        print("The Content-Type of the HTTP response was: " + str(response.headers['Content-Type']))

        data = json.loads(response.text)  # convert to python dict with loads.
        print('You asked for information about kenteken ' + data[0]["kenteken"])
        print('The color of this car is: ' + data[0]["eerste_kleur"])
        print('The maximum amout of persons that can be in this car are: ' + data[0]["aantal_zitplaatsen"])
    else:
        print("Could not fetch data from", url)

main()
