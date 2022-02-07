
def arrayManipulation(n, queries):

    maxSum = 0
    arr = [0] * n # n boyutlu dizi oluşturuluyor

    for query in queries:
        # print(query)
        a = query[0]
        b = query[1]

        for i in range(a, b+1):
            arr[i-1] += query[2]
            print(arr[i-1])
        # print(arr)

    maxSum = max(sorted(arr))

    return maxSum

n = 10
queries = [ [1,5,3], [4,8,7], [6,9,1] ]

print(arrayManipulation(n, queries))