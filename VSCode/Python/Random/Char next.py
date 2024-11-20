alpha_s = 'abcdefghijklmnopqrstuvwxyz' 
alpha_c = alpha_s.upper() 
dict1 = dict(zip(alpha_s, alpha_s[1:] + alpha_s[:1])) 
dict2 = dict(zip(alpha_c, alpha_c[1:] + alpha_c[:1])) 
     
dict1.update(dict2) 
     
input_text2 = "One Flew Over the Cuckoo's Net" 
     
output_text2 = '' 
for c in input_text2 : 
	output_text2 += dict1.get(c, c) 
     
print(output_text2) 