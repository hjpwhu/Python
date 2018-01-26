import os
import sys
import math
import time
import codecs
import random
import argparse
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import init
import torch.autograd as autograd
from torch.autograd import Variable
from random import shuffle


parser = argparse.ArgumentParser()
parser.add_argument('--word_dim', dest='word_dim', type=int, help='word embedding dimension', default=20)
parser.add_argument('--hid_size', dest='hid_size', type=int, help='hidden dimension size', default=50)
parser.add_argument('--enc_size', dest='enc_size', type=int, help='encode dimension size', default=10)
parser.add_argument('--epochs', dest='epochs', type=int, help='epochs for model training', default=10)
parser.add_argument('--learning_rate', dest='learning_rate', type=float, help='learning_rate', default=5e-3)
parser.add_argument('--init_weight', dest='init_weight', type=float, help='initial weight for OOV', default=5e-1)
parser.add_argument('--seed', dest='seed', type=int, help='random seed', default=2718281828)
parser.add_argument('--emb_file', dest='emb_file', type=str, help='embedding file', default='/Volumes/SANDISK/Workshop/Corpus/bin/text.txt')
parser.add_argument('--data_file', dest='data_file', type=str, help='data file', default='/Volumes/SANDISK/Workshop/Corpus/imdb/tmp')


args = parser.parse_args()
torch.manual_seed(args.seed)
use_gpu = torch.cuda.is_available()
print(args)


class RVAE(nn.Module):
    def __init__(self, word_dim, hid_size, enc_size):
        super(RVAE, self).__init__()
        
        self.WeC2P = nn.Linear(2 * word_dim, word_dim)
        self.WeP2H = nn.Linear(word_dim, hid_size)
        self.WeH2H = nn.Linear(hid_size, hid_size)

        self.WeH2M = nn.Linear(hid_size, enc_size)
        self.WeH2D = nn.Linear(hid_size, enc_size)
        
        self.WdE2H = nn.Linear(enc_size, hid_size)
        self.WdH2H = nn.Linear(hid_size, hid_size)
        self.WdH2P = nn.Linear(hid_size, word_dim)
        self.WdP2C = nn.Linear(word_dim, 2 * word_dim)
        
        self.tanh = nn.Tanh()
        self.soft = nn.LogSoftmax()
        
    def encode(self, sent, node, size):
        parent = Variable(torch.FloatTensor(torch.randn(1, size)))
        
        for i in range(node):
            if i == 0:
                parent = sent[i]
            else: 
                parent = self.tanh(self.WeC2P(torch.cat((parent, sent[i]), 0)))
                
        hid_code = self.tanh(self.WeH2H(self.tanh(self.WeP2H(parent))))
        mu = self.tanh(self.WeH2M(hid_code))
        va = self.tanh(self.WeH2D(hid_code))

        return hid_code, mu, va
    
    def reparameterize(self, mu, logvar):
          std = logvar.mul(0.5).exp_()
          eps = Variable(std.data.new(std.size()).normal_())
          
          return eps.mul(std).add_(mu)
    
    def decode(self, code, node, size):
        sent = Variable(torch.FloatTensor(torch.randn(node, size)).zero_())
        
        parent = self.tanh(self.WdH2P(self.tanh(self.WdH2H(self.tanh(self.WdE2H(code))))))
        
        for i in range(node - 1): 
            if i < node - 2:           
                children = self.tanh(self.WdP2C(parent))
                sent[node - i - 1] = children[0:size]
                parent = children[size:]
            else:
                children = self.tanh(self.WdP2C(parent))
                sent[1] = children[0:size]
                sent[0] = children[size:]
        
        return sent
    
    def forward(self, sent):
        node = sent.size()[0]
        size = sent.size()[1]
        hi, mu, va = self.encode(sent, node, size)
        zc = self.reparameterize(mu, va)
        se = self.decode(zc, node, size)
        sc = self.soft(zc)
        return se, mu, va, sc    


def loss_function(recon_x, x, mu, logvar):
    mse = nn.MSELoss()
    mse_loss = mse(recon_x, x)

    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    return mse_loss + KLD
    

