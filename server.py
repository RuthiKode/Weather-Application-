import socket
import requests

def get_weather(city):
    try:
        # WeatherAPI Endpoint and API Key
        api_key = "f85f5f5ddec54d1ebe6121611241512"
        base_url = "http://api.weatherapi.com/v1/current.json?"
        complete_url = f"{base_url}key={api_key}&q={city}"

        # Fetching weather data
        response = requests.get(complete_url)
        data = response.json()

        # Checking for valid response
        if "error" not in data:
            location = data["location"]["name"]
            temperature = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]
            condition = data["current"]["condition"]["text"]

            weather_info = (
                f"City: {location}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} km/h\n"
                f"Condition: {condition}"
            )
        else:
            weather_info = "City not found."
    except Exception as e:
        weather_info = f"Error: {e}"

    return weather_info

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))  # Use your IP/port if needed
server.listen(5)
print("Server is listening on port 5000...")

while True:
    client_socket, client_address = server.accept()
    print(f"Connection established with {client_address}")

    # Receive city name from client
    city = client_socket.recv(1024).decode("utf-8")
    print(f"City requested: {city}")

    # Fetch weather and send response
    weather_data = get_weather(city)
    client_socket.send(weather_data.encode("utf-8"))

    # Close connection
    client_socket.close()
