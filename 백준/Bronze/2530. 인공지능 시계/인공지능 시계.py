h, m, s = map(int, input().split())
rs = int(input()) # required time

time = 3600*h + 60*m + s + rs # change to sec
fh = (time//3600)
fm = (time - 3600*fh)//60
fs = (time - 3600*fh) % 60

fh = fh%24 # over 24h

print(fh, fm, fs)