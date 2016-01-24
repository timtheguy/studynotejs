from DatumBox import DatumBox
API_KEY = "454ec357b72e7d0c06cac8df90bb8862"
PASSED_STRING = raw_input("Enter the string to analyze:")
tags = []
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
    if n == ("time") or n == ("person") or n == ("year") or n == ("way") or n == ("day") or n == ("thing") or n == ("man")or n == ("world") or n == ("life") or n == ("hand") or n == ("part") or n == ("child") or n == ("eye") or n == ("woman") or n == ("place") or n == ("work") or n == ("week") or n == ("case") or n == ("point") or n == ("man") or n == ("company") or n == ("group")or n == ("problem") or n == ("fact") or n == ("be") or n == ("have") or n == ("do") or n == ("say") or n == ("get") or n == ("make") or n == ("go") or n == ("know") or n == ("take") or n == ("see") or n == ("come") or n == ("think") or n == ("look") or n == ("want") or n == ("give") or n == ("use") or n == ("find") or n == ("tell") or n == ("ask") or n == ("work") or n == ("seem") or n == ("feel") or n == ("try") or n == ("leave") or n == ("call") or n == ("good") or n == ("new") or n == ("first") or n == ("last") or n == ("long") or n == ("great") or n == ("little") or n == ("own") or n == ("other") or n == ("old") or n == ("right") or n == ("big") or n == ("high") or n == ("different") or n == ("small") or n == ("large") or n == ("next") or n == ("early") or n == ("young") or n == ("important") or n == ("few") or n == ("public") or n == ("bad")or n == ("same") or n == ("able") or n == ("to") or n == ("of") or n == ("in") or n == ("for") or n == ("on") or n == ("with") or n == ("at") or n == ("by") or n == ("from") or n == ("up") or n == ("about") or n == ("into") or n == ("over") or n == ("after") or n == ("beneath") or n == ("under") or n == ("above") or n == ("the") or n == ("and") or n == ("a") or n == ("that") or n == ("I") or n == ("it") or n == ("not") or n == ("he") or n == ("as") or n == ("you") or n == ("this") or n == ("but") or n == ("his") or n == ("they") or n == ("her") or n == ("she") or n == ("or") or n == ("an") or n == ("will") or n == ("my") or n == ("one") or n == ("all") or n == ("would") or n == ("there") or n == ("their") or n == ("is") or n == ("a") or n == ("b") or n == ("c") or n == ("d") or n == ("e") or n == ("f") or n == ("g") or n == ("h") or n == ("i") or n == ("j") or n == ("k") or n == ("l") or n == ("m") or n == ("n") or n == ("o") or n == ("p") or n == ("q") or n == ("r") or n == ("s") or n == ("t") or n == ("u") or n == ("v") or n == ("w") or n == ("x") or n == ("y") or n == ("z"):
        tags.remove(n) # if statement simplifies to n == "time". Pull each item into a list, loop over list, test each item individually
for item in tags:
    print item
