'''
out = ''

for i in range(1, 10):
	out += 'shutdown /r /m \\\LCCS-LAB-00'
	out += str(i)
	out += '\n'

for i in range(10, 47):
	out += 'shutdown /r /m \\\LCCS-LAB-0'
	out += str(i)
	out += '\n'

print(out)
'''

#'''
f = open('loop_input.txt', 'r')
out = []
for line in f:
	out.append(line.strip())

out_ = ''
for i in out:
	out_ += 'shutdown /s /m \\\\' + i + ''
	out_ += '\n'

print(out_)
#'''