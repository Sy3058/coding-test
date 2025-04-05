total = int(input())
books = list(int(input()) for _ in range (9))
print(total - sum(books))