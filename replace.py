# Exercice 1 :
forecast = "It will be rainy today."
new_forecast = forecast.replace("rainy", "sunny") 
print(forecast) # Original forecast
print(new_forecast) # New forecast 

# Exercice 2 : 
test_string = "The replacement will be arriving shortly"
new_string = test_string.replace("shortly", "now")

print(test_string)
print(new_string)

# Exercice 3 : 
old_string = "the old string"
new_string = old_string.replace("old", "new")

print(old_string)
print(new_string)

print("We replaced " + old_string + " with " + new_string)

# Exercice 4 : 
words = "red fish"
words.replace("red", "blue") # this sentence will be lost
print(words)
print(words.replace("red", "blue"))

