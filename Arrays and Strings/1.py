def tie_em_up(a,b,c):
    out = []
    for ii in range(0,len(a)):
        out.append((a[ii],b[ii],c[ii]))
    return out

def UniqueStr(str):
    prevmap={}
    for n,char in enumerate(str):
        if char in prevmap:
            return False
        else:
            prevmap[char] = n
    return True


def anagram(str1,str2):
    counter = {}
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1)!=len(str2):
        return False
    else:
        for ii in range(0,len(str1)):
            if str1[ii] not in counter: 
                counter[str1[ii]] = 1
            else:
                counter[str1[ii]] += 1
        for ii in range(0,len(str2)):
            if counter[str2[ii]]==0:
                return False
            else:
                counter[str2[ii]]-=1
    return sum(counter.values())==0


def Urlify(string):
    new_string = ''
    for ii in range(0,len(string)):
        if string[ii] == ' ':
            new_string = new_string+'%20'
        else:
            new_string=new_string+string[ii]
    return new_string



def linearsearch(A, key):
    ii = 0
    for ii in range(0, len(A)):
        if A[ii] == key:
            return ii
    return False


def binarysearch_iterative(A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r)//2
        if A[m] == key:
            return m
        elif key < A[m]:
            r = m -1
        elif key > A[m]:
            l = m + 1    
    return False


def binarysearch_recursive(A, key, L , R):
    if L > R:
        return False
    else:
        m  = (L + R)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            return binarysearch_recursive(A, key, L, (m -1))
        elif key > A[m]:
            return binarysearch_recursive(A, key, (m+1), R)
        
        
if __name__ == '__main__':
    
    a = ["NC", "DC", "MAA"]
    b = ["1", "2", "3"]
    c = ['Harish', 'Kaushik', 'Hemant']
    print("TieEmUp:", tie_em_up(a,b,c))
    
    
    str1 = 'the quick brown fox'
    str2 = 'fox quick brown the'
    
    print('Anagram:', anagram(str1, str2))
    
    string = 'Mr.John Smith College Park'
    print('Urlify:' , Urlify(string))
    
    A = [1,2,3,4,5,6]
    print("Linear Search: ", linearsearch(A,5))
    
    A = [1, 21, 30, 36, 37, 73]
    print('BinarySearchIterative: ',binarysearch_iterative(A, 73))
    
    A = [1, 21, 30, 36, 37, 73]
    L = 0
    R = (len(A)-1)
    key = 73
    print("BinarySearchRecursive: ", binarysearch_recursive(A, key, L, R))
