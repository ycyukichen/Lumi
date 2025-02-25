![Lumi Chatbot](Lumi2.png)  
# Lumi AI Chatbot

Lumi is an emotionally intelligent AI chatbot designed to provide friendly and empathetic conversations. It integrates Groq's Llama 3.3 70B model and works with a fine-tuned BERT model from Hugging Face to generate responses while maintaining a warm and supportive tone. Whether you're feeling happy, sad, or just need someone to talk to, **Lumi is here for you**. 

Try Lumi here: https://huggingface.co/spaces/Yuki-Chen/Lumi_yourfriend 

## Features

- **Emotion Detection**: Analyzes user input to detect emotions and tailor responses accordingly.
- **Multilingual Support**: Currently, Lumi can response in multiple languages.
- **Concise Responses**: Ensures clear and to-the-point replies using optimized prompts and model parameters.
- **Groq API Integration**: Uses Llama 3.3 70B via Groq API for high-quality AI responses.
- **Fine-Tuned BERT Model**: Utilizes a fine-tuned BERT model from Hugging Face for emotion classification.
- **Streamlit Interface**: Provides a lightweight and interactive web chat experience.

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ycyukichen/Lumi.git
cd Lumi
```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Lumi requires a Groq API key for model access. Set your API key as an environment variable:

```bash
export GROQ_API_KEY="your_actual_groq_api_key"
```

### 4. Run the Chatbot

Start the chatbot using Streamlit:

```bash
streamlit run app.py
```

## API Integration

Lumi connects to Groq's Llama 3.3 70B model through the OpenAI-compatible API. The request format follows:

```python
def call_groq_llama3(prompt, max_tokens=150, temperature=0.5, top_p=0.7):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens, "temperature": temperature, "top_p": top_p}
    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"].strip() if response.status_code == 200 else f"Error: {response.status_code}"
```

## Customization

- Modify **temperature & top\_p** in `generate_response()` to adjust creativity.
- Edit **emotion prompts** in `emotion_prompts` to personalize chatbot tone.

## Future Improvements

- Enhance **memory** for contextual conversations.
- Implement **voice input & output** for accessibility.
- Optimize **response latency** with improved caching.
