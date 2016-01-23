Datumbox-Python-Wrapper
=======================

The Datumbox API provides a number of Remote Procedure Calls for Text Analysis and Natural Language Processing. This repo provides an easy way to use the API when writting Python.

You'll need an API key which you can get from the [Datumbox Site](http://www.datumbox.com/)


##Examples##

###Twitter Sentiment Analysis
```python 
>>> from DatumBox import DatumBox
>>> datum_box = DatumBox(API_KEY)
>>> datum_box.twitter_sentiment_analysis("I love my cat")
u'positive'

```
Text given to the classification methods should not contain HTML tags, the text_extract method provides an easy way to remove HTML tags (But involves a remote procedure call which may be undesirable)

##Exceptions that can be raised##
The wrapper will throw DatumBoxError if the API returns an error. Page 11 of the [API Documentation](http://www.datumbox.com/files/API-Documentation-1.0v.pdf) shows you possible Error Codes / Messages


The wrapper uses [urllib2](http://docs.python.org/2/library/urllib2.html) to make the remote procedure calls so you can handle any exceptions this can raise if you wish.

##Failing Tests##
Many of the classification tasks the Datumbox attempts to solve are [AI-Complete](http://en.wikipedia.org/wiki/AI-complete) this means that the results returned by the API are heuristic. Specifically the Readabilty Assesment and Commercial Detection tests I wrote fail as the API returns the wrong result, this should not be taken as a weakness of the API but rather the state of NLP in general.
