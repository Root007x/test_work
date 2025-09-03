# Resume Parser and Analyzer

A FastAPI-based application that parses resumes, analyzes them against job descriptions, and provides scoring and recommendations.

## Features

- PDF Resume parsing
- Resume analysis against job descriptions
- Resume scoring
- CV rewriting suggestions
- FastAPI-powered REST API

## Project Structure

```
test_work/
├── src/
│   ├── api/
│   │   └── endpoints/
│   │       └── pdf_router.py
│   ├── config/
│   │   └── config.py
│   ├── core/
│   │   └── logging.py
│   ├── schemas/
│   │   └── prompts.py
│   ├── services/
│   │   ├── preprocessing.py
│   │   ├── rewrite_cv.py
│   │   └── score.py
│   ├── utils/
│   │   └── helper.py
│   └── main.py
├── data/
│   └── parsed_resume.json
├── logs/
├── notebooks/
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

## Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Other dependencies (listed in requirements.txt)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Root007x/test_work.git
   cd test_work
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your GROQ API key:
     ```
     GROQ_API_KEY=your_api_key_here
     LLM_MODEL_NAME=your_model_name
     ```

## Running the Application

Run the application from the project root directory:

```bash
python -m src.main
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### PDF Upload and Analysis

- **Endpoint**: `/pdf_upload`
- **Method**: POST
- **Parameters**:
  - `file`: PDF file (resume)
  - `job_des`: Job description text
- **Returns**: JSON response with analysis results

## Development

1. Create virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```

2. Install development dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run with reload for development:
   ```bash
   python -m src.main
   ```
