import time
import os

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

def read_integers(file):
    with open(file) as f:
        return [int(i) for i in f]

ProcessTime = time.process_time()

for file in os.listdir(os.curdir+"/input"):
    if file.endswith(".txt"):
        file_input_path = os.path.join("input", file)
        r = read_integers(file_input_path)
        mergeSort(r)
        with open(os.path.join("temp_output", file), 'w') as filewriter:
            filewriter.writelines("%s\n" % i for i in r)

temp_list = []
for file in os.listdir(os.curdir+"/temp_output"):
    if file.endswith(".txt"):
        file_input_path = os.path.join("input", file)
        r = read_integers(file_input_path)
        temp_list.extend(r)

mergeSort(temp_list)
with open('output/sorted.txt', 'w') as filewriter:
    filewriter.writelines("%s\n" % i for i in temp_list)


print(time.process_time() - ProcessTime)
