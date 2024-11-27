s = "Python rules!"
S = s.upper()
index = s.find("rules")
S_ques = S.replace("!","?")
print(f"Uppercase: {S}\nLocation: {index}\nReplaced: {S_ques}")
