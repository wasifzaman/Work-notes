f_in = open('safesquid_whitelist.txt', 'r')
f_out = open('safesquid_cleaned.txt', 'w')
s = f_in.read()

s_split = [i for i in s.split('|')]
s_slash_removed = [i.replace('\\', '') for  i in s_split]
print(s_slash_removed)

for i in s_slash_removed:
	f_out.write(i + '\n')