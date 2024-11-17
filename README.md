Project Name: Weather Data Pipeline

Project Description:

This Python project fetches weather data from the OpenWeatherMap API for a specified city, transforms it into a structured format, stores it in a SQLite database, and retrieves the latest entries. It utilizes a scheduling mechanism to update the database regularly.

Technologies and Tools:

Python (version 3.x): Core programming language
requests: Library for making HTTP requests to the API
pandas: Data analysis and manipulation library
sqlite3: Built-in Python library for interacting with SQLite databases
schedule: Third-party library (installation required) for scheduling tasks
Git: Version control system (not directly used in the code, but assumed for project management)
Virtual Environment: Recommended to isolate project dependencies (instructions provided)
Prerequisites:

Python 3.x installed (https://www.python.org/downloads/)
pip (Python package installer) included with Python installation
Setting Up the Project:

Clone the Repository:

Bash
git clone https://github.com/Koena-Developments/WeatherDataPipeline.git
Use code with caution.

Navigate to the project directory:

Bash
cd WeatherDataPipeline
Use code with caution.

Create and Activate a Virtual Environment (Recommended):

Windows:
Bash
python -m venv myworld
myworld\Scripts\activate
Use code with caution.

Linux/macOS:
Bash
python3 -m venv myworld   # Use python3 if you have multiple Python versions
source myworld/bin/activate
Use code with caution.

Install Required Packages:

Bash
pip install requests pandas schedule
Use code with caution.

Running the Project:

Update API_KEY and CITY variables:


API_KEY =4b5d02b2975cbc4485c633220da31f98
CITY = Johannesburg

to use your own
Replace API_KEY with your OpenWeatherMap API key (https://openweathermap.org/api).

Modify CITY to your desired location (e.g., "London", "Tokyo").
Start the data pipeline:

Bash
python pipeline.py
Use code with caution.

This will fetch the weather data, transform it, save it to the database (weather_data.db), and schedule updates every hour. The console will display success messages upon execution.

How it Works:

Fetch weather data:
The fetch_weather_data function retrieves weather data from the OpenWeatherMap API for the specified city.
Transform data:
The transform_data function converts the raw API response into a structured pandas DataFrame, extracting relevant information like temperature, humidity, and timestamp.
Create and load data into database:
create_table ensures the weather_data.db exists and defines a table structure.
load_data inserts the transformed data into the database.
Fetch latest data:
fetch_latest_data retrieves the five most recent entries from the database for visualization purposes.
Scheduling data updates:
The schedule library is used to automate the data pipeline execution every hour.
run_pipepline encompasses the fetching, transforming, and storing steps.
The while True loop continuously monitors the schedule and runs pending tasks.

Contact:

thabangmotswenyane511@gmail.com
