Link to the webpage: https://spam-message-detector.herokuapp.com/
# spam-message-detector
## About The Project
:: Following are the steps into which the project can be divided ::

**About the dataset:**
The dataset contained information about the different messages being spam or ham.
Since the data had characters from various languages and character set, we had use encoding: "ISO-8859-1" to load the file.
i.e., (df = pd.read_csv('spam.csv',encoding = "ISO-8859-1")

**1. Data Cleaning**
- Dataset has 5 columns, of which last 3 had null values mostly, so I decided to drop them.
- Dropped the duplicates rows while keeping the first occurance: dataset = dataset.drop_duplicates(keep = 'first')
- Used LabelEncoder to provide labels to ham and spam messages.
 
**2. EDA**
- % of ham ans spam messages: ham: - 87% and spam: - 12% --> implies the data is imbalanced.
- Used nltk library to find the number of words, sentences, characters in the text column.
- Created 3 more columns for ['num_characters','num_words','num_sentences']
- From the summary of these features on ham and spam category we found that spam messages generally had greater mean value for number of words,chars,sentences.(i.e., spam messages are comparatively longer)
- From the heatmap of correlation among all these numerical features, we got to know that there is multicollinearity among these features,( may be they all were derived form the same text columns. 0.97, 0.62, 0.68.. were their values...)
- So Decided not to take all those features in model building ahead.
**3. Word Cloud**
- Using the libraries of wordcloud, we can plot the top words appearing in any of the labels (spam or ham)
**4. Text Pre-Processing:**
   1. Lower case: converted the text data to lower case.[ text = text.lower(text) ]
   2. Tokenization: it separates the all the words in a sentence. [text = nltk.word_tokenize(text) ]
   3. Removing special Characters: using .isalnum() function, got rid of all the special characters (like %%$*#$@!.......)
   4. Removing stop words and punctuation: stopwords like is,am,are,you,,etc eliminated from the dataset.
   5. Stemming: this removes the different verb forms of a word, and give the root word.

**5. Model Building**
a. Used CountVectorizer() and TfidfVectorizer() to get the vector form of the dataset.
b. Trained the model on Naive Bayes Algorithms-GaussianNB, MultinomialNB,BernoulliNB. since text data are known to perform better on naive bayes models.
c. MultinomialNB performed better amongst them (accuracy: 97%, precision_score:1.00).
d. Used other Classification models like svm, knn,randomforest,logistic-reg,decision-tree,adaboost,bagging,extra-tree,gradient-boosting,xgb.. but the mulitnomial Naive bayes out-performed them.
e. Also checked the model accuracy on adding new fetures column: num_characters, but there was hardly any change in precisio/accuracy.

_Checking other classifiers: Voting & Stacking_

g. Tried re-training the model using some other ensemble based learning models like voting classifer and stacking---> but no appreciable change in the result.
h. Finally trained the model (mulitinomial NB ) with tfidf vectorizer with no of features = 3000.(ie. taking top 3000 words only).(without num-characters)


**6. Pickling the file:**
a. pickled the tfid-(vectorizer) and mnb-(multinomial NB) files.

**7.Streamlit app development**
a. Writing the code for the streamlit app followed only 4 basic steps.
   - - 0 . Taking the input:[ input-sms= st.text_area("enter the message")]
   - - 1 . Pre-Processing the messages.
   - - 2 . Vectorizing the processed message.
   - - 3 . Predicting the category using model.predict() function.
   - - 4 . Displaying the result: 
