# Offline Customer Support Chatbot Report

## 1. Introduction
This project aims to build an offline customer support chatbot using Ollama and Llama 3.2. The goal is to evaluate the effectiveness of local LLMs and compare zero-shot and one-shot prompting techniques.

## 2. Methodology
We created 20 e-commerce-related customer queries and used two prompting techniques:
- Zero-shot prompting
- One-shot prompting

We evaluated responses based on:
- Relevance
- Coherence
- Helpfulness

## 3. Results & Analysis

### Average Scores

- Zero-Shot:
  - Relevance: 4.6
  - Coherence: 5.0
  - Helpfulness: 4.3

- One-Shot:
  - Relevance: 4.8
  - Coherence: 5.0
  - Helpfulness: 4.5

### Comparative Analysis

From the evaluation, one-shot prompting consistently outperformed zero-shot prompting in relevance and helpfulness. This is because the example provided in one-shot prompts guided the model toward more structured and context-aware responses.

Zero-shot responses were often more detailed but sometimes inconsistent in tone and structure. In contrast, one-shot responses were concise, professional, and aligned with customer support expectations.

### Example Observation

For the query "My discount code is not working", the zero-shot response asked for additional details, while the one-shot response directly provided a helpful troubleshooting approach. This shows that one-shot prompting improves response effectiveness.

## 4. Conclusion & Limitations
The Llama 3.2 3B model is effective for basic customer support tasks. However, it has limitations such as lack of real-time data and occasional inconsistencies.

Future improvements could include:
- Using larger models
- Integrating real-time databases
- Fine-tuning responses