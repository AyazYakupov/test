f = open('input.txt')
text = f.readline()
d = {}
for line in f:
    words = line.strip().split(' - ')
    en = words[0]
    lat = words[1].split(', ')
    for key in lat:
        if key in d:
            d[key].append(en)
        else: d[key] = [en]
f.close

for key in d:
    d[key].sort()

g = open('output.txt', 'w')
g.write(str(len(d)) + '\n')
for lat in d:
    g.write(lat + ' - ' + ', '.join(d[lat])+ '\n')

g.close
