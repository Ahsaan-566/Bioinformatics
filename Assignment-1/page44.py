from pprint import pprint

#pattern = 'ac'


def symboltoindex(symbol):
    if symbol == 'a':
        return 0
    elif symbol == 'c':
        return 1
    elif symbol == 'g':
        return 2
    elif symbol == 't':
        return 3


def indextosymbol(number):
    if number == 0:
        return 'a'
    elif number == 1:
        return 'c'
    elif number == 2:
        return 'g'
    elif number == 3:
        return 't'


def patterntonumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:len(pattern) - 1]
    return 4 * patterntonumber(prefix) + symboltoindex(symbol)

print patterntonumber('aatcg')

def numbertopattern(index, k):
    if k == 1:
        return indextosymbol(index)
    prefixIndex = index / 4
    remainder = index % 4
    symbol = indextosymbol(remainder)
    prefixpattern = numbertopattern(prefixIndex, k - 1)
    return prefixpattern + symbol


# print numbertopattern(1,3)

text = 'acttggggcagaagt'


def findingfrequentwordsbysorting(text, k):
    frequentpatterns = []
    temp = []

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        index = patterntonumber(pattern)
        count = 1;
        temp.append([pattern, index, count])
    temp.sort(key=lambda x: x[1])

    for i in range(len(text) - k):
        if temp[i][1] == temp[i + 1][1]:
            temp[i + 1][2] = temp[i][2] + 1
    max_index = max(temp, key=lambda x:x[2])

    for i in range(len(text)-k+1):
        if temp[i][2]== max_index[2]:
            pattern = numbertopattern(temp[i][1],k)
            frequentpatterns.append(pattern)

    temp.insert(0, ['kmear', 'index', 'count'])
    pprint(temp)
    return frequentpatterns


temp = findingfrequentwordsbysorting(text,3);
print
print("Most frequent kmear is")
pprint(temp)