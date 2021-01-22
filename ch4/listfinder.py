headtail = ['h','t','h','h','h','t','h','h','t','t','t']
size = len(headtail)
count = 0
for i in range(size - 2):
    if headtail[i] == headtail[i + 1] and headtail[i + 1] == headtail[i + 2]:
        count =+ 1
print(count)