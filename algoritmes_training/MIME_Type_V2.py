def extraire_extention(nom):
    e = nom.split(".")
    if len(e) == 1:
        return None
    return e[-1]


dictionnaire = {"wav": "audio/x-wa", "mp3": "audio/mpeg", "pdf": "application/pdf"}
l = ['a', 'a.wav', 'b.wav.tmp', 'test.vmp3', 'pdf',
     'afll.pdf', 'mp3', 'report..pdf', 'defaultwav', '.mp3.', 'final.']
n = 3
q = 11
definition = ""

for a in range(q):
    ex = extraire_extention(l[a])
    if ex is None:
        print("UNKNOWN")
    else:
        if dictionnaire.get(ex):
            print(dictionnaire[ex][0])
        else:
            print("UNKNOWN")