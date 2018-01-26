import os
import codecs

from nltk.tokenize import word_tokenize

DATA_DIR = '/Users/hjp/Downloads/semeval/task1b_en/fear/data/'
TRAIN_FILE = 'fear_train.txt'
DEV_FILE = 'fear_dev.txt'
TEST_FILE = 'fear_test.txt'
TRAID_DIR = 'train_txt'
DEV_DIR = 'dev_txt'
TEST_DIR = 'test_txt'



def data_split():
    train_file = []
    labels = {}
    count = 0
    train_label = []
    train_file = []
    with open(os.path.join(DATA_DIR, TRAIN_FILE), encoding='utf-8') as fp:
        for lines in fp:
            label = lines.split()[0].strip()
            txt = lines.replace(label, '')
            if label not in labels:
                labels[label] = len(labels)
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            #print(os.path.join(DATA_DIR+TRAID_DIR, filename))
            fp_train = codecs.open(os.path.join(DATA_DIR+TRAID_DIR, filename), 'a+', 'utf-8')
            train_file.append(filename)
            fp_train.write(txt)
            fp_train.close()
            # record #count label
            train_label.append(labels[label])
    fp_file = codecs.open(DATA_DIR+'train_txt.txt', 'a+', 'utf-8')
    for file in train_file:
        fp_file.write(file + '\n')
    fp_file.close()
    fp_label = codecs.open(DATA_DIR+'train_label.txt', 'a+', 'utf-8')
    for t in train_label:
        fp_label.write(str(t) + '\n')
    fp_label.close()

    fp.close()
    print(labels)
    #with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
    #fp = open(os.path.join(DATA_DIR, TEST_FILE), 'r')
    
    
    
    count = 0
    dev_label = []
    dev_file = []
    with open(os.path.join(DATA_DIR, DEV_FILE), encoding='utf-8') as fp:
        for lines in fp:
            label = lines.split()[0].strip()
            txt = lines.replace(label, '')
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            fp_dev = codecs.open(os.path.join(DATA_DIR+DEV_DIR, filename), 'a+', 'utf-8')
            #fp_test = open(os.path.join(TEST_DIR, filename), 'wb')
            dev_file.append(filename)
            fp_dev.write(txt)
            fp_dev.close()
            # record #count label
            dev_label.append(labels[label])
        fp_file = codecs.open(DATA_DIR+'dev_txt.txt', 'a+', 'utf-8')
        for file in dev_file:
            fp_file.write(file + '\n')
        fp_file.close()
    
        fp_label = codecs.open(DATA_DIR+'dev_label.txt', 'a+', 'utf-8')
        for t in dev_label:
            fp_label.write(str(t) + '\n')
        fp_label.close()    
        fp.close()
    
    
    
    
    count = 0
    test_label = []
    test_file = []
    with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
        for lines in fp:
            print(lines)
            label = lines.split()[0].strip()
            print(label)
            txt = lines.replace(label, '')
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            fp_test = codecs.open(os.path.join(DATA_DIR+TEST_DIR, filename), 'a+', 'utf-8')
            #fp_test = open(os.path.join(TEST_DIR, filename), 'wb')
            test_file.append(filename)
            fp_test.write(txt)
            fp_test.close()
            # record #count label
            test_label.append(labels[label])
        fp_file = codecs.open(DATA_DIR+'test_txt.txt', 'a+', 'utf-8')
        for file in test_file:
            fp_file.write(file + '\n')
        fp_file.close()
    
        fp_label = codecs.open(DATA_DIR+'test_label.txt', 'a+', 'utf-8')
        for t in test_label:
            fp_label.write(str(t) + '\n')
        fp_label.close()    
        fp.close()
        
def semeval_data(srcFile, tarFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
    tweet_length = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" not in line:
                print(line)
                sents = line.split('\t')
                #print(sents[1] + "\t" + sents[3])
                print(sents[3][0:1])
                tokens = word_tokenize(sents[1])
                strline = ""
                for i in range(len(tokens)):
                    if len(strline) == 0:
                        strline = tokens[i]
                    else:
                        strline = strline + " " + tokens[i]
                print(sents[3][0:1] + "\t" + strline )
                #strline = strline.replace("\\n", "")
                wrtFile.write(sents[3][0:1] + "\t" + strline + "\n")
                if len(tokens) > tweet_length:
                    tweet_length = len(tokens)
                print(word_tokenize(sents[1]))
    print(tweet_length)
    
def semeval_test(srcFile, tarFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
    tweet_length = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" not in line:
                print(line)
                sents = line.split('\t')
                print(sents[1] + "\t" + sents[3])
                print(sents[3])
                tokens = word_tokenize(sents[1])
                strline = ""
                for i in range(len(tokens)):
                    if len(strline) == 0:
                        strline = tokens[i]
                    else:
                        strline = strline + " " + tokens[i]
                print("0\t" + strline )
                #strline = strline.replace("\\n", "")
                wrtFile.write("0\t" + strline + "\n")
                if len(tokens) > tweet_length:
                    tweet_length = len(tokens)
                print(word_tokenize(sents[1]))
    print(tweet_length)
    
    
def semeval_pred(srcFile, preFile, subFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(subFile, 'a+', 'utf-8') 
    score = []
    with open(preFile, encoding='utf-8') as f:
        for line in f:
            score.append(line.strip())
            
    #tweet_length = 0
    index = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" in line:
                wrtFile.write(line)
            else:
                if score[index] == '0':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t0: no anger can be inferred\n')
                elif score[index] == '1':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t1: low amount of anger can be inferred\n')
                elif score[index] == '2':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t2: moderate amount of anger can be inferred\n')
                else:
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t3: high amount of anger can be inferred\n')
                index += 1
        
        
def main():
    train_srcFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear-train.txt"
    train_tarFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear_train.txt"
    dev_srcFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear-dev.txt"
    dev_tarFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear_dev.txt"
    test_srcFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear-test.txt"
    test_tarFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear_test.txt"
    test_preFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/fear_pred.txt"
    test_subFile = "/Users/hjp/Downloads/semeval/task1b_en/fear/src/EI-oc_en_fear_pred.txt"
    #semeval_data(train_srcFile, train_tarFile)
    #semeval_data(dev_srcFile, dev_tarFile)
    #semeval_test(test_srcFile, test_tarFile)
    data_split()
    #semeval_pred(test_srcFile, test_preFile, test_subFile)


if __name__ == "__main__":
    main()
