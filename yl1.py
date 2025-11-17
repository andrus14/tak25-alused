# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides
# sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)

# küsin kasutajalt kroonid
# teisendan kroonid eurodeks
# ümardan
# väljastan tulemuse

eek = float(input('EEK: '))
eur = eek / 15.6466
print(round(eur, 2))