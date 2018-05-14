# -*- coding: utf-8 -*-
import json

def http_headers_to_json(input_file,output_file):
    with open(input_file) as f:
        file = [str(i) for i in f.read().split('\n')]
    if file[0][0:4] == 'HTTP' :
        js = answer(file[0])
    else:
        js = question(file[0])

    for i in range(1,len(file)-1, 1):
        if (file[i] == '\n'):
            break
        s = file[i].split(': ',1)
        js.update([(s[0], s[1])])
    with open(output_file, 'w') as f:
        json.dump(js, f, indent=4)

def question(file):
    file = file.split()
    js = dict(method = file[0], uri = file[1], protocol = file[2])
    return js

def answer(file):
    s = ''
    file = file.split()
    js = dict(protocol = file[0], status_code = file[1])
    if file[0] != 'HTTP/2' :
        for i in range(2,len(file), 1):
            s +=' '+file[i]
    js.update(status_message = s)
    return js




if __name__ == '__main__' :
    http_headers_to_json('1.txt','1o.json')
    http_headers_to_json('2.txt','2o.json')
    http_headers_to_json('3.txt','3o.json')