cel_criterion = nn.CrossEntropyLoss()
rvae = RVAE(args.word_dim, args.hid_size, args.enc_size)
optimizer = optim.Adam(rvae.parameters(), lr=args.learning_rate)


if use_gpu:
    rvae = rave.cuda()
    cel_criterion = cel_criterion.cuda()


def sentiment_corpus(srcFile, tarFile):
    wrtFile = codecs.open(tarFile, 'a+', 'utf-8')    
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            label = line[1:2]      
            sent = ""
            tokens = line.split()
            for i in range(len(tokens)):
                if ")" in tokens[i]:
                    words = tokens[i].split(')')
                    if "LRB" not in words[0] and "RRB" not in words[0] and "--" not in words[0]:
                        if len(sent) == 0:
                            sent = words[0]
                        else:
                            sent = sent + " " + words[0]
            sent = sent.replace("\/", " ")
            sent = sent.replace(" - ", " ")
            sent = sent.replace("\*", " ")
            sent = sent.replace("  ", " ")
            sent = sent.replace("  ", " ")
            toks = sent.split()
            if len(toks) > 4:
                wrtFile.write(label + "\t" + sent + "\n")
    wrtFile.close()    
    

def data():
    srcTrainFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/ssc/train.txt"
    tarTrainFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/tmp/train.txt"
    srcValidFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/ssc/valid.txt"
    tarValidFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/tmp/valid.txt"
    srcTestFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/ssc/test.txt"
    tarTestFile = "/Users/hjp/MacBook/Workspace/Workshop/Corpus/tmp/test.txt"
    
    sentiment_corpus(srcTrainFile, tarTrainFile)
    sentiment_corpus(srcValidFile, tarValidFile)
    sentiment_corpus(srcTestFile, tarTestFile)
    

def read_embedding():
    emb_voc, emb_vec = [], {}
    with open(args.emb_file, encoding='utf-8') as lines:
        for line in lines:
            tokens = line.split()
            if len(tokens) == (args.word_dim + 1):
                emb_voc.append(tokens[0])
                emb_vec[tokens[0]] = np.asarray(tokens[1:], dtype='float32')
        lines.close()
    return emb_voc, emb_vec


oov, voc = 0, 0


def build_embedding(ssc_voc, ssc_vec, line, emb_voc, emb_vec):
    global oov, voc
    tokens = line.split()
    
    for i in range(len(tokens)):
        if tokens[i] not in ssc_voc:
            voc += 1
            ssc_voc.append(tokens[i])
            if tokens[i] in emb_voc:
                ssc_vec[tokens[i]] = torch.from_numpy(emb_vec[tokens[i]]).view(1, args.word_dim)
            else:
                ssc_vec[tokens[i]] = init.normal(torch.Tensor(1, args.word_dim), 0, args.init_weight) 
                oov += 1
    return ssc_voc, ssc_vec   


def read_corpus(emb_voc, emb_vec):
    ssc_voc, ssc_vec = [], {}
    train_data, valid_data, test_data = [], [], []    
    assert os.path.exists(args.data_file)
    
    with open(os.path.join(args.data_file, 'train.txt'), encoding='utf-8') as lines:
        for line in lines:
            sents = line.lower().split('\t')
            train_data.append(sents[0] + "\t" + sents[1])
            ssc_voc, ssc_vec = build_embedding(ssc_voc, ssc_vec, sents[1], emb_voc, emb_vec)
                        
    with open(os.path.join(args.data_file, 'valid.txt'), encoding='utf-8') as lines:
        for line in lines:
            sents = line.lower().split('\t')
            valid_data.append(sents[0] + "\t" + sents[1])
            ssc_voc, ssc_vec = build_embedding(ssc_voc, ssc_vec, sents[1], emb_voc, emb_vec)
    
    with open(os.path.join(args.data_file, 'test.txt'), encoding='utf-8') as lines:
        for line in lines:
            sents = line.lower().split('\t')
            test_data.append(sents[0] + "\t" + sents[1])
            ssc_voc, ssc_vec = build_embedding(ssc_voc, ssc_vec, sents[1], emb_voc, emb_vec)
                        
    return train_data, valid_data, test_data, ssc_voc, ssc_vec


