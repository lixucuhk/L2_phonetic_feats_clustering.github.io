import random
import os

def extract_phn_IPA_wavfiles(clusternum):
	phnIPAs = []
	wavfiles = []
	senids = []
	for file in os.listdir('./'+clusternum):
		if '.phn' in file:
			senids.append(file[:-4])
	random.shuffle(senids)
	for senid in senids[:3]:
		temrfile = open('./'+clusternum+'/'+senid+'.phn', 'r')
		text = temrfile.readline()
		text = text[:-1]+'('
		temrfile.close()
		temrfile = open('./'+clusternum+'/'+senid+'.IPA', 'r')
		text += temrfile.readline()[:-2]+')'
		phnIPAs.append(text)
		temrfile.close()
		wavfiles.append(clusternum+'/'+senid+'.wav')

	return phnIPAs, wavfiles

phn2IPA = {}
rfile = open('./phone2IPA.conf', 'r')
for line in rfile.readlines():
	phn, num, IPA = line.split()
	phn2IPA.update({phn:IPA})

rfile.close()

type2clusters = {}
rfile = open('./merged_clusters_mtype.txt', 'r')
for line in rfile.readlines():
	items = line.split()
	if line[0] == ' ':
		ptype = 'none'
		clusters = items
	else:
		ptype = items[0]
		clusters = items[1:]
	type2clusters.update({ptype:clusters})

rfile.close()

types = type2clusters.keys()

rfile = open('./index_template.html', 'r')
wfile = open('./index.html', 'w')

for line in rfile.readlines():
	wfile.write(line)

rfile.close()

# Case 1
types_subset = []
for item in types:
	if '_1' in item:
		types_subset.append(item)
types_subset.sort()
wfile.write('  <h3>Case 1 (native-like patterns)</h3>\n \
    <table border="1">\n \
      <tr>\n \
        <td align="center" > </td>\n \
        <td align="center" >Sample 1</td>\n \
        <td align="center" >Sample 2</td>\n \
        <td align="center" >Sample 3</td>\n \
      </tr>)\n')

for item in types_subset:
	ptype = item
	clusternum = type2clusters.get(ptype)[0]
	labels, files = extract_phn_IPA_wavfiles(clusternum)
	wfile.write('      <tr>\n')
	wfile.write('        <td align="center" rowspan="2" ><b>'+ptype+'</b></td>\n')
	for i in range(3):
		wfile.write('        <td align="center" >\n \
          <audio controls>\n \
          <source src="'+files[i]+'" type="audio/wav">\n \
          </audio>\n \
        </td>\n')

	wfile.write('      </tr>\n')
	wfile.write('      <tr>\n')
	for i in range(3):
		wfile.write('        <td align="center" >'+labels[i]+'</td>\n')
	wfile.write('      </tr>\n')

# Case 2
types_subset = []
for item in types:
	if '_2' in item and ',' not in item:
		types_subset.append(item)
types_subset.sort()
wfile.write('  <h3>Case 2 (sounds like a native pattern, but there is a small deviation)</h3>\n \
    <table border="1">\n \
      <tr>\n \
        <td align="center" > </td>\n \
        <td align="center" >Sample 1</td>\n \
        <td align="center" >Sample 2</td>\n \
        <td align="center" >Sample 3</td>\n \
      </tr>)\n')

for item in types_subset:
	ptype = item
	clusternum = type2clusters.get(ptype)[0]
	labels, files = extract_phn_IPA_wavfiles(clusternum)
	wfile.write('      <tr>\n')
	wfile.write('        <td align="center" rowspan="2" ><b>'+ptype+'</b></td>\n')
	for i in range(3):
		wfile.write('        <td align="center" >\n \
          <audio controls>\n \
          <source src="'+files[i]+'" type="audio/wav">\n \
          </audio>\n \
        </td>\n')
	wfile.write('      </tr>\n')
	wfile.write('      <tr>\n')
	for i in range(3):
		wfile.write('        <td align="center" >'+labels[i]+'</td>\n')
	wfile.write('      </tr>\n')

