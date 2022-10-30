def extraire_extention(nom):
    e = nom.split(".")
    if len(e) == 1:
        return ""
    return e[-1]


list = ['wav audio/x-wav', 'mp3 audio/mpeg', 'pdf application/pdf', 'a', 'a.wav', 'b.wav.tmp', 'test.vmp3', 'pdf', 'afll.pdf', 'mp3', 'report..pdf', 'defaultwav', '.mp3.', 'final.']
n = 3
q = 11
definition=""

for ex in list[n:]:
    extentions = extraire_extention(ex)
    for definition in list[:n]:
        definition = definition.split()
        if extentions.lower() == definition[0].lower():
            print(definition[1])
            break
    if extentions != definition[0]:
        print("UNKNOWN")

