import streamlit as st
import pickle
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import string
# creating an object of PorterStemmer since it is used ahead in the function to stem the words.
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()  # -- to lower
    text = nltk.word_tokenize(text)  # -- to words.

    y = []
    for i in text:  # -- removing non-alpha-numeric.
        if i.isalnum():
            y.append(i)

    # text = y ---> is wrong
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)  # -- in the form of string.


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")
input_sms  = st.text_area("Enter the message")

# steps that we will do here.

if st.button('Predict'):
    # 1. preprocess the message.
    transformed_sms = transform_text(input_sms)
    # 2. vectorize the data
    vector_input  = tfidf.transform([transformed_sms])
    # 3. Predict the category
    result = model.predict(vector_input)[0]
    # 4. Display the result.
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')