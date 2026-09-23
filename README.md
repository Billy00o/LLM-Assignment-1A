# LLM Assignment 1A – Phi-4-mini Chatbot

**Course:** AI (Large Language Model)  
**Assignment:** 1A – Implementation of Large Language Model Applications  
**Group Members:**  
- Student 1: Leong Chon Hou – P2303322 
- Student 2: Xu Wei Ye - P2319796

**Project Title:** Simple Chatbot using Microsoft Phi-4-mini

---

## 1. Objective

The goal of this assignment is to explore and implement a Large Language Model application by:

- Loading a pretrained open-source LLM (Phi-4-mini)
- Integrating it with LangChain
- Building a simple interactive chatbot with conversation memory
- Testing the model’s output quality and coherence

---

## 2. Model Used

- **Model:** Microsoft Phi-4-mini-instruct
- **Parameters:** 3.8B
- **Format:** GGUF (Q4_K_M quantization)
- **Source:** [bartowski/microsoft_Phi-4-mini-instruct-GGUF](https://huggingface.co/bartowski/microsoft_Phi-4-mini-instruct-GGUF)
- **License:** MIT
- **Why this model?**  
  It offers excellent performance for its small size, runs well on CPU, and is suitable for student hardware.

---

## 3. Project Structure
AI_Assignment1A/
├── models/                              # Put .gguf file here
│   └── Phi-4-mini-instruct-Q4_K_M.gguf
├── llm_env                              # Virtual environment
├── chatbot.py                           # Main chatbot application
├── test_llm.py                          # Simple unit test
├── requirements.txt
├── README.md
└── RESULTS.md


> **Note:** The large model file (`.gguf`) is **not** uploaded to GitHub due to size limits. Users must download it themselves.

---

## 4. Prerequisites

- Python 3.8 or higher
- Git
- VS Code (or any IDE)
- At least 4–6 GB free RAM (8 GB recommended)
- Internet connection 

---

## 5. Installation Guide

### Step 1: Clone the repository
```bash
git clone [your-github-repo-url]
cd LLM_Assignment1A

Step 2: Create and activate virtual environment
Windows:
Bashpython -m venv llm_env
llm_env\Scripts\activate
macOS / Linux:
Bashpython -m venv llm_env
source llm_env/bin/activate

Step 3: Install dependencies
Bashpip install -r requirements.txt

Step 4: Download the model from Hugging Face

Create the models folder:
Bashmkdir models
Download the model 
Go to: https://huggingface.co/bartowski/microsoft_Phi-4-mini-instruct-GGUF
Download the file microsoft_Phi-4-mini-instruct-Q4_K_M.gguf
Place it inside the models folder
Rename it to Phi-4-mini-instruct-Q4_K_M.gguf

## 6. How to Run the chatbot
Bashpython chatbot.py

Example:
textYou: what is the capital of China
Bot: The capital of China is Beijing.

You: exit
Goodbye!

## 7. Testing
Run the unit test:
Bashpython test_llm.py

Model answer: The capital of France is Paris.
Test passed!



## 8. Videos
1. Installation
2. Implementation
3. Testing


## 9. Requirements
langchain
langchain-community
llama-cpp-python
huggingface_hub
