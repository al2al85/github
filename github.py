# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:57:21 2021

@author: Admin
"""

from datetime import datetime

file = open("github.txt", "w")

liste_cest = ["c", "c'est", "ces", "ce", "cest", "cset", "ses", "sé", "set", "sè", "set", "sèt", "zé", "zet"]
liste_quand = ["Quand", "Quan", "Qan", "Quend", "Quen", "Qen", "Kand", "Quant", "Kant", "Kan", "Can", "Cen", "Cant", "Cand", "Cent", "Cend", "Kent", "Kent"]
liste_quon = ["Qu'on", "Quon", "Qon", "Ku'on", "Qu'ont", "Ku'ont", "Kuon", "Kon", "Khon", "Kohn", "Cuont", "Cu'ont", "Cu'on", "Con", "Chon", "Cohn", "Quont"]
liste_a = ["a", "ah", "ha", "e", "haa", "aah", "à"]
liste_1 = ["un", "1", "ain", "in", "aiun", "ainh", "àin", "àiun", "àeinh", "ein", "hein", "ehin", "eihn" "einh"]
liste_github = ["github", "jithub", "githeube", "jiteube", "gythub", "gytheube", "gytheube", "githoube", "gatahbe", "jitabeh", "gythuebe", "githuebe", "jituebe"]

count = 0
starttime = datetime.now()
for element1 in liste_cest:
    for element2 in liste_quand:
        for element3 in liste_quon:
            for element4 in liste_a:
                for element5 in liste_1:
                    for element6 in liste_github:
                        print(element1 + " " +  element2 +" " + element3 + " " +element4 +" " +element5 +" " + element6)
                        count +=1
                        file.write(element1 + " " +  element2 +" " + element3 + " " +element4 +" " +element5 +" " + element6 +"\n")
stoptime = datetime.now()
print(str(count) + " possibilitées")
print("Temps passé : " + str(stoptime - starttime))
file.close()