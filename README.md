# API-INTEGRATION-AND-DATA-VISUALIZATION

*company* : CODTECH IT SOLUTION

*NAME* : DIVYANSHI KUSHWAH

*INTERN ID * : CT08WQT

*DOMAIL* : PYTHON PROGRAMMING

*DURATION* :4 WEEKS

*MENTOR* :NEELA SANTHOSH

DESCRIPTION 
This Python script is designed to fetch weather forecast data for a specified city using the OpenWeatherMap API and visualize the data using the matplotlib and seaborn libraries. It begins by defining the API URL, which is constructed using the city name (set to Indore in this case) and an API key, which the user must replace with their own. The script sends a request to the API, retrieves the data in JSON format, and processes it into a structured format using Pandas. Specifically, it extracts the date, temperature (in Celsius), humidity, and general weather conditions from the forecast data and stores this information in a DataFrame. The script also includes error handling to manage issues like network failures or invalid responses. Once the data is successfully fetched, the visualize_data function is called to create two visualizations: a line plot showing the temperature trend over time and a bar plot displaying the humidity levels. Both plots use the date and time as the x-axis and temperature or humidity as the y-axis. The temperature plot is a line plot, while the humidity plot is a bar plot, both styled with markers, grid lines, and axis labels for clarity. The script thus allows users to easily visualize short-term weather patterns for a specified city, making it a useful tool for weather analysis or reporting. However, there is a minor error in the script where the if __name__ block is incorrectly written as _main_, which would need to be corrected for the script to run successfully.
