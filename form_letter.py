form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution." 
# Write Emily a letter
form_letter = form_letter.replace("[Insert Name Here]", "Emily")
# form_letter now saves Emily as the name
print(form_letter)
# This doesn't find a match
form_letter = form_letter.replace("[Insert Name Here]", "Josh")
# Prints the same form_letter as before
print(form_letter)

# Print personnalised letter for each person 
form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution." 
# Write Emily a letter
emily_letter = form_letter.replace("[Insert Name Here]", "Emily")
# Save as new variable
print(emily_letter)
# Write Josh a letter
josh_letter = form_letter.replace("[Insert Name Here]", "Josh")
# Saved as a new letter
print(josh_letter)
