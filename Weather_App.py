import tkinter as tk
from tkinter import messagebox
import requests


class WeatherApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Weather App")

        # Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual OpenWeatherMap API key
        self.api_key = "YOUR_OPENWEATHERMAP_API_KEY"

        # Create and place widgets in the window
        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(
            root, text="Get Weather", command=self.get_weather
        )
        self.get_weather_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def get_weather(self):
        # Fetch weather information for the entered city using the OpenWeatherMap API
        city = self.city_entry.get()
        if city:
            try:
                response = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
                )
                data = response.json()

                if data["cod"] == 200:
                    # Extract relevant information from the API response
                    weather_description = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]

                    # Update the result label with weather information
                    result_text = f"Weather in {city}: {weather_description}\nTemperature: {temperature:.1f}°C"
                    self.result_label.config(text=result_text)
                else:
                    # Show a warning if the city is not found
                    messagebox.showwarning("Error", "City not found.")
            except requests.ConnectionError:
                # Show a warning if there is a connection error
                messagebox.showwarning("Error", "Failed to connect to the server.")
        else:
            # Show a warning if no city is entered
            messagebox.showwarning("Warning", "Please enter a city name.")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
