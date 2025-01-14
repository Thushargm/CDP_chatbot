# CDP Chatbot
This is a Django-based chatbot designed to answer "how-to" questions about Segment, mParticle, Lytics, and Zeotap platforms.

## Features
- Extracts answers directly from the official documentation of each CDP.
- Provides responses to questions such as "How to set up a source in Segment?" or "How to create a user profile in mParticle?"
- Handles variations in question phrasing and terminology.
- Includes a web-based UI.

## Requirements
- Python 3.8+
- Django 4.2
- Requests
- BeautifulSoup

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Access the chatbot at `http://127.0.0.1:8000/`.

## License
MIT
