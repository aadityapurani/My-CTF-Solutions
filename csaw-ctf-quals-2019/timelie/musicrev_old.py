import os

from music21 import *

numUniquePitches = 12
numChords = 200
fileFormat = 'xml'
octave = 4

FOLDER_NAME = "_temp"
FILE_NAME = "music"


def unique(l):
    unique_list = []
    for item in l:
        if(item not in unique_list):
            unique_list.append(item)
    return unique_list

def addList(a,b):
    return unique(a+b)

def subList(a,b):
    for item in b:
        if(item in a):
            a.pop(a.index(item))

def reverseFunction(chordList,output):
    # reverse combine_lunar_frequencies
    bin_arr = []
    chordList = [unique([int(pit.pitches-60) for pit in item.pitches]) for item in chordList]
    for i in range(len(output)):
        item = output[i]
        chords = chordList[i%len(output)]
        bin_arr.append(unique(subList(item,chordList)))
    return bin_arr

def createM24File(numChords,chosenChord,fileName):
    # don't include the name
    s = stream.Stream()
    for _ in range(numChords):
        c = chord.Chord()
        for _ in range(numUniquePitches):
            p = pitch.Pitch(chosenChord,octave=octave)
            c.add(p)
        s.append(c)
    s.write(fileFormat,fileName+'.' + fileFormat)


def main():
    fileNames = [FILE_NAME+str(i+1) for i in range(numUniquePitches)]
    try:
        os.mkdir(FOLDER_NAME)
    except:
        pass
    for i in range(len(fileNames)):
        createM24File(numChords,i,FOLDER_NAME+'/'+fileNames[i])
    return
    outputs = []

    convertedFiles = [
        converter.parse(fileName).chordify().flat.getElementsByClass('Chord')
        for fileName in fileNames
    ]
    reversedFunctions = [reverseFunction(converted,output) for converted,output in zip(convertedFiles,outputs)]

    finalArr = reversedFunctions[0]
    for i in range(len(reversedFunctions[0])):
        item2 = reversedFunctions[1][i]
        if(1 in item2[i]):
            index = max([arr.index(1) for arr in finalArr[1:][i]])
            finalArr[i] = finalArr[i][:index] + [1] + finalArr[i][index:]
    finStr = ""
    for item in finalArr:
        hexValue = hex(sum([2**num for num in item]))
        finStr += hexValue
    return hexValue

if(__name__=='__main__'):
    main()
