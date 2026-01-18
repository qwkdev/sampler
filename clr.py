import colorsys
from collections import defaultdict

data = '''
#616161
#B3B3B3
#DDDDDD
#FFFFFF
#FFB3B3
#FF6161
#DD6161
#B36161

#FFF3D5
#FFB361
#DD8C61
#B37661
#FFEEA1
#FFFF61
#DDDD61
#B3B361

#DDFFA1
#C2FF61
#A1DD61
#81B361
#C2FFB3
#61FF61
#61DD61
#61B361

#C2FFC2
#61FF8C
#61DD76
#61B36B
#C2FFCC
#61FFCC
#61DDA1
#61B381

#C2FFF3
#61FFE9
#61DDC2
#61B396
#C2F3FF
#61EEFF
#61C7DD
#61A1B3

#C2DDFF
#61C7FF
#61A1DD
#6181B3
#A18CFF
#6161FF
#6161DD
#6161B3

#CCB3FF
#A161FF
#8161DD
#7661B3
#FFB3FF
#FF61FF
#DD61DD
#B361B3

#FFB3D5
#FF61C2
#DD61A1
#B3618C
#FF7661
#E9B361
#DDC261
#A1A161

#61B361
#61B38C
#618CD5
#6161FF
#61B3B3
#8C61F3
#CCB3C2
#8C7681

#FF6161
#F3FFA1
#EEFC61
#CCFF61
#76DD61
#61FFCC
#61E9FF
#61A1FF

#8C61FF
#CC61FC
#EE8CDD
#A17661
#FFA161
#DDF961
#D5FF8C
#61FF61

#B3FFA1
#CCFCD5
#B3FFF6
#CCE4FF
#A1C2F6
#D5C2F9
#F98CFF
#FF61CC

#FFC261
#F3EE61
#E4FF61
#DDCC61
#B3A161
#61BA76
#76C28C
#8181A1

#818CCC
#CCAA81
#DD6161
#F9B3A1
#F9BA76
#FFF38C
#E9F9A1
#D5EE76

#8181A1
#F9F9D5
#DDFCE4
#E9E9FF
#E4D5FF
#B3B3B3
#D5D5D5
#F9FFFF

#E96161
#AA6161
#81F661
#61B361
#F3EE61
#B3A161
#EEC261
#C27661
'''

data = [i.strip() for i in data.split('\n') if i.strip()]

def torgb(clr) -> tuple[int, int, int]:
	clr = clr.lstrip('#')
	return tuple(int(clr[i:i+2], 16) for i in (0, 2, 4))

def tohsv(clr) -> tuple[float, float, float]:
	return colorsys.rgb_to_hsv(*(i/255 for i in torgb(clr)))

def out(clr):
	if not clr:
		return '<button class="colour empty"></button>'
	return f'<button class="colour" data-value="{data.index(clr)}" style="--clr: {clr.lower()}"></button>'

# s = sorted(data, key=lambda c: lab(c))
# for clr in s:
# 	print(out(clr))

r = [[] for _ in range(8)]
for n, c in enumerate(data):
	r[(n%8)%8].append(c)
for i in r:
	for j in i:
		print(out(j))
exit()


BANDS = 128
cols = [[] for _ in range(BANDS)]
for c in data:
	h, s, v = tohsv(c)
	if s <= 0.25:
		b = BANDS-1
	else:
		b = min(BANDS-2, round(h * (BANDS-1)))
	cols[b].append((h, v**3, c))

lb = 0
for b in cols:
	if lb < len(b):
		lb = len(b)

cols2 = []
for n, band in enumerate(cols):
	cols2.append(([i[-1] for i in sorted(band, key=(lambda x: x[0]) if n == len(cols)-1 else (lambda x: x[1]))] + ['']*lb)[:lb])

output = []
for i in cols2:
	for c in i:
		if c:
			output.append(out(c))

split = 8
output = [output[i:i+split] for i in range(0, len(output), split)]
output = list(map(list, zip(*output)))
for col in output:
	for item in col:
		print(item)