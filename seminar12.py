def do_stredu(text):
    word=[]
    lenght = len(text)
    word.append(text[0:lenght:2])
    other = text[1:lenght:2]
    def reversed(variable): 
        if len(variable) == 1:
            return variable
        return variable[-1] + reversed(variable[:-1])
    word.append(reversed(other))
    print(''.join(word))

def vlozeni_do_textu(text,vloz):
    word = []
    for i in text:
        word.append(i)
        word.append(vloz)
    print(''.join(word))
    
def eratosthenovo_sito(n):
    a = []

    for i in range(n + 1):
        a.append(i)

    a[1] = 0
    
    i = 0
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a[0] = 1
    a = set(a)
    a.remove(0)
    print(a)

do_stredu("PYTHON")
vlozeni_do_textu("PYTHON","abc")
eratosthenovo_sito(100)