from DatumBox import DatumBox
API_KEY = "454ec357b72e7d0c06cac8df90bb8862"
datum_box = DatumBox(API_KEY)
print datum_box.topic_classification("The three key principles in designing the language were reliability, efficiency, and machine-independence. The language is designed to allow aerospace-related tasks (such as vector/matrix arithmetic) to be accomplished in a way that is easily understandable by people who have spaceflight knowledge, but may not necessarily have proficiency with computer programming.")