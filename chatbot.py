import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error: Could not get response"

def load_template(path):
    with open(path, "r") as file:
        return file.read()

def main():
    zero_template = load_template("prompts/zero_shot_template.txt")
    one_template = load_template("prompts/one_shot_template.txt")

    queries = [
        "How can I track my order?",
        "My discount code is not working at checkout.",
        "What is your return policy?",
        "Can I cancel my order after placing it?",
        "How long does shipping take?",
        "I received a damaged product. What should I do?",
        "Do you offer cash on delivery?",
        "How can I change my delivery address?",
        "My payment was deducted but order not confirmed.",
        "Do you have international shipping?",
        "How do I apply a coupon code?",
        "Can I exchange a product for a different size?",
        "Why is my order delayed?",
        "How can I contact customer support?",
        "Is there any warranty on your products?",
        "How do I reset my account password?",
        "Can I return a product without the original packaging?",
        "What payment methods do you accept?",
        "How do I check my order history?",
        "Can I place an order without creating an account?"
    ]

    with open("eval/results.md", "w", encoding="utf-8") as file:
        for i, query in enumerate(queries, start=1):
            print(f"Processing Query {i}...")

            zero_prompt = zero_template.replace("{query}", query)
            one_prompt = one_template.replace("{query}", query)

            zero_response = query_ollama(zero_prompt)
            one_response = query_ollama(one_prompt)

            file.write(f"## Query {i}\n")
            file.write(f"**Customer Query:** {query}\n\n")

            file.write("### Zero-Shot Response:\n")
            file.write(zero_response + "\n\n")

            file.write("### One-Shot Response:\n")
            file.write(one_response + "\n\n")

            file.write("---\n\n")

if __name__ == "__main__":
    main()