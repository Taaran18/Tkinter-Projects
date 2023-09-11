import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "YOUR_OPENWEATHERMAP_API_KEY"

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric")
                data = response.json()

                if data["cod"] == 200:
                    weather_description = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]
                    result_text = f"Weather in {city}: {weather_description}\nTemperature: {temperature:.1f}°C"
                    self.result_label.config(text=result_text)
                else:
                    messagebox.showwarning("Error", "City not found.")
            except requests.ConnectionError:
                messagebox.showwarning("Error", "Failed to connect to the server.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
