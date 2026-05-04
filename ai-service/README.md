# Email Digest AI Service

AI-powered microservice for summarizing emails and providing recommendations.

## Tech Stack
- **Python 3.11**
- **Flask**
- **Groq API (LLaMA-3.3-70b)**
- **Redis** (Caching)
- **Flask-Limiter** (Rate limiting)

## Setup

1. Create a `.env` file in this directory:
   ```env
   GROQ_API_KEY=your_key_here
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the service:
   ```bash
   python app.py
   ```

## API Reference

### POST `/api/v1/ai/describe`
Summarizes an email body and provides sentiment.
**Request:**
```json
{ "email_body": "..." }
```

### POST `/api/v1/ai/recommend`
Provides 3 actionable recommendations.
**Request:**
```json
{ "description": "...", "sentiment": 0.8 }
```

### POST `/api/v1/ai/generate-report`
Generates a structured digest report.
**Request:**
```json
{ "summaries": ["...", "..."] }
```

### GET `/health`
Returns service status.
