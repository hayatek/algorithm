from typing import List

input = [2,5,1,8,7,3]
def bubble_sort(l:List[int]) -> List[int]:
    for i in range(len(l) -1):
        for j in range(len(l) -1 -i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

if __name__ == '__main__':
    print(bubble_sort(input))