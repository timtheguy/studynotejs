from DatumBox import DatumBox
API_KEY = "454ec357b72e7d0c06cac8df90bb8862"
datum_box = DatumBox(API_KEY)
print datum_box.twitter_sentiment_analysis("I love my cat")