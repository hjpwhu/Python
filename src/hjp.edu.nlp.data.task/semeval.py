import codecs

f = codecs.open("/Users/hjp/Downloads/task/data/dev.txt", 'r', 'utf-8')

for line in f.readlines():
    print(line)
    sents = line.split('\t')
    print(sents[1] + "\t" + sents[3])
    for i in range(len(sents)):
        print(sents[i])
    
f.close()
