from transformers import pipeline
model_name = "IMSyPP/hate_speech_en"
classifier = pipeline("text-classification", model=model_name)
     

label_mapping = {
    'LABEL_0': 'acceptable',
    'LABEL_1': 'inappropriate',
    'LABEL_2': 'offensive',
    'LABEL_3': 'violent'
}

def classify_text(texts):
    results = classifier(texts)
    return [{'comment': text, 'label': label_mapping[result['label']]} for text, result in zip(texts, results)]

# Example usage
texts_to_classify = ["great", "you are fat","yo a looser","very good","bitch","pussy","Ariza is a snake and a coward"" but at least he isn't a cripple like your hero Roach lmaoo"]
custom_predictions = classify_text(texts_to_classify)

for pred in custom_predictions:
    if pred['label'] == "acceptable":
      print(pred['comment'])
    else:
      print(f"{pred['label']}")

