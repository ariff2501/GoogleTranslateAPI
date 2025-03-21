from flask import Flask, request, jsonify
from googletrans import Translator
import asyncio

app = Flask(__name__)

async def translate_text(text, dest='en', src='auto'):
    translator = Translator()
    translation = await translator.translate(text, dest=dest, src=src)
    return translation.text


@app.route('/')
def home():
    return "Welcome to the Translation API!"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    print('received data :',data)
    text = data.get('text')  # Get text to translate (mandatory)
    
    # Get optional parameters
    dest_language = data.get('dest', 'en')  # Default destination is English
    src_language = data.get('src', 'auto')  # Default source is auto-detection

    if not text:
        return jsonify({'error': 'Text to translate is required!'}), 400

    try:
        # Call the async translate_text function
        result = asyncio.run(translate_text(text, dest=dest_language, src=src_language))
        return jsonify({'translatedText': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)