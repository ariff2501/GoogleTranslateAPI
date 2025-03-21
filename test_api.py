import requests

# Define the API endpoint
api_url = 'http://127.0.0.1:5000/translate'  # Change to '/translating' if you've updated the route

# Sample data to send for translation
data = {
    'text': '안녕하세요.',  # The text you want to translate
    'dest': 'en',        # Target language (English)
    'src': 'auto'        # Source language (auto-detect)
}

try:
    # Send POST request to the API
    response = requests.post(api_url, json=data)

    # Check if the request was successful
    response.raise_for_status()  # Raises an exception for HTTP errors

    # Parse and print the JSON response
    translated_text = response.json()
    print('Translated Text:', translated_text['translatedText'])
except requests.exceptions.HTTPError as err:
    print('HTTP error occurred:', err)
except Exception as e:
    print('An error occurred:', e)