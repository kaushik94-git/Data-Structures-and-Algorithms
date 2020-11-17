def tie_em_up(a,b,c):
    out = []
    for ii in range(0,len(a)):
        out.append((a[ii],b[ii],c[ii]))
    return out


if  __name__ == '__main__':
    a = ["John", "Charles", "Mike"]
    b = ["Jenny", "Christy", "Monica"]
    c = ['Harish', 'Kaushik', 'Hemant']
  
    print(tie_em_up(a,b,c))  
