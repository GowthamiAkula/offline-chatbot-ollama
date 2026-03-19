# 🛍️ Offline Customer Support Chatbot using Ollama & Llama 3.2

## 📌 Project Overview

This project implements an **offline AI-powered customer support chatbot** using **Ollama** and **Llama 3.2 (3B model)**. The chatbot is designed to handle common e-commerce queries such as order tracking, returns, payments, and account issues—without sending any data to external servers.

The main objective is to evaluate the effectiveness of **local Large Language Models (LLMs)** and compare **Zero-Shot vs One-Shot prompting techniques**.

---

## 🚀 Features

* ✅ Fully offline chatbot (no internet required after setup)
* ✅ Uses Llama 3.2 model via Ollama
* ✅ Supports 20 real-world e-commerce queries
* ✅ Implements Zero-Shot and One-Shot prompting
* ✅ Generates and logs responses automatically
* ✅ Includes evaluation with scoring (Relevance, Coherence, Helpfulness)

---

## 🏗️ Project Structure

```
offline-chatbot-project/
│
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
├── eval/
│   └── results.md
│
├── chatbot.py
├── setup.md
├── report.md
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Ollama (Local LLM runtime)
* Llama 3.2 (3B model)
* Requests library

---

## 🔄 How It Works

1. User queries are predefined in `chatbot.py`
2. Queries are inserted into:

   * Zero-shot prompt template
   * One-shot prompt template
3. Requests are sent to Ollama API:

   ```
   http://localhost:11434/api/generate
   ```
4. Llama 3.2 generates responses
5. Results are saved in `eval/results.md`
6. Responses are evaluated and scored

---

## 🧠 Prompting Techniques

### 🔹 Zero-Shot Prompting

* No examples provided
* Model relies only on instructions

### 🔹 One-Shot Prompting

* Includes one example
* Produces more structured and consistent responses

---

## 📊 Evaluation Criteria

Each response is evaluated on:

* **Relevance (1–5):** Accuracy of response
* **Coherence (1–5):** Clarity and grammar
* **Helpfulness (1–5):** Practical usefulness

---

## ▶️ How to Run

1. Install Ollama: [https://ollama.com](https://ollama.com)
2. Pull model:

   ```
   ollama pull llama3.2:3b
   ```
3. Activate virtual environment:

   ```
   source venv/Scripts/activate
   ```
4. Install dependencies:

   ```
   pip install requests datasets
   ```
5. Run chatbot:

   ```
   python chatbot.py
   ```

---

## 📈 Results Summary

* One-shot prompting showed better consistency and helpfulness
* Zero-shot responses were more detailed but less structured
* Local LLM performed effectively for basic customer support tasks

---

## ⚠️ Limitations

* No real-time order or database integration
* Responses may vary due to probabilistic nature of LLMs
* Slower performance on CPU-based systems

---

## 🔮 Future Improvements

* Integrate real-time backend (orders, tracking)
* Use larger or fine-tuned models
* Add web interface (UI)
* Improve response consistency

---

## 👩‍💻 Author

Gowthami Akula

---