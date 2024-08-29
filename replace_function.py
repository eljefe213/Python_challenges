sentence = "a breakfast for billy the bee is an early egg"

#sentence = sentence.replace("e", "a")
sentence = sentence.replace("e", "@")
#sentence = sentence.replace("a", "b")
sentence = sentence.replace("a", "e")
sentence = sentence.replace("@", "a")
#sentence = sentence.replace("b", "e")

print(sentence)
