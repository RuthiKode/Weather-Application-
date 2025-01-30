import socket
import tkinter as tk
from tkinter import messagebox

# Function to get weather data
def fetch_weather():
    try:
        # Connect to the server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 5000))  # Use server IP if needed

        # Send city name
        city_name = city_entry.get()
        if not city_name.strip():
            messagebox.showerror("Error", "Please enter a city name!")
            return

        client.send(city_name.encode("utf-8"))

        # Receive and display weather data
        weather_data = client.recv(4096).decode("utf-8")
        result_label.config(text=weather_data)

        # Close connection
        client.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Input field for city name
city_label = tk.Label(app, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

# Button to fetch weather
fetch_button = tk.Button(app, text="Get Weather", font=("Arial", 12), command=fetch_weather)
fetch_button.pack(pady=10)

# Label to display results
result_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

# Start the GUI loop
app.mainloop()