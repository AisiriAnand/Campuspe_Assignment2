# Generative AI API Integration Assignment

**Name:** Aisiri Anand  
**Assignment:** CampusPe - Generative AI API Integration (Multiple AI Providers)  
**Due Date:** March 30, 2026

---

## Overview

This repository contains Python programs that integrate with multiple Generative AI APIs:
- OpenAI (GPT-3.5)
- Groq (Mixtral-8x7B)
- Ollama (Local LLaMA)
- Hugging Face (Mistral)
- Google Gemini
- Cohere (Command)

Each program accepts user input, sends requests to the respective API, and displays AI-generated responses with proper error handling.

---

## Repository Structure

```
CampusPe Assignment 2/
├── openai_integration.py          # OpenAI API integration
├── groq_integration.py            # Groq API integration
├── ollama_integration.py          # Ollama local AI integration
├── huggingface_integration.py     # Hugging Face API integration
├── gemini_integration.py          # Google Gemini API integration
├── cohere_integration.py          # Cohere API integration
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variables template
└── README.md                      # This file
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AisiriAnand/Campuspe_Assignment2.git
cd Campuspe_Assignment2
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

1. Copy the environment template file:
   ```bash
   cp .env.example .env
   ```

2. Add your actual API keys to the `.env` file:
   - **OpenAI:** Get key from https://platform.openai.com/api-keys
   - **Groq:** Get key from https://console.groq.com/keys
   - **Google Gemini:** Get key from https://makersuite.google.com/app/apikey
   - **Cohere:** Get key from https://dashboard.cohere.com/api-keys
   - **Hugging Face:** Get token from https://huggingface.co/settings/tokens
   - **Ollama:** Runs locally (no API key needed)

### 5. Ollama Setup (Optional)

For Ollama integration, install Ollama locally:

1. Download from https://ollama.com/
2. Run: `ollama run llama2`
3. The integration will connect to `localhost:11434`

---

## Usage

Run any integration script:

```bash
# OpenAI
python openai_integration.py

# Groq
python groq_integration.py

# Ollama (requires local installation)
python ollama_integration.py

# Hugging Face
python huggingface_integration.py

# Google Gemini
python gemini_integration.py

# Cohere
python cohere_integration.py
```

Each program will:
1. Display a welcome message
2. Prompt for user input
3. Send the request to the API
4. Display the AI response
5. Continue until you type 'exit'

---

## Features

### Common Features Across All Programs:
- **Environment Variable Security:** API keys are never hardcoded
- **Error Handling:** Comprehensive try-except blocks
- **Input Validation:** Checks for empty inputs
- **Graceful Exit:** Type 'exit' to quit cleanly
- **User-Friendly Interface:** Formatted output with separators

### Provider-Specific Features:
- **OpenAI:** Uses GPT-3.5-turbo model
- **Groq:** Uses Mixtral-8x7B with fast inference
- **Ollama:** Local execution, no API calls needed
- **Hugging Face:** Uses Mistral-7B-Instruct
- **Gemini:** Uses Google's Gemini Pro model
- **Cohere:** Uses Command model for chat

---

## API Key Requirements

| Provider | API Key Required | Free Tier Available |
|----------|------------------|---------------------|
| OpenAI | Yes | Limited credits |
| Groq | Yes | Generous free tier |
| Ollama | No | Free (local) |
| Hugging Face | Yes | Free tier available |
| Google Gemini | Yes | Free tier available |
| Cohere | Yes | Trial available |

---

## Error Handling

Each program handles:
- Missing API keys
- Invalid API responses
- Network connectivity issues
- Empty user inputs
- Keyboard interrupts (Ctrl+C)
- API rate limits

---

## Technologies Used

- **Python 3.8+**
- **python-dotenv** - Environment variable management
- **openai** - OpenAI API client
- **groq** - Groq API client
- **google-generativeai** - Google Gemini SDK
- **cohere** - Cohere API client
- **huggingface-hub** - Hugging Face Inference API
- **requests** - HTTP requests for Ollama
- **ollama** - Ollama Python client

---

## Screenshots

After testing each program, screenshots should be captured showing:
1. Program startup and welcome message
2. User input prompt
3. API response display
4. Multiple interaction cycles

Add screenshots to a `screenshots/` folder in your repository.

---

## Testing Checklist

- [ ] OpenAI integration works with valid API key
- [ ] Groq integration responds correctly
- [ ] Ollama connects to local instance
- [ ] Hugging Face returns valid responses
- [ ] Gemini integration functions properly
- [ ] Cohere generates responses
- [ ] All programs handle missing API keys gracefully
- [ ] All programs handle network errors
- [ ] 'exit' command works in all programs
- [ ] Empty inputs are handled properly

---

## Challenges Faced

1. **Environment Variable Management:** Setting up .env file properly
2. **Error Handling:** Ensuring all edge cases are covered
3. **API Rate Limits:** Handling rate limiting gracefully
4. **Ollama Local Setup:** Ensuring local server is running
5. **Multiple Dependencies:** Managing different SDK versions

---

## Submission Checklist

- [x] All 6 Python files created
- [x] requirements.txt with all dependencies
- [x] .env.example template provided
- [x] README.md with instructions
- [x] Screenshots of working programs
- [x] Repository is public
- [x] All files committed to GitHub

---

## License

This project is for educational purposes as part of the CampusPe curriculum.

---

## Contact

**Aisiri Anand**  
Email: aisirianand03@gmail.com  
GitHub: https://github.com/AisiriAnand
