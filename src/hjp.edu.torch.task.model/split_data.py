import os
import codecs

DATA_DIR = '/Users/hjp/Downloads/task1_EI_oc/anger/'
TRAIN_FILE = 'anger_train1.txt'
TEST_FILE = 'anger_dev1.txt'
TRAID_DIR = 'train_txt'
TEST_DIR = 'test_txt'

if __name__=='__main__':
    train_file = []
    #fp = open(os.path.join(DATA_DIR, TRAIN_FILE), 'r')
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
            print(os.path.join(DATA_DIR+TRAID_DIR, filename))
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
    test_label = []
    test_file = []
    with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
        for lines in fp:
            label = lines.split()[0].strip()
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

