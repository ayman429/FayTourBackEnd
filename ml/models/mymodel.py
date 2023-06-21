import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib


# Similarity Calculation

class Recommendation:
    def __init__(self):
        # Load data from API
        place_response = 'http://faytourapp.pythonanywhere.com/api/TourismPlace/'
        place_headers = {
            'Authorization': 'Token 463b03a1419c5b8908382d397cba4c06a85a5b17'
        }
        place_response_obj = requests.get(
            place_response, headers=place_headers)
        if place_response_obj.status_code == 200:
            self.place_data = pd.DataFrame(place_response_obj.json())
        else:
            print("Error fetching place data from API: ",
                  place_response_obj.status_code)
    
    def get_recommendations(self, name):
        place_data = self.place_data.copy()
        # place_data.drop_duplicates(subset='name', keep='first', inplace=True)
        # place_data.dropna(subset=['description', 'type'], inplace=True)
        # place_data.reset_index(inplace=True, drop=True)
        
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        place_tfidf = tfidf_vectorizer.fit_transform(place_data['description'])
        user_tfidf = tfidf_vectorizer.transform([name])
        similarity_scores = cosine_similarity(
            user_tfidf, place_tfidf).flatten()
        place_data['similarity_score'] = similarity_scores
        place_data.sort_values(by='similarity_score',
                               ascending=False, inplace=True)
        recommendations = place_data[['name', 'id', 'similarity_score']].head(5)
        return recommendations


# Create an object of Recommendation class
my_object =Recommendation()
inputmodel ="I love museums and historical places, and I enjoy outdoor activities such as hiking and camping"
# x =my_object.get_recommendations(inputmodel)
joblib.dump(my_object, 'model3.joblib')


# Load the model 
# loaded_model = joblib.load('model2.joblib')

# # Dump it again without Recommendation
# joblib.dump(loaded_model, 'model2.joblib')  

# # Load the modified model 
# loaded_model = joblib.load('model2.joblib') 
# Call the get_recommendations method with an input
# output = my_object.get_recommendations(
#     "I love museums and historical places, and I enjoy outdoor activities such as hiking and camping")

# # Print the output
# print(output)

# Save the model using Joblib

# Load the model using Joblib
# aaaaa= joblib.load('model3.joblib')
# output2 = aaaaa.get_recommendations(
#     "I love museums and historical places, and I enjoy outdoor activities such as hiking and camping")
# print(output2)