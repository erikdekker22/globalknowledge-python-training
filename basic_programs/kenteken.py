import json, requests



def ask_kenteken():
    kenteken = input("Please specify a kenteken: ")
    url = 'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=' + kenteken # example 0001ES
    return url

def get_auto_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Something went wrong! ")

def search_data():
    search_value = input("Please specify what you want to search: [e.g. eerste_kleur, aantal_cilinders, merk]")
    return search_value

def main():
    url_kenteken = ask_kenteken()
    response = get_auto_data(url_kenteken)
    # print(json.dumps(response, indent=4, sort_keys=True))
    exact_value = search_data()
    print(response[0][exact_value])




if __name__ == "__main__":
    main()




