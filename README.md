Link to the webpage: https://spam-message-detector.herokuapp.com/
# spam-message-detector
## About The Project
:: Following are the steps into which the project can be divided ::

**About the dataset:**
The dataset contained information about the different messages being spam or ham.
Since the data had characters from various languages and character set, we had use encoding: "ISO-8859-1" to load the file.
i.e., (df = pd.read_csv('spam.csv',encoding = "ISO-8859-1")

**1. Data Cleaning**
a. Dataset has 5 columns, of which last 3 had null values mostly, so I decided to drop them.
b. Dropped the duplicates rows while keeping the first occurance: dataset = dataset.drop_duplicates(keep = 'first')
c. Used LabelEncoder to provide labels to ham and spam messages.
 
**2. EDA**
a. % of ham ans spam messages: ham: - 87% and spam: - 12% --> implies the data is imbalanced.
b. Used nltk library to find the number of words, sentences, characters in the text column.
c. Created 3 more columns for ['num_characters','num_words','num_sentences']
d. From the summary of these features on ham and spam category we found that spam messages generally had greater mean value for number of words,chars,sentences.(i.e., spam messages are comparatively longer)
e. From the heatmap of correlation among all these numerical features, we got to know that there is multicollinearity among these features,( may be they all were derived form the same text columns. 0.97, 0.62, 0.68.. were their values...)
f. So Decided not to take all those features in model building ahead.
**3. Word Cloud**
a. Using the libraries of wordcloud, we can plot the top words appearing in any of the labels (spam or ham)
**4. Text Pre-Processing:**
   1. Lower case: converted the text data to lower case.[ text = text.lower(text) ]
   2. Tokenization: it separates the all the words in a sentence. [text = nltk.word_tokenize(text) ]
   3. Removing special Characters: using .isalnum() function, got rid of all the special characters (like %%$*#$@!.......)
   4. Removing stop words and punctuation: stopwords like is,am,are,you,,etc eliminated from the dataset.
   5. Stemming

5. Model Building
Classification Model Algorithms
Checking other classifiers: Voting & Stacking
Pickling the file
Streamlit app development
