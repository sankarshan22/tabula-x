import requests
import re

# Converts a full name to the format: First initial + full last name
# def convert_name_format(full_name):
#     parts = full_name.strip().split()
#     if len(parts) >= 2:
#         first_initial = parts[0][0].upper() + '.'
#         last_name = " ".join(parts[1:]).upper()
#         return f"{first_initial} {last_name}"
#     return full_name


# def extract_name_only(text):
#     match = re.search(r"\b[A-Z]\.\s+[A-Z]+(?:\s+[A-Z]+)*", text.upper())
#     return match.group(0) if match else text.strip().upper()

# --- Main ---

# Define the full name manually


# Set the prompt you want to send to Mistral
prompt = f"""" There was a train for "YENNISHHETY KARTHIKEY" on the dateof 03/27/2025
            1. Identify the date and name fromm the above given sentence.
            2. Identify the name and Convert the full name  into the format: First name first letter + full second name, just result only.
            3. Identify conver the date to dd/mm/yyyy form.
            4.rewrite the full sencentce with changed parameters
             respond to only aksed questions only, just result only
            """
                

# Send request to Mistral via Ollama API (assuming Mistral is running locally)
response = requests.post(
    'http://localhost:11434/api/generate',  # Ensure this is the correct URL for Mistral via Ollama
    json={
        "model": "mistral",  # Mistral model name
        "prompt": prompt,
        "temperature": 0.5,
        "stream": False
    }
)

# Get and clean model response
generated_output_raw = response.json().get("response", "").strip()
# generated_output = extract_name_only(generated_output_raw)

# Compare
# match = generated_output == expected_output
# bleu_score = 1.0 if match else 0.0

# # Output
print(f"Generated Output: {generated_output_raw}")
# print(f"Expected Output: {expected_output}")
# print(f"BLEU Score: {bleu_score}")
