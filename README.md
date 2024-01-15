<div align='center'>
  <h1>Live Weather Application 🌥️</h1>
</div>
<br>
<div align='center'>
  <br>
  <img src="https://github.com/altamsh04/Live-Weather-Application/assets/84860267/95867a0a-582d-43e1-8852-57e485e1811c" alt="Live Weather Application's Screenshot">
  <br>
</div>
<br>
The Live Weather Application is a Python-based weather application that provides real-time weather information for a given city. The application utilizes web scraping techniques with the Beautiful Soup library to extract weather data from Google Search results. The graphical user interface (GUI) is built using the tkinter library, and the application also features weather icons to represent the current weather condition.

## Technologies Used
- Python

## Python Modules Used
1. **tkinter:** Used for creating the graphical user interface (GUI) to interact with the user.
2. **requests:** Enables sending HTTP requests to retrieve weather data from Google Search.
3. **Beautiful Soup (bs4):** Used for web scraping to extract information from the HTML response.

## Features
1. **City-based Weather Information:**
   - Users can enter a city name, and the application fetches real-time weather data using web scraping.
2. **Current Weather Conditions:**
   - Displays current weather conditions, including temperature, weather description, and time.
3. **Additional Weather Information:**
   - Provides additional details such as precipitation, humidity, and wind speed.
4. **Weather Icons:**
   - Displays weather icons corresponding to the current weather condition for a more visually appealing representation.

## How to Use
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/altamsh04/Live-Weather-Application.git
   ```
2. Install the required libraries using the following commands:
   ```bash
   pip install requests
   pip install beautifulsoup4
   ```
3. Run the Python script `weather.py`.
4. Enter the desired city in the provided input field.
5. Click the "Find Weather" button to retrieve and display the weather information.
