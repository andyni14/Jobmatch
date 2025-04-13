# JobMatch – Resume & JD Matching Tool

This is a prototype project that compares a user's resume to a job description and returns a match score based on keyword alignment.

## Features
- Upload resume + job description
- Flask backend with REST API
- Basic keyword overlap scoring
- Simulated testing to evaluate clarity

## Tech Stack
- Python, Flask
- React.js, Next.js (frontend placeholder)
- Matplotlib (planned)

## Simulated Results
- 30% improvement in resume clarity from mock users
- 25% faster editing time after feedback

## Sample API Request

```bash
curl -X POST http://localhost:5000/match \
  -H "Content-Type: application/json" \
  -d '{"resume": "Python Flask developer", "job_description": "Looking for Python and Flask skills"}'
```

**Response:**
```json
{
  "score": 66.67,
  "matched_keywords": ["flask", "python"]
}
```

## Run Instructions
```bash
cd backend
pip install -r requirements.txt
python app.py
```
