import boto3
import os
aws_access_key_id = "AKIAUJVBNW2TBB5VTU5S"
aws_secret_access_key = "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"

def translate_text(text, target_language='en'):
    # Set up the AWS Translate client
    translate = boto3.client(service_name='translate',
                            region_name='us-west-2', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

    # Translate the text
    result = translate.translate_text(Text=text, SourceLanguageCode='he' if target_language=='en' else 'he', TargetLanguageCode=target_language)

    # Print the translated text
    print(f'Translated text: {result["TranslatedText"]}')
    return result["TranslatedText"]

for file in os.listdir('../data_library_hebrew'):
    if file.endswith('.txt'):
        with open(os.path.join('../data_library_hebrew', file), 'r') as f:
            text = f.read()

            # Split "translation" into 5000 character chunks	
            with open(os.path.join('../aws_translations', file), 'x') as f:
                texts = [text[i:i+5000] for i in range(0, len(text), 5000)]
                for texti in texts:
                    translation = translate_text(texti)
                    f.write(translation)