from DatumBox import DatumBox
API_KEY = "454ec357b72e7d0c06cac8df90bb8862"
PASSED_STRING = "This is an test string"
tags = [] 
keywordlist = []
datum_box = DatumBox(API_KEY)
tags.append(datum_box.topic_classification(PASSED_STRING))
if datum_box.is_educational(PASSED_STRING):
	tags.append("Educational")
elif datum_box.is_educational(PASSED_STRING)!=True:
	tags.append("Not Educational")
tags.append(datum_box.readability_assessment(PASSED_STRING))
list = datum_box.keyword_extract(PASSED_STRING)
for m in list:
    tags.append(m)
for n in tags:
    if n == ("time" or "person" or "year" or "way" or "day" or "thing" or "man" or "world" or "life" or "hand" or "part" or "child" or "eye" or "woman" or "place" or "work" or "week" or "case" or "point" or "man" or "company" or "group" or "problem" or "fact" or "be" or "have" or "do" or "say" or "get" or "make" or "go" or "know" or "take" or "see" or "come" or "think" or "look" or "want" or "give" or "use" or "find" or "tell" or "ask" or "work" or "seem" or "feel" or "try" or "leave" or "call" or "good" or "new" or "first" or "last" or "long" or "great" or "little" or "own" or "other" or "old" or "right" or "big" or "high" or "different" or "small" or "large" or "next" or "early" or "young" or "important" or "few" or "public" or "bad" or "same" or "able" or "to" or "of" or "in" or "for" or "on" or "with" or "at" or "by" or "from" or "up" or "about" or "into" or "over" or "after" or "beneath" or "under" or "above" or "the" or "and" or "a" or "that" or "I" or "it" or "not" or "he" or "as" or "you" or "this" or "but" or "his" or "they" or "her" or "she" or "or" or "an" or "will" or "my" or "one" or "all" or "would" or "there" or "their"):
        tags.remove(n)
for item in tags:
    print item