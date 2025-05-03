import requests
from dateutil import parser
from nltk.translate.bleu_score import sentence_bleu
import re

# Extract date string from the prompt
def extract_date_from_prompt(prompt):
    match = re.search(r"'([^']+)'", prompt)
    return match.group(1) if match else None

# Convert extracted date to expected format
def get_expected_date_from_prompt(prompt):
    date_str = extract_date_from_prompt(prompt)
    if not date_str:
        return None
    try:
        # Clean ordinal suffixes
        date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
        date_obj = parser.parse(date_str)
        return date_obj.strftime("%d-%m-%Y")
    except (ValueError, OverflowError) as e:
        print(f"Error parsing date: {e}")
        return None

# Function to extract date from response (if extra text appears)
def extract_date_only(text):
    match = re.search(r"\d{2}-\d{2}-\d{4}", text)
    return match.group(0) if match else text.strip()

# --- Main ---
prompt = "Convert '12th of July, 2000' to dd-mm-yyyy format. Respond with the date only."

expected_output = get_expected_date_from_prompt(prompt)

# Send request to LLaMA2
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "llama2",
        "prompt": prompt,
        "temperature": 0.5,
        "stream": False
    }
)

# Clean and extract generated output
generated_output = response.json().get("response", "").strip()
generated_output = extract_date_only(generated_output)

# Tokenize
expected_tokens = expected_output.split("-") if expected_output else []
generated_tokens = generated_output.split("-") if generated_output else []

# Check if the generated output matches the reference output exactly
if generated_output == expected_output:
    bleu_score = 1.0
else:
    bleu_score = 0.0

# Output results
print(f"Generated Output: {generated_output}")
print(f"Expected Output: {expected_output}")
print(f"BLEU Score: {bleu_score:.4f}")
