_x = """Johan Cruyff
Pelè
Diego Maradona
Michel Platini
Franz Beckenbauer
Ronaldo
Kylian Mbappe
Erling Haaland
Kevin De Bruyne
Lionel Messi
Karim Benzema
Thibaut Courtois
Harry Kane
Robert Lewandowski
Mohamed Salah
Rúben Dias
Vinícius Júnior
Rodri
Neymar Jr
M. ter Stegen
Virgil van Dijk
Alisson Becker
Casemiro
Federico Valverde
Bernardo Silva
Joshua Kimmich
Bruno Fernandes
Ederson
Jan Oblak
A. Griezmann
Cristiano Ronaldo
De Gea
Marco Verratti
Gregor Kobel
L. Martínez
G. Donnarumma
Frenkie de Jong
M. Ødegaard
Mike Maignan
Marquinhos
Heung Min Son
Luka Modrić
Manuel Neuer
Jamal Musiala
Ronald Araujo
Jude Bellingham
Pedri
Bukayo Saka
Rafael Leão
Sandro Tonali
M. de Ligt
C. Nkunku
O. Dembélé
Alexander-Arnold
Nicolò Barella
S. Milinković-Savić
A. Robertson
N. Kanté
Paulo Dybala
João Cancelo
Sadio Mané
W. Szczęsny
Toni Kroos
Rodrygo
Phil Foden
A. Bastoni
Declan Rice
Theo Hernández
Marcus Rashford
André Onana
Marcos Acuña
Kingsley Coman
Aymeric Laporte
Thomas Partey
Yassine Bounou
Leon Goretzka
H. Çalhanoğlu
Jack Grealish
A. Rüdiger
John Stones
E. Martínez
Raphaël Varane
David Alaba
Keylor Navas
Luis Suárez
Paul Pogba
Giorgian De Arrascaeta
EDOUARD MENDY
AYMERIC LAPORTE
RAHEEM STERLING
RIYAD MAHREZ
CIRO IMMOBILE
THIAGO SILVA
NICOLO BARELLA
BRUNO FERNANDES
MARCELO BROZOVIC
PAREJO
DAVID ALABA
MILAN SKRINIAR
İLKAY GUNDOGAN
THEO HERNANDEZ"""

splited = _x.split("\n")

import random

def produce(i_value):
    _val = splited[random.randint(0, (len(splited))-1)]
    if _val == i_value:
        return produce(i_value)
    else:
        return _val.strip()

cout=1
output_ = ""
for i in splited:
    output_+=f"""a++;
window["ans"+a] = "{i.strip()}"; //Ans{cout}
window["noans1"+a] = "{produce(i)}";
window["noans2"+a] = "{produce(i)}";
window["noans3"+a] = "{produce(i)}";
window["noans4"+a] = "{produce(i)}";

"""
    cout+=1

f = open('playersOutput.txt', 'a', encoding='utf-8')
f.write(output_)
f.close()