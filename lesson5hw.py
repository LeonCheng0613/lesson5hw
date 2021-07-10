s = []
si = int(input('How many students are in this class? Answer : '))
si2 = si
sch = 0
while si >= 1:
    cs = input('score : ')
    cs = int(cs)
    s.append(cs)
    si = si - 1

s2 = max(s)
s3 = min(s)
s = sum(s)
s = s / si2
print('The averege of the', str(si2), 'is', str(s), '.', 'The highest of the', str(si2), 'scores is', str(s2) + 'and the lowest score among them is', str(s3) + '.')