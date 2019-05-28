verbs = None
with open("Hangman/verbs.txt", "r") as verbs_file:
	verbs = verbs_file.read().split("\n")

new = ""	

#for verb in verbs:
#	new += verb.split(" -> ")[1].split(",")[0] + "\n"
	
#for verb in verbs:
#	if verb[len(verb) - 1] == "s":
#		new += verb + "\n"
		
for verb in verbs:
	if len(verb) <= 5:
		new += verb + "\n"
	
print(new)