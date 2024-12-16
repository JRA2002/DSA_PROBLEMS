def chunk_list(list):
    list_chunk = []
    for i in range(0,len(list),4) :
        chunk = list[i:i+4]
        list_chunk.append(chunk)

    for i in list_chunk:
        print(i)

list = [1,2,3,4,5,6,7,8,9]
chunk_list(list)