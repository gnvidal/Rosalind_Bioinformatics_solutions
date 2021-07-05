memo={}
def fib_rec(n, k):
	if n==0 or n==1:
		return 1
	return fib_rec(n-1) + fib_rec(n-2)
#now, we've used dynamic programming
def fib_dina(n, k=1):
    args=(n,k)
    if args in memo:
        return memo[args]
    if n==0 or n==1:
        return 1
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib_dina(n-1, k) + k*fib_dina(n-2, k)
    memo[args] = ans
    return ans
if __name__ == "__main__":
    with open("Downloads/rosalind_fib.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(fib_dina(int(n), int(k)))
