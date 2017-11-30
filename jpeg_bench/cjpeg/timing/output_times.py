#!/usr/bin/env python

import sys

colorTimes = []
huffTimes = []
dataTimes = []

with open(sys.argv[1]) as f:
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

print 'Color conversion - total time %d ns, average %d ns' % (totalColor, avgColor)
print 'Huffman Encode - total time %d ns, average %d ns' % (totalHuff, avgHuff)
print 'Data Compression - total time %d ns, average %d ns' % (totalData, avgData)
