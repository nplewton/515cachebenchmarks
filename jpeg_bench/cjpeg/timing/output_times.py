#!/usr/bin/env python

import sys
import os

colorTimes = []
huffTimes = []
dataTimes = []

outFile = open('times.csv', 'w+')
outFile.write('type,sample,phase,total,avg\n')

timesFiles = filter(lambda n : 'times' in n and '.txt' in n, os.listdir('.'))

for name in timesFiles:
    with open(name) as f:
        for l in f.readlines():
            time = int(l.split(' ')[-2])
            if 'Data Compression' in l:
                dataTimes.append(time)
            elif 'Huffman Encode' in l:
                huffTimes.append(time)
            elif 'Color Conversion' in l:
                colorTimes.append(time)

        totalColor = sum(colorTimes)
        totalHuff = sum(huffTimes)
        totalData = sum(dataTimes)

        avgColor = totalColor / len(colorTimes)
        avgHuff = totalHuff / len(huffTimes)
        avgData = totalData / len(dataTimes)

        sampleNo = int(name[5])
        typ = 'None'

        if 'pref' in name:
            try:
                prefNum = int(name[-5])
            except:
                prefNum = 1

            typ = 'prefetch %d' % (prefNum)

        outFile.write('%s,Sample %d,Color,%d,%d\n' % (typ, sampleNo, totalColor, avgColor))
        outFile.write('%s,Sample %d,Huffman,%d,%d\n' % (typ, sampleNo, totalHuff, avgHuff))
        outFile.write('%s,Sample %d,Compress,%d,%d\n' % (typ, sampleNo, totalData, avgData))
