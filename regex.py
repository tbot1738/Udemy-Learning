import re


string = "Hmmm, ig this works ? my email is noob_bot@gmail.com"
pattern = re.compile(r"[a-z A-Z]")
searched = pattern.match(string)
print(searched)
