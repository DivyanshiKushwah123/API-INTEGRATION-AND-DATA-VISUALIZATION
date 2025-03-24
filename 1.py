import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API Configuration
API_KEY = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}"  # Replace with your API key
CITY = "indore"  # Replace with your city name
API_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch Data from API
def fetch_weather_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_list = data['list']
            weather_data = []
            
            for item in weather_list:
                weather_data.append({
                    "Date": item['dt_txt'],
                    "Temperature": item['main']['temp'],
                    "Humidity": item['main']['humidity'],
                    "Weather": item['weather'][0]['main']
                })
            
            return pd.DataFrame(weather_data)
        else:
            print("Failed to fetch data:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()

# Visualization
def visualize_data(df):
    if not df.empty:
        plt.figure(figsize=(14, 6))
        
        # Temperature Plot
        sns.lineplot(x='Date', y='Temperature', data=df, marker='o', color='blue')
        plt.title(f'Temperature Trend in {CITY}')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.show()

        # Humidity Plot
        plt.figure(figsize=(14, 6))
        sns.barplot(x='Date', y='Humidity', data=df, palette='coolwarm')
        plt.title(f'Humidity Levels in {CITY}')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Humidity (%)")
        plt.grid(True)
        plt.show()

# Main Function
if __name__ == "_main_":
    print(f"Fetching weather data for {CITY}...")
    weather_df = fetch_weather_data(API_URL)
    if not weather_df.empty:
        print(weather_df.head())
        visualize_data(weather_df)
    else:
        print("No data to visualize.")