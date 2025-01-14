# CDP_chatbot

README
CDP Support Agent Chatbot
This is a chatbot application designed to answer "how-to" questions related to Segment, mParticle, Lytics, and Zeotap platforms. It extracts relevant instructions from the official documentation of these platforms to guide users effectively.

Features
How-to Guidance:

Answers platform-specific questions, such as setting up sources, creating profiles, or building audience segments.
Example Questions:
"How do I set up a new source in Segment?"
"How can I create a user profile in mParticle?"
"How do I build an audience segment in Lytics?"
"How can I integrate my data with Zeotap?"
Documentation Parsing:

Fetches and processes content from official documentation:
Segment
mParticle
Lytics
Zeotap
Question Variability Handling:

Processes questions with diverse phrasing and terminology.
Handles irrelevant questions gracefully.
Bonus Features
Cross-CDP Comparisons: Explains differences in features or workflows across the platforms.
Advanced Queries: Supports complex, platform-specific "how-to" instructions.
Requirements
Python 3.8+
Django 4.2
NLP libraries or a simple document indexer
Web development tools/frameworks
How to Run
Clone the repository.
Install dependencies: pip install -r requirements.txt
Configure the environment variables in a .env file.
Run migrations: python manage.py migrate
Start the application: python manage.py runserver
Access the chatbot at http://127.0.0.1:8000/.
License
MIT

Packaging (requirements.txt)
makefile
Copy code
spacy
gunicorn
psycopg2-binary
Django==4.2.5
python-dotenv==1.0.0
openai==0.28.0
django-extensions==3.2.5
django-sslserver==0.23
beautifulsoup4==4.12.0
requests==2.28.2
Let me know if you'd like this packaged into a PDF or need further refinements.
