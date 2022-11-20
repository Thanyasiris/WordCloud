# WordCloud

WordCloud is a Fianal Project in Big Data Subject, Computer Science Year 3, KMITL.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all

```bash
pip install -r requirements.txt
```
or
```bash
pip install Eel
pip install textblob
pip install matplotlib
pip install pandas
pip install wordcloud
pip install langdetect
pip install pycountry
pip install sklearn
pip install scikit-learn
pip install tweepy
pip install python-dotenv
pip install pymongo
```
if cannot install try to use [Anaconda Prompt](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

### import nltk to avoid error then run it and remove it later
import nltk
nltk.download('vader_lexicon')
```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

## Require
- `.env` ( Variables that contains the user credentials to access Twitter API )

## Run UI
```
python main.py
```

## Run Select Sentiment ver.
```
python sentiment.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
