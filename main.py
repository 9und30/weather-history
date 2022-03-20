import requests, json
import datetime, time
import matplotlib.pyplot as plt

# api daten
API_KEY = 'xxx' # eigenen api key von openweathermap eingeben :)
RESPONSE_FORMAT = 'json'
UNITS = 'metric'

# geo daten (z.Z. eingetragen FFM)
LAT = 50.110924
LON = 8.682127


def main():

    prev_times = []
    ago = [0, 0, 0, 0, 0]

    today = datetime.date.today()

    for i in range(5):
        prev_time = today - datetime.timedelta(5-i)
        prev_times.append(prev_time.strftime('%d.%m'))

    # die letzten 5 tage unix setzen
    for i in range(len(ago)):
        day = today - datetime.timedelta(i)
        day_unix = time.mktime(day.timetuple())
        ago[i] = int(day_unix)

  
    # api calls
    response_prev_1 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LAT}&lon={LON}&dt={ago[0]}&appid={API_KEY}&mode={RESPONSE_FORMAT}&units={UNITS}')

    response_prev_2 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LAT}&lon={LON}&dt={ago[1]}&appid={API_KEY}&mode={RESPONSE_FORMAT}&units={UNITS}')

    response_prev_3 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LAT}&lon={LON}&dt={ago[2]}&appid={API_KEY}&mode={RESPONSE_FORMAT}&units={UNITS}')

    response_prev_4 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LAT}&lon={LON}&dt={ago[3]}&appid={API_KEY}&mode={RESPONSE_FORMAT}&units={UNITS}')

    response_prev_5 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={LAT}&lon={LON}&dt={ago[4]}&appid={API_KEY}&mode={RESPONSE_FORMAT}&units={UNITS}')

    
    result_prev_1_json = response_prev_1.text
    result_prev_1 = json.loads(result_prev_1_json)

    result_prev_2_json = response_prev_2.text
    result_prev_2 = json.loads(result_prev_2_json)

    result_prev_3_json = response_prev_3.text
    result_prev_3 = json.loads(result_prev_3_json)

    result_prev_4_json = response_prev_4.text
    result_prev_4 = json.loads(result_prev_4_json)

    result_prev_5_json = response_prev_5.text
    result_prev_5 = json.loads(result_prev_5_json)


    # max temperatur der letzten 5 tage
    max_temps = [0, 0, 0, 0, 0]

    max = result_prev_1['hourly'][0]['temp']
    for i in range(24):
        deg = result_prev_1['hourly'][i]['temp']
        if max < deg:
            max = deg
    max_temps[4] = max

    max = result_prev_2['hourly'][0]['temp']
    for i in range(24):
        deg = result_prev_2['hourly'][i]['temp']
        if max < deg:
            max = deg
    max_temps[3] = max

    max = result_prev_3['hourly'][0]['temp']
    for i in range(24):
        deg = result_prev_3['hourly'][i]['temp']
        if max < deg:
            max = deg
    max_temps[2] = max

    max = result_prev_4['hourly'][0]['temp']
    for i in range(24):
        deg = result_prev_4['hourly'][i]['temp']
        if max < deg:
            max = deg
    max_temps[1] = max

    max = result_prev_5['hourly'][0]['temp']
    for i in range(24):
        deg = result_prev_5['hourly'][i]['temp']
        if max < deg:
            max = deg
    max_temps[0] = max


    # balkendiagramm
    plt.bar(prev_times, max_temps)
    plt.title('Max. Temperaturen der letzten 5 Tage')
    plt.xlabel('Tag')
    plt.ylabel('Temperatur in °C')
    plt.show()

if __name__ == '__main__':
    main()