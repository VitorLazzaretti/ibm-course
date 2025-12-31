import json
import requests

def emotion_detector(input_text):
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = {
        "raw_document": {
            "text": input_text
        }
    }
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    api_response = requests.post(api_url, json=payload, headers=headers)
    parsed_response = json.loads(api_response.text)

    results = {}

    if api_response.status_code == 400:
        results = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return results

    results = parsed_response['emotionPredictions'][0]['emotion']
    main_emotion = max(results, key=results.get)
    results['dominant_emotion'] = main_emotion

    return results


text_to_analyze = "I love this new technology!"
text = emotion_detector(text_to_analyze)
print(text)