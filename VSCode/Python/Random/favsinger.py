N = int(input("Enter:"))
Playlist = list(map(int, input().split()))
maxivalue = max(Playlist)
count=0
i = 1
while i<=maxivalue:
    n=Playlist.count(i)
    if n>count:
        count=n
    i+=1
print(count)
j=1
orgcount=0
while j<=maxivalue:
    m=Playlist.count(j)
    if m==count:
        orgcount+=1
    j+=1

print(orgcount)