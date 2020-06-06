import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

print("=== Welcome to article classifier ===")

print("\nPlease wait while the platform is booting...")

df_train = pd.read_csv('../data/data_train.csv')
X_train, X_test, y_train, y_test = train_test_split(df_train['article'], df_train['occupation'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train.values.astype('U'))
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

while True:
    print("\nEnter path of file to predict or \"exit\" to exit:")
    path = input()
    if path == "exit":
        break
    datafile=open(path, "r")
    data = "\n".join(datafile.readlines())
    print("\nOccupation: ",clf.predict(count_vect.transform([data]))[0])

print("\nThanks for using...")