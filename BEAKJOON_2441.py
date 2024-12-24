sentence = str(input())
a = ( len(sentence) // 10 ) + 1
for i in range(a):
    b = i * 10
    c = b + 10
    print(sentence[b:c])