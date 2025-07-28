k = input().strip()

if len(k) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit()
base = int(k[1]) - int(k[0])
for i in range (2, len(k)):
    if int(k[i]) - int(k[i-1]) != base:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        exit()
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")