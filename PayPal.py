def solution1(A):
    max_set = set()
    tot_set = set()
    for index in range(len(A)):
        if A[index] not in tot_set:
            tot_set.add(A[index])
            tmp_set = set()
            while A[index] not in tmp_set:
                tmp_set.add(A[index])
                tot_set.add(A[index])
                index = A[index]
            if len(tmp_set) > len(max_set):
                max_set = tmp_set
    return max_set, len(max_set)

print
print solution1([5,4,0,3,1,6,2])
print solution1([0])
print solution1([])

def solution2a(A):
    tot_set = set(range(1,len(A)+1))
    for index in range(len(A)):
        if A[index] in tot_set:
            tot_set.pop(A[index])
    return tot_set

def solution2(A):
    nums = [0] * (len(A)+2)
    nums[0] = 1
    array_length = len(nums)
    for index in range(len(A)):
        if A[index] < array_length:
            nums[A[index]] = 1
    return nums.index(0)

print
print solution2([1,3,6,4,1,2])
print solution2([0])
print solution2([])

def solution3a(K, A):
    found = [False] * len(A)
    count = 0
    for index in range(len(A)):
        if not found[index]:
            complement = K-A[index]
            if complement in A:
                complement_index = A.index(complement)
                if not found[complement_index]:
                    found[index] = True
                    found[complement_index] = True
                    if A[index] == complement:
                        count += 1
                    else:
                        count += 2

    return count

def solution3(K, A):
    count = 0
    for index in range(len(A)):
        complement = K-A[index]
        count += len([x for x in A if x==complement])
    return count

def solution3c(K, A):
    sorted_list = sorted(A)
    index = 0
    tail_index = len(A)-1
    count = 0
    while index < tail_index:
        #print (index,tail_index)
        if sorted_list[index] == K/2.0:
            seq = 1
            while sorted_list[index] == sorted_list[index+1]:
                seq += 1
                index += 1
            count += (seq * (seq-1)) + seq
            break
        if sorted_list[tail_index] == K/2.0:
            seq = 1
            while sorted_list[tail_index] == sorted_list[tail_index-1]:
                seq += 1
                tail_index -= 1
            count += (seq * (seq-1)) + seq
            break
        complement = K-sorted_list[index]
        if sorted_list[tail_index] > complement:
            tail_index -= 1
        elif sorted_list[tail_index] < complement:
            index += 1
        else:
            #print complement
            head_seq,tail_seq = 1,1
            while sorted_list[index] == sorted_list[index+1]:
                head_seq += 1
                index += 1
            while sorted_list[tail_index] == sorted_list[tail_index-1]:
                tail_seq += 1
                tail_index -= 1
            count += head_seq * tail_seq * 2
            index += 1
            tail_index -= 1
    return count


print
print solution3(6,[1,8,-3,0,1,3,-2,4,5])
print solution3(6,[0])
print solution3(6,[])
print
print solution3c(6,[1,8,-3,0,1,3,-2,4,5])
print solution3c(6,[0])
print solution3c(6,[])
