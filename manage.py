#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Recruitment_Management2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    class Preprocess:
        def __init__(self,method='WordNetLemmatizer'):
            # WordNetLemmatizer is recommended because it reduces the given word to the root word 
            # by referring to the WordNet corpus unlike other stemming techniques which just 
            # truncate the word by removing the suffix, which is why I have set it as default
            self.method = method
            self.stemmers = {
                'PorterStemmer':PorterStemmer(),
                'LancasterStemmer':LancasterStemmer(),
                'SnowballStemmer':SnowballStemmer(language='english'),
                'WordNetLemmatizer':WordNetLemmatizer()
            }
            self.stemmer = self.stemmers[self.method]
            # Remove punctuation signs and stopwords for better results 
            self.stopWords = list(punctuation) + list(stopwords.words('english'))
            # Adding custom stopwords for better preprocessing, feel free to add more
            self.moreStopWords = ['job','description','requirement','skill', 'qualification']
            self.stopWords.extend(self.moreStopWords)
            self.encoder = LabelEncoder()
            # Using tf-idf vectorizer because it not only relies on the count but also the 
            # number of documents it occurs in 
            # tf * log(N/df), where tf = term frequency/count of words 
            # N = total number of documents 
            # df = document frequency (number of documents containing that word)
            # Count vectorizer gets tricked by the term frequency but in tf-idf it does not happen
            # eg - if the word occurs frequently in almost all documents,it may be a filler word 
            # which was ignored in stopwords, so it can trick the count vectorizer,but in tf-idf
            # N/df almost = 1, so log(N/df) will be almost 0 and hence the word will not be given 
            # much importance which is desirable, hence we should use tfidf vectorizer instead of 
            # count vectorizer 
            self.vectorizer = TfidfVectorizer()
            self.isFitted = False
        def preprocess(self, message):
            message = message.lower()
            #Remove links 
            message = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                            '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', message)
            # Remove extra spaces 
            message = re.sub(' +', ' ', message)
            # Remove mentions 
            message =re.sub("(@[A-Za-z0-9_]+)","", message)
            # Remove Hashtags
            message = re.sub('#[A-Za-z0-9_]+','', message)
            # Remove all non alphanumeric characters 
            message = re.sub("^[A-Za-z0-9_-]*$", "", message)
            # Remove Emojis 
            emoji_pattern = re.compile(
                "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                "]+",
                flags=re.UNICODE,
            )
            message = emoji_pattern.sub('',message)
            if self.method == 'WordNetLemmatizer':
                message = ' '.join([self.stemmer.lemmatize(word) for word in message.split() if word not in self.moreStopWords])
            else:
                message = ' '.join([self.stemmer.stem(word) for word in message.split() if word not in self.moreStopWords])
            return message 
        def fit(self,X,y=None):
            self.vectorizer.fit(X)
            if y is not None:
                self.encoder.fit(y)
            self.isFitted=True
        def transform(self, X, y=None):
            if not self.isFitted:
                raise NotImplementedError('Please fit first by calling the fit function')
            X = self.vectorizer.transform(X)
            if y is not None:
                y = self.encoder.transform(y)
                return X,y
            else:
                return X 
        def fit_transform(self,X,y=None):
            self.fit(X,y)
            X,y = self.transform(X,y)
            return X,y
    main()
