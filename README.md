# Jurisdiction-Aware Chatbot (Flask Demo)

🛡️ This project demonstrates a chatbot with basic legal risk detection based on user location, using Flask.

## Features

- Detects user jurisdiction based on IP
- Assesses legal risk level (low, medium, high)
- Filters banned keywords per country
- Returns filtered or redirected response if risk is high

## Structure

```
├── main.py
├── risk_engine.py
├── filters.py
├── requirements.txt
└── data/
    └── blocked_words.json
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python main.py
```

3. Test it:

```bash
curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"message": "hello"}'
```

## For Replit

Upload all files and just press **Run**.

---

This project is a prototype for educational use only.