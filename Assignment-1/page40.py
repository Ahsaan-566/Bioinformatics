from pprint import pprint

string = 'aaaaggggttttcctcgta'
kmear = 3
count = []
temp_count = -1

for a in 'acgt':	
	for b in 'acgt':
		for c in 'acgt':
			d = a+b+c
			temp_count = temp_count + 1
			count.append([])
			count[temp_count].append(d)
			count[temp_count].append(0)




def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c in sublist:
            return i
    return -1

for i in range(len(string)-kmear+1):
	k =  string[i:i+3]
	a = in_list(k , count)
	count[a][1] =  count[a][1]+1 


pprint(count)



