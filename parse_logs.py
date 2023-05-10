from glob import glob
import json

files = glob('openfold*')

dictionary = {}
for log in files:
    with open(log, 'r') as file:
        d = dict()
        for line in file.readlines():
            if 'Running inference' in line:
                id = line.split(' ')[-1].split('-')[0]

            if 'Inference time:' in line:
                d['Inference'] = line.split(' ')[-1][:-1]


            if 'Relaxation time:' in line:
                d['Relaxation'] = line.split(' ')[-1][:-1]

                if len(d)!=2:
                    print(d)
                    raise Exception('Log format is not right')
                
                dictionary[id] = d
                d = dict()


with open("times.json", "w") as outfile:
    json.dump(dictionary, outfile)