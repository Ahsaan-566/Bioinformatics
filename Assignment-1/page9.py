from pprint import pprint

string = 'attgtgtaaaaa'
kmear = 3
count = []
count.append([])
count[0].append('kmears')
count[0].append('number')

def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c in sublist:
            return i
    return -1

for i in range(len(string)-kmear+1):
	k =  string[i:i+kmear]


	a = in_list(k , count)
	if a!=-1:
		count[a][1] =  count[a][1]+1 
	else:
		count.append([])
		print len(count)
		count[len(count)-1].append(k)
		count[len(count)-1].append(1)


pprint(count)
