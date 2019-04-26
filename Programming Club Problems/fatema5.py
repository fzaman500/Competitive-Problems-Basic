cases = int(input())
alphabet = []
for a in range(97, 122):
    alphabet.append(chr(a))
for i in range(0, cases):
    shift = int(input())
    word = input()
    finWord = ""
    for j in range(0, len(word)):
        for k in range(0, len(alphabet)):
            if word[j] == alphabet[k]:
                finWord = finWord + alphabet[(k + shift) % 26]
    print("Message #" + str(i + 1) + ": " + finWord)
