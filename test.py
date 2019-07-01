import nltk
from nltk import word_tokenize
nltk.download('punkt')

pcorpus = dict()
pcorpus1 = dict()
lines_lang1 = open("data_lang1.txt", "r").readlines()
lines_lang2 = open("data_lang2.txt", "r").readlines()

for line1, line2 in zip(lines_lang1, lines_lang2):
    sentence1 = tuple(word_tokenize("NULL " + line1.strip("\n")))
    sentence2 = tuple(word_tokenize("NULL " + line2.strip("\n")))
    pcorpus[sentence1] = sentence2
    pcorpus1[sentence2] = sentence1
print (pcorpus)

#dic word2:{word1:probability}
dic={}
for i in pcorpus1.keys():
    for j in i:
        dic[j]={}

for i in pcorpus1.keys():
    for j in i:
        for t in pcorpus1[i]:
            dic[j][t]=0
        
for sen in pcorpus1.keys():
    for word in sen:
        for trans in pcorpus1[sen]:
            dic[word][trans]+=1

for l2 in dic.keys():
    s=0
    for l1 in dic[l2]:
        s+=dic[l2][l1]
    for l1 in dic[l2]:
        dic[l2][l1]=round(dic[l2][l1]/s,2)
print(dic)

#translation_probs word1:{word2:probability}

translation_probs = {}
for i in dic.keys():
    for j in dic[i]:
        translation_probs[j]={}
for i in dic.keys():
    for j in dic[i]:
        translation_probs[j][i]=0
for i in dic.keys():
    for j in dic[i]:
        translation_probs[j][i]=dic[i][j]

print(translation_probs["ok-voon"])
#{'NULL': 0.04, 'at-voon': 0.19, 'bichat': 0.08, 'dat': 0.07, 'at-drubel': 0.17, 'pippat': 0.11, 'rrat': 0.08, 'krat': 0.08, 'sat': 0.17, 'lat': 0.08}

num_epochs = 1
#for i in range(num_epochs):