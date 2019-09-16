import os

from lxml import etree
from music21 import *

numUniquePitches = 12
numChords = (18 * 3 + 0) * 2
half_numChords = int(numChords/2)
fileFormat = 'xml'
octave = 4

def unique(l):
    unique_list = []
    for item in l:
        if(item not in unique_list):
            unique_list.append(item)
    return unique_list

def subList(a,b):
    # print(a,b)
    for item in b:
        if(item in a):
            a.pop(a.index(item))
    return a

def reverseFunction(Input,Output):
    bin_arr = []
    for i in range(len(Output)):
        oItem = Output[i]
        iItem = Input[i%len(Input)]

        theData = subList(oItem,iItem)
        bin_arr.append(theData)
    return bin_arr

def createM24File(numChords,chosenChord,fileName):
    # don't include the name
    s = stream.Stream()
    for _ in range(half_numChords):
        c = chord.Chord()
        for _ in range(numUniquePitches):
            p = pitch.Pitch(chosenChord,octave=octave)
            c.add(p)
        s.append(c)
    for _ in range(half_numChords):
        c = chord.Chord()
        for _ in range(numUniquePitches):
            p = pitch.Pitch(chosenChord+1,octave=octave)
            c.add(p)
        s.append(c)
    s.write(fileFormat,fileName+'.' + fileFormat)

def getData(fileName):
    data = converter.parse(fileName + '.' + fileFormat).chordify().flat.getElementsByClass('Chord')
    data = [unique([int(pit.ps-60) for pit in item.pitches]) for item in data]
    data = unique(data)
    return data

def getMetaData(outputFileName):
    return etree.parse(outputFileName).find('work').find('work-title').text

for i in xrange(1, 200):
    print "Sicing "+str(i)
    fileName = "input"
    #outputFN = "output_"+str(i)
    outputFN ="pleaswork"

    # createM24File(numChords,1,fileName)

    # return

    metaData = getMetaData(outputFN+'.'+fileFormat)

    Input = getData(fileName)

    Output = getData(outputFN)

    Reversed = reverseFunction(Input,Output)
    print(len(Reversed),len(Output))
    half_out = int(len(Reversed)/2)
    finalArr = Reversed[:half_out]
    for i in range(half_out):
        item2 = Reversed[i+half_out]
        if(1 in item2):
            finalArr[i].append(1)
    finStr = ""
    for item in finalArr:
        hexValue = hex(sum([2**num for num in item]))[2:]
        finStr += hexValue
    l = (metaData,finStr)
    print str(l)
    f = open('siced.txt','a')
    f.write(str(l))
