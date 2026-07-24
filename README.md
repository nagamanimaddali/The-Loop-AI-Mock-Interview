# The Loop - AI-Powered Mock Interview Platform

## Overview

The Loop is an AI-powered mock interview platform that helps students and job seekers prepare for technical interviews. It uses the Google Gemini API to generate interview questions, ask adaptive follow-up questions, and provide AI-generated performance reports.

## Features

- AI-generated interview questions
- Adaptive follow-up questions
- Multiple interview topics
- Easy, Medium, and Hard difficulty levels
- Configurable number of questions
- Interview timer
- Progress tracking
- AI-generated interview report
- Performance analysis
- Strengths and weaknesses evaluation

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI
- Google Gemini API

### Deployment
- Docker
- AWS App Runner

## Project Structure

```
TheLoop
│
├── Backend
│   ├── app.py
│   ├── gemini.py
│   └── .env
│
└── Frontend
    ├── landing.html
    ├── setup.html
    ├── interview.html
    ├── Report.html
    ├── history.html
    └── about.html
```

## Installation

1. Clone the repository

```
git clone https://github.com/nagamanimaddali/The-Loop-AI-Mock-Interview.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create a `.env` file inside the Backend folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

4. Run the Flask server

```
python app.py
```

## Future Improvements

- Voice-based interviews
- Resume analysis
- AI-generated learning roadmap
- Per-question AI feedback

## Author

Nagamani Maddali