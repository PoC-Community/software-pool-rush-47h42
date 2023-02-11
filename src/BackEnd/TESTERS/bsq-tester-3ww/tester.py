#!/usr/bin/python3
#3WW

import os, json
import subprocess
import sys

def main() -> None:
    ret = ""
    os.system('touch ../main.json')
    file = open('../main.json', 'w')
    Json = []
    list_path_map = []
    list_path_solved = []
    for filename in os.listdir("../../TESTERS/bsq-tester-3ww/maps-intermediate/mouli_maps"):
       list_path_map.append("../../TESTERS/bsq-tester-3ww/maps-intermediate/mouli_maps/" + filename)
    for filename in os.listdir("../../TESTERS/bsq-tester-3ww/maps-intermediate/mouli_maps_solved"):
        list_path_solved.append("../../TESTERS/bsq-tester-3ww/maps-intermediate/mouli_maps_solved/" + filename)
    good = 0
    for i in range(len(list_path_map)):
        one = os.popen("./bsq " + list_path_map[i]).read()
        if one:
            one = one.split('\n')
            one.pop()
            one.pop(0)
            two = os.popen("cat " + list_path_solved[i]).read()
            two = two.split('\n')
            two.pop()
            two.pop(0)

            if (one == two):
                ret = 'OK'
                good += 1
            else:
                ret = 'KO'
        else:
            ret = 'KO'
        tmp = 'test on ' + list_path_map[i]
        Json.append({tmp : ret})
    json.dump(Json, file)
    file.close()
    file = open('../main.json', 'r')
    buff = file.read()
    file.close()
    file = open('../main.json', 'w')
    file.write(buff.replace(',', ',\n').replace('[', '[\n').replace(']', '\n]'))
    file.close()
    # print(colored(str(good), 'green'), "on", colored(str(len(list_path_solved)), 'blue'), "->", (good * 100) / len(list_path_solved))

main()
