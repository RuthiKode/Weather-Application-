# Weather-Application-
Overview
This Weather App is a simple client-server application that fetches real-time weather data using Python, Socket Programming, and Tkinter for the GUI. The client sends a city name to the server, which then retrieves weather details from an API and sends the response back to the client for display.

Key Features
Client-Server Architecture: Uses Python sockets for communication.
Real-Time Weather Data: Fetches live weather information using WeatherAPI.
User-Friendly GUI: Built with Tkinter for an intuitive user experience.
Error Handling: Displays messages for invalid inputs or connection failures.
Technology Stack
Python – Core language for both client and server.
Socket Programming – For establishing communication between client and server.
Requests Library – For making API calls to retrieve weather data.
Tkinter – For GUI development on the client side.
How It Works
The server listens for incoming connections and processes weather requests.
The client sends the requested city name to the server.
The server fetches weather data using the WeatherAPI and sends it back.
The client displays the received weather information in the GUI.
Use Cases
Can be used as a simple weather-checking tool.
Demonstrates network programming and API integration.
Serves as a learning project for Python socket communication.
