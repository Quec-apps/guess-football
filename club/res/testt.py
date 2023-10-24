_x = """FC Barcelona
FC Internazionale Milano
FC Bayern Munich
Estudiantes De La Plata
Club Atlético De Madrid
Manchester United FC
Chelsea FC
Liverpool FC
Real Madrid CF
Sport Club Internacional
AS Roma
RSC Anderlecht
Valencia CF
Cruzeiro Esporte Clube
Club Libertad"""

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

f = open('clubOutput.txt', 'a')
f.write(output_)
f.close()