# Case 3
types_subset = []
for item in types:
	if '_2' in item and ',' in item:
		types_subset.append(item)
types_subset.sort()
wfile.write('  <h3>Case 3 (sounds like more than one native pattern)</h3>\n \
    <table border="1">\n \
      <tr>\n \
        <td align="center" > </td>\n \
        <td align="center" >Sample 1</td>\n \
        <td align="center" >Sample 2</td>\n \
        <td align="center" >Sample 3</td>\n \
      </tr>)\n')

for item in types_subset:
	ptype = item
	clusternum = type2clusters.get(ptype)[0]
	labels, files = extract_phn_IPA_wavfiles(clusternum)
	wfile.write('      <tr>\n')
	wfile.write('        <td align="center" rowspan="2" ><b>'+ptype+'</b></td>\n')
	for i in range(3):
		wfile.write('        <td align="center" >\n \
          <audio controls>\n \
          <source src="'+files[i]+'" type="audio/wav">\n \
          </audio>\n \
        </td>\n')
	wfile.write('      </tr>\n')
	wfile.write('      <tr>\n')
	for i in range(3):
		wfile.write('        <td align="center" >'+labels[i]+'</td>\n')
	wfile.write('      </tr>\n')

# Case 4
types_subset = []
for item in types:
	if '_3' in item:
		types_subset.append(item)
types_subset.sort()
wfile.write('  <h3>Case 4 (large deviation from a native pattern)</h3>\n \
    <table border="1">\n \
      <tr>\n \
        <td align="center" > </td>\n \
        <td align="center" >Sample 1</td>\n \
        <td align="center" >Sample 2</td>\n \
        <td align="center" >Sample 3</td>\n \
      </tr>)\n')

for item in types_subset:
	ptype = item
	clusternum = type2clusters.get(ptype)[0]
	labels, files = extract_phn_IPA_wavfiles(clusternum)
	wfile.write('      <tr>\n')
	wfile.write('        <td align="center" rowspan="2" ><b>'+ptype+'</b></td>\n')
	for i in range(3):
		wfile.write('        <td align="center" >\n \
          <audio controls>\n \
          <source src="'+files[i]+'" type="audio/wav">\n \
          </audio>\n \
        </td>\n')
	wfile.write('      </tr>\n')
	wfile.write('      <tr>\n')
	for i in range(3):
		wfile.write('        <td align="center" >'+labels[i]+'</td>\n')
	wfile.write('      </tr>\n')

# Case 5
types_subset = []
for item in types:
	if 'none' in item:
		types_subset.append(item)
types_subset.sort()
wfile.write('  <h3>Case 5 (far away from all native patterns)</h3>\n \
    <table border="1">\n \
      <tr>\n \
        <td align="center" > </td>\n \
        <td align="center" >Sample 1</td>\n \
        <td align="center" >Sample 2</td>\n \
        <td align="center" >Sample 3</td>\n \
      </tr>)\n')

for item in types_subset:
	ptype = item
	clusternum = type2clusters.get(ptype)[0]
	labels, files = extract_phn_IPA_wavfiles(clusternum)
	wfile.write('      <tr>\n')
	wfile.write('        <td align="center" rowspan="2" ><b>'+ptype+'</b></td>\n')
	for i in range(3):
		wfile.write('        <td align="center" >\n \
          <audio controls>\n \
          <source src="'+files[i]+'" type="audio/wav">\n \
          </audio>\n \
        </td>\n')
	wfile.write('      </tr>\n')
	wfile.write('      <tr>\n')
	for i in range(3):
		wfile.write('        <td align="center" >'+labels[i]+'</td>\n')
	wfile.write('      </tr>\n')

wfile.write('    </table>\n \
  </div>\n \
</body>\n \
</html>\n')

wfile.close()
