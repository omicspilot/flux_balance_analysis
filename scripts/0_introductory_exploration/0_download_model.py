import requests
import os
import sys

# A dictionary of available E. coli models from BiGG
AVAILABLE_MODELS = {
    "1": "iML1515",  # E. coli K-12 MG1655
    "2": "iJO1366",  # E. coli K-12 MG1655
}

# Prompt user for choice
print("Please choose which E. coli model to download:")
for key, value in AVAILABLE_MODELS.items():
    print(f"  {key}: {value}")

choice = input("Enter the number of your choice: ")
model_id = AVAILABLE_MODELS.get(choice)

if not model_id:
    print("❌ Invalid choice. Exiting.", file=sys.stderr)
    sys.exit(1)

# Ensure the target directory exists
output_dir = "models"
os.makedirs(output_dir, exist_ok=True)

# Construct URL and file path
url = f"http://bigg.ucsd.edu/static/models/{model_id}.json"
file_path = os.path.join(output_dir, f"{model_id}.json")

# Check if the file already exists
if os.path.exists(file_path):
    print(f"✅ Model file '{file_path}' already exists. Skipping download.")
    sys.exit(0)

print(f"⬇️  Downloading {model_id} from {url}...")
try:
    # Add a User-Agent header to mimic a browser, which can help with network issues.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Save to models/ directory
    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Model successfully downloaded to {file_path}")

except requests.exceptions.RequestException as e:
    print(f"❌ Failed to download model. Error: {e}", file=sys.stderr)
    sys.exit(1)
