import os
import torch
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModelForCausalLM

BERT_MODEL_NAME = "Yuki-Chen/fine_tuned_BERT_goemotions_1"
LLAMA_MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"
hf_token = os.getenv("HUGGINGFACE_TOKEN")

@st.cache_data
def load_emotion_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(BERT_MODEL_NAME).to(device)
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading emotion model: {e}")
        return None, None

@st.cache_resource
def load_llama_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(LLAMA_MODEL_NAME, use_auth_token=hf_token)
        model = AutoModelForCausalLM.from_pretrained(
            LLAMA_MODEL_NAME,
            use_auth_token=hf_token,
            device_map="auto" if torch.cuda.is_available() else None,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True
        )
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading Llama model: {e}")
        return None, None
