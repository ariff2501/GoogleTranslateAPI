﻿# GoogleTranslateAPI

This project is a simple Translation API built with Flask that utilizes the Google Translate library to translate text between different languages.

## Features
- Translate text from one language to another.
- Supports auto-detection of the source language.
- Default target language is English.

## Technologies Used
- Python
- Flask
- googletrans library

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

## Installation Steps

### Clone the Repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
### Create a Virtual Environment
```bash
python -m venv venv
```

### Activate the Virtual Environment
#### On Windows :
```bash
venv\Scripts\activate
```
#### On macOS/Linux:
```bash
source venv/bin/activate
```
### Install Required Dependencies
```bash
pip install -r requirements.txt
```
## Usage

### 1. Run the Flask application:
```bash
python app.py
```
### 2. Access the API at `http://localhost:5000/`.

## Endpoints
- GET /: Returns a welcome message.
- POST /translate: Translates the given text.
### Request Format
```bash
{
  "text": "Text to be translated",
  "dest": "en",   // Optional: Target language (default is English)
  "src": "auto"   // Optional: Source language (default is auto-detect)
}
```
### Response
```bash{
  "translatedText": "Hello"
}
```
### Example
```bash
curl -X POST http://localhost:5000/translate -H "Content-Type: application/json" -d '{"text": "Bonjour", "dest": "en"}'
```
