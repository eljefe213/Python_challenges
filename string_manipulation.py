# Exercice 1 : 
str1 = "Spam spam spam spam. Lovely spam! Wonderful spam! Spam spa-a-a-a-a-am..."
str2 = str1[21:25] 
print(str2) 

# Exercice 2 : 
str1 = "scrumptious"
i = 1
j = 6
str2 = str1[i:j]
print(str2) # Output: "crump"

# Exercice 3 :
str1 = "Unequivocal"
str2 = str1[2:]
print(str2)

# Exercice 4 : 
str1 = "Goldfish"
str2 = str1[:4]
print(str2)

# Exercice 5 :
sentence = "I like rocks but they seem indifferent."
conjunction_index = sentence.find("but")
left_side = sentence[0:conjunction_index] 
right_side = sentence[conjunction_index + 3:]
classy_sentence = left_side + "yet" + right_side
print(classy_sentence)

