seznam_osob = []

def vytvor_osobu(jmeno, prijmeni, adresa, den, mesic, rok, telefon, email,sez_osob):
    sez_osob = []
    sez_osob.append({"jmeno": jmeno,"prijmeni": prijmeni,"adresa": adresa,"den": den,"mesic": mesic,"rok": rok,"telefon": telefon,"email": email})
    return sez_osob

osoba1 = vytvor_osobu("Alice", "Pokorna", "Holicka62", 27, 5, 1987, "214 145 478", "alice.pokorna@email.cz","osoba1")
osoba2 = vytvor_osobu("Pavel", "Novak", "tr. 17 listopadu 24", 22, 2, 1990, "654 784 478", "pavel.novak@seznam.cz","osoba2")
osoba3 = vytvor_osobu("Liza", "Navratilova", "Klášterského 22", 7, 11, 1985, "730 753 490", "liza.navratilova@seznam.cz","osoba2")
osoba4 = vytvor_osobu("Lukas", "Dvorak", "Pavlova 185/6", 31, 3, 1993, "930 552 841", "lukas.dvorak@seznam.cz","osoba2")

def vloz(s, o):
    v = []
    for i in range(len(o)):
        v.append(o[i])
    s.append(v)
    return s

vloz(seznam_osob, osoba1)
vloz(seznam_osob, osoba2)
vloz(seznam_osob, osoba3)
vloz(seznam_osob, osoba4)

def najdi_osobu(kde, co, s):
    for i in range(len(s)):
        for j in seznam_osob[i]:
            if j[kde] == co:
                return True

if (najdi_osobu("adresa", "Holicka62", seznam_osob)):
    print("Alice nalezena. \n")
else: 
    print("Alice nenalezena. \n")

if (najdi_osobu("prijmeni", "Novotny", seznam_osob)):
    print("Novotny nalezen. \n")
else:
    print("Novotny nenalezen. \n")

def nejmladsi(s):
    for i in osoba1:
        iMinRok = i["rok"]
        iMinMesic = i["mesic"]
        iMinDen = i["den"]
        nejmladsi = ""
    for i in range(len(seznam_osob)):
        for j in seznam_osob[i]:
                if j["rok"] < iMinRok:
                    iMinRok = j["rok"]
                    nejmladsi = seznam_osob[i]
                elif j["rok"] == iMinRok:
                    if j["mesic"] < iMinMesic:
                        iMinMesic = j["mesic"]
                        nejmladsi = seznam_osob[i]
                    elif j["mesic"] == iMinMesic:
                        if j["den"] < iMinDen:
                            iMinDen = j["den"]
                            nejmladsi = seznam_osob[i]
                        elif j["den"] == iMinDen:
                            iMinDen = j["den"]
                            nejmladsi = seznam_osob[i]
    return nejmladsi
                
o = nejmladsi(seznam_osob)

def tisk_osoby(o):
    for i in o:
       jmeno = i["jmeno"]
       prijmeni = i["prijmeni"]
       rok = i["rok"]
       mesic = i["mesic"]
       den = i["den"]
    return f"{jmeno} {prijmeni}, datum narozeni : {den} - {mesic} - {rok}"

print("Nejmladsi osobou v seznamu je", tisk_osoby(o)," ")

def tisk(s):
    print("Osoby ze seznamu s: ")
    for i in range(len(s)):
        print(*s[i])

tisk(seznam_osob)