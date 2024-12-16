def minmax(data):
    
    if data[0] <= data[1]:  #define a max and min values
            min = data[0]
            max = data[1]
    else:
         min = data[1]
         max = data[0]

    for i in range(len(data)-2):  #iterate over the lenght of the list
        
        if min > data[i+2]:
            min = data[i+2]
        
        if max < data[i+2]:
            max = data[i+2]

    return max,min  #this return a tuple (max, min)
    

print(minmax([10,20,7,30,6,5,6,19,4,9]))
