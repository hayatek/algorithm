from typing import List

input = [2,5,1,8,7,3]

def check_order(num_list:List[int]) -> bool:
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            return False
    return True


def bubble_sort(l:List[int]) -> List[int]:
    while not check_order(l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l


if __name__ == '__main__':
    print(bubble_sort(input))