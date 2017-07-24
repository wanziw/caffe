import os 
import sys
import random
import numpy as np
from sklearn import cross_validation

trainX = []
trainY = []
testX  = []
testY  = []
intra  = []
extra  = []

print sys.argv[1], sys.argv[2]
trainingpath= sys.argv[1] + "CASIA-WebFace/"
testingpath = sys.argv[1] + sys.argv[2] + '/'


#training dataset
folder = [name for name in os.listdir(trainingpath) if os.path.isdir(os.path.join(trainingpath, name))]
for ff in folder:
    path = trainingpath + ff + '/croped/'
    im = [name for name in os.listdir(path)]
    for ii in im: 
        trainX.append(path + ii)
        trainY.append(str(int(ff)))

#testing dataset
folder = [name for name in os.listdir(testingpath)]
for ff in folder:
    path = testingpath + ff + '/croped/'
    im = [name for name in os.listdir(path)]
    for ii in im: 
        testX.append(path + ii)
        testY.append(ff)

#generate testing pairs
testamount = 10
while True:
    if len(intra) == testamount and len(extra) == testamount:
        break
    a = random.randint(0, len(testX) - 1)
    b = random.randint(0, len(testX) - 1)
    if testY[a] == testY[b]:
        if len(intra) == testamount: continue
        intra.append([a, b])
    else:
        if len(extra) == testamount: continue
        extra.append([a, b])

#corss validation
X_train, _, Y_train, _ = cross_validation.train_test_split(trainX, trainY, test_size = 0.2)
X_test = testX
Y_test = testY

#write all information into files
f = open('./data/deepid2/train.out', 'w')
for i in range(len(X_train)):
    f.write('../../' + X_train[i] + ' ' + Y_train[i] + '\n')

f = open('./data/deepid2/val.out'  , 'w')
for i in range(len(X_test)):
    f.write('../../' + X_test[i] + ' ' + Y_test[i] + '\n')

f = open('./data/deepid2/intra.out', 'w')
for i in range(len(intra)):
    f.write(str(intra[i][0]) + ' ' + str(intra[i][1]) + '\n')

f = open('./data/deepid2/extra.out', 'w')
for i in range(len(extra)):
    f.write(str(extra[i][0]) + ' ' + str(extra[i][1]) + '\n')

f = open('./data/deepid2/name' + sys.argv[2] + '.out', 'w')
for i in range(len(testY)):
    f.write(str(testY[i]) + '\n')

