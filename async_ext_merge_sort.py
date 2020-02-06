import asyncio
import time
import os


async def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        await mergeSort(lefthalf)
        await mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    # print("Merging ",alist)


async def read_integers(file):
    with open(file) as f:
        return [int(i) for i in f]


async def writer(array):
    with open('output/async_sorted.txt', 'w') as filewriter:
        filewriter.writelines("%s\n" % i for i in temp_list)


async def main():
    for file in os.listdir(os.curdir + "/input"):
        if file.endswith(".txt"):
            file_input_path = os.path.join("input", file)
            r = await read_integers(file_input_path)
            await mergeSort(r)
            with open(os.path.join("temp_output", file), 'w') as filewriter:
                 filewriter.writelines("%s\n" % i for i in r)

    temp_list = []
    for file in os.listdir(os.curdir + "/temp_output"):
        if file.endswith(".txt"):
            file_input_path = os.path.join("input", file)
            r = await read_integers(file_input_path)
            temp_list.extend(r)

    await mergeSort(temp_list)
    with open('output/async_sorted.txt', 'w') as filewriter:
        filewriter.writelines("%s\n" % i for i in temp_list)


if __name__ == "__main__":
    ProcessTime = time.process_time()
    asyncio.run(main())
    print(time.process_time() - ProcessTime)