def build_semcom(line, ssc_vec):
    sents = line.split('\t')
    tokens = sents[1].split()
    tags = sents[2].split()
    label = torch.LongTensor([int(sents[0])])    
    row, idx = 0, 0
    
    for i in range(len(tags)):
        if tags[i][0:1] == 'b' or tags[i][0:1] == 'o':
            row += 1
    sentm = torch.FloatTensor(row, args.word_dim)
    
    for i in range(len(tags)):
        if tags[i][0:1] == 'b' or tags[i][0:1] == 'o':
            sentm[idx] = ssc_vec[tokens[i]]
            if idx < row - 1:
                idx = idx + 1 
        else:
            sentm[idx] = sentm[idx] + ssc_vec[tokens[i]]
            
    return label, sentm


def build_matrix(line, ssc_vec):
    sents = line.lower().split('\t')
    tokens = sents[1].split()
    label = torch.LongTensor([int(sents[0])])
    sentm = torch.FloatTensor(len(tokens), args.word_dim).zero_()
    
    for i in range(len(tokens)):
        sentm[i] = ssc_vec[tokens[i]]
    
    return label, sentm 


def set_timer(sec):
    min = math.floor(sec / 60)
    sec -= min * 60
    return '%d min %d sec!' % (min, sec)


def train():
    accu_best, accu_test = 0, 0
    emb_voc, emb_vec = read_embedding()
    train_data, valid_data, test_data, ssc_voc, ssc_vec = read_corpus(emb_voc, emb_vec)
    
    for i in range(args.epochs): 
        start = time.time()   
        random.shuffle(train_data)
        epoch_storage, train_correct, valid_correct, test_correct = 0, 0, 0, 0

        for j in range(len(train_data)):
            label, sentm = build_matrix(train_data[j], ssc_vec)
            sent = Variable(sentm)
            target = Variable(label)
            if use_gpu:
                sent = sent.cuda()
                target = target.cuda()
            out, mu, va, sc = rvae(sent)
            _, predicted = torch.max(sc.view(1, args.enc_size), 1)
            if predicted[0].data[0] == target.data[0]:
                train_correct += 1
            loss = loss_function(out, sent, mu, va)
            if use_gpu:
                loss = loss.cuda()
            loss = loss + cel_criterion(sc.view(1, args.enc_size), target) 
            epoch_storage += loss.data[0]
            optimizer.zero_grad()
            loss.backward()    
            optimizer.step()
        print("total loss: " + str(epoch_storage / len(train_data)))
        print("train accu: " + str(train_correct / len(train_data)))
        
        for j in range(len(valid_data)):
            label, sentm = build_matrix(valid_data[j], ssc_vec)
            sent = Variable(sentm)
            target = Variable(label)
            if use_gpu:
                sent = sent.cuda()
                target = target.cuda()
            out, mu, va, sc = rvae(sent)
            _, predicted = torch.max(sc.view(1, args.enc_size), 1)
            if predicted[0].data[0] == target.data[0]:
                valid_correct += 1
                
        accu_valid = valid_correct / len(valid_data)
        print("valid accu: " + str(accu_valid))
        
        if accu_valid > accu_best:
            accu_best = accu_valid
            for j in range(len(test_data)):
                label, sentm = build_matrix(test_data[j], ssc_vec)
                sent = Variable(sentm)
                target = Variable(label)
                if use_gpu:
                    sent = sent.cuda()
                    target = target.cuda()
                out, mu, va, sc = rvae(sent)
                _, predicted = torch.max(sc.view(1, args.enc_size), 1)
                if predicted[0].data[0] == target.data[0]:
                    test_correct += 1
            print("epochs: " + str(i + 1) + " test accu: " + str(test_correct / len(test_data)))
        end = time.time()
        print("cost time: " + set_timer(end - start))
        
 
def main():
    train()
    print("oov: ", oov, "\tvoc: ", voc)


if __name__ == "__main__":
    main()