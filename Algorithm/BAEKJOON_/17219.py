import sys
input = sys.stdin.readline

N, TC = map(int, input().split())

site = {}
for _ in range(N) :
    address, pw = input().split()
    site[address] = pw

result = []
for _ in range(TC) :
    result.append(site[input().rstrip()])
print("\n".join(result))