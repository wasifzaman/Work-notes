
out = ''

for i in range(1, 10):
	out += 'LCCS-LAB-00'
	out += str(i)
	out += ','

for i in range(10, 47):
	out += 'LCCS-LAB-0'
	out += str(i)
	out += ','

print(out)


'''
f = open('loop_input.txt', 'r')
out = []
for line in f:
	out.append(line.strip())

out_ = ''
for i in out:
	out_ += '"' + i + '"'
	out_ += ','

print(out_)
'''