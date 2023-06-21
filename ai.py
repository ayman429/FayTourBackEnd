
import joblib
# Load the model using Joblib
tfidf_vectorizer = joblib.load('model5.joblib')
output2 = tfidf_vectorizer.get_recommendations(
    "I love museums and historical places, and I enjoy outdoor activities such as hiking and camping")
print(output2)