import requests
import pandas as pd
from datetime import datetime
import sqlite3
import schedule
import time


API_KEY = "4b5d02b2975cbc4485c633220da31f98"
CITY = "Johannesburg"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



def fetch_weather_data(city):
    params = {'q': city, 'appid': API_KEY, 'units':'metric'}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    
data = fetch_weather_data(CITY)
print(data)

def transform_data(data):
    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'weather': data['weather'][0]['description'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return pd.DataFrame([weather_info])


# testing if the data was tranformed

weather_df = transform_data(data)
print("TRANSFORMED DATA ")
print(weather_df)


# NOW WE NEED TO CREATE A DATA BASE TO LOAD THE DATA 

def create_table():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   city TEXT,
                   temperature REAL,
                   humidity INTEGER,
                   pressure INTEGER,
                   weather TEXT,
                   timestamp TEXT
                   )

''')

    conn.commit()
    conn.close()

def load_data(dataframe):
    conn = sqlite3.connect('weather_data.db')
    dataframe.to_sql('weather', conn, if_exists='append', index=False)
    print("data successfully loaded into the db...")
    conn.close()

create_table()
load_data(weather_df)


def fetch_latest_data():
    conn = sqlite3.connect('weather_data.db')
    query = "SELECT * FROM weather ORDER BY timestamp DESC LIMIT 5"
    df = pd.read_sql_query=(query, conn)
    conn.close()
    return df


print(fetch_latest_data())



def run_pipepline():
    data = fetch_weather_data(CITY)
    if data:
        transformed_data = transform_data(data)
        load_data(transformed_data)
        print("Data pipeline executed successfully")

schedule.every(1).hours.do(run_pipepline)


while True:
    schedule.run_pending()
    time.sleep(1)
