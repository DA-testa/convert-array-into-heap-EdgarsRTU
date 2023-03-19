def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            l =2*j + 1
            if l >= n:
                break
            if l +1 < n and data[l + 1] < data[l]:
                l += 1
            if data[j] > data[l]:
                swaps.append((j, l))
                data[j], data[l] = data[l], data[j]
                j = l
            else:
                break  
  
    return swaps
 
 
def main():
    
    read_input = input()
    
    if read_input.startswith('I'):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif read_input.startswith('F'):
        file = input().strip()
        with open(f'tests/{file}', 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        
    else:
        print('Invalid')
     
 
 
if __name__ == "__main__":
    main()
    #Edgars Miklaševičs
