Link to the webpage: https://spam-message-detector.herokuapp.com/
# spam-message-detector
## About The Project
:: Following are the steps into which the project can be divided ::
**About the dataset:**
The dataset contained information about the different messages being spam or ham.
Since the data had characters from various languages and character set, we had use encoding: "ISO-8859-1" to load the file.(df = pd.read_csv('spam.csv',encoding = "ISO-8859-1")

1. Data Cleaning
2. EDA
3. Word Cloud

4. Text Pre-Processing:
   1. Lower case
   2. Tokenization
   3. Removing special Characters
   4. Removing stop words and punctuation
   5. Stemming

5. Model Building
Classification Model Algorithms
Checking other classifiers: Voting & Stacking
Pickling the file
Streamlit app development
