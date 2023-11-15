from sentence_transformers import SentenceTransformer, util
import json
import matplotlib.pyplot as plt

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

#Load the sentences
input = json.load(open('xml/sentences.json'))

#Access the relevant sentences
ackerSt = input['blackTarantula4']
srcSt = input['helen']

#Compute embeddings
ackerEmbeddings = model.encode(ackerSt, convert_to_tensor=True)
srcEmbeddings = model.encode(srcSt, convert_to_tensor=True)

#Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.cos_sim(ackerEmbeddings, srcEmbeddings)

# Initialize a dictionary to store the data
data = {}

# Loop through Acker sentences
for i in range(len(ackerSt)):
    acker_sentence = ackerSt[i]
    source_sentence_scores = {}
    
    # Loop through source sentences
    for j in range(len(srcSt)):
        source_sentence = srcSt[j]
        score_str = cosine_scores[i][j]
        # Convert the score from string to float
        score = float(score_str)
        source_sentence_scores[source_sentence] = score
    
    data[acker_sentence] = source_sentence_scores

# Write the data to a JSON file
with open('xml/cosineScores.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print("JSON data has been written to 'xml/cosineScores.json'")

# Data Filtering
# Load the JSON data
with open('xml/cosineScores.json', 'r') as f:
    data = json.load(f)

# Set the threshold
threshold = 0.4

# Filter the data
filtered_data = {}

for acker_sentence, source_sentence_scores in data.items():
    filtered_srcSt_scores = {}

    for src_sentence, score in source_sentence_scores.items():
        if float(score) >= threshold:
            filtered_srcSt_scores[src_sentence] = float(score)

    if filtered_srcSt_scores:
        filtered_data[acker_sentence] = filtered_srcSt_scores

# Write the filtered data to a new JSON file
with open('xml/cosineScores_filtered.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)

print("Filtered JSON data has been written to 'xml/cosineScores_filtered.json'")

