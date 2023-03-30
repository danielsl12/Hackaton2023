import os
from google.cloud import translate_v2

# Set up the Google Cloud Translate API client
translate_client = translate_v2.Client()

# Set up the directory where the TXT files are located
txt_dir = "./data_library/"

# Loop through each TXT file in the directory
for filename in os.listdir(txt_dir):
    if filename.endswith(".txt"):
        # Load the TXT file into a string
        with open(os.path.join(txt_dir, filename), "r", encoding="utf-8") as file:
            text = file.read()

        # Translate the text from Hebrew to English using the Google Cloud Translate API
        result = translate_client.translate(text, target_language="en")

        # Save the translated text to a new file
        new_filename = os.path.splitext(filename)[0] + "_en.txt"
        with open(os.path.join(txt_dir, new_filename), "w", encoding="utf-8") as file:
            file.write(result["translatedText"])
