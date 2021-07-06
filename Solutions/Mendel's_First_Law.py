def iprb(k, m, n):
    total=k+m+n

    p1=(k/total)*((k-1)/(total-1))
    p2=(k/total)*(m/(total-1))
    p3=(k/total)*(n/(total-1))
    p4=(m/total)*(k/(total-1))
    p5=0.75*(m/total)*((m-1)/(total-1))
    p6=0.5*(m/total)*(n/(total-1))
    p7=0*(n/total)*((n-1)/(total-1))
    p8=0.5*(n/total)*(m/(total-1))
    p9=(n/total)*(k/(total-1))

    return round(p1+p2+p3+p4+p5+p6+p7+p8+p9, 5)

if __name__ == "__main__":
    with open("Downloads/rosalind_iprb.txt", 'r') as f:
        k, m, n = map(int, f.readline().strip().split(" "))
        print(iprb(k, m, n))
