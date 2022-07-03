import json

# inp = json.loads(input())
# inp = [{"name": "A", "parents": []},
#        {"name": "B", "parents": ["A", "C"]},
#        {"name": "C", "parents": ["A"]}]
inp = [{"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]
# inp = json.loads(inp_)
# dfgre : 3
# gsd : 2
# gsdfgre : 4
# hsdgreg : 1
'''
inp = [{"name": "B", "parents": ["A", "C"]},
       {"name": "C", "parents": ["A"]},
       {"name": "A", "parents": []},
       {"name": "D", "parents":["C", "F"]},
       {"name": "E", "parents":["D"]},
       {"name": "F", "parents":[]}] 
'''
# A : 5
# B : 1
# C : 4
# D : 2
# E : 1
# F : 3
# data_py = json.loads(inp)

'''inp = [  # тестовый граф наследования в виде json-объекта
    {'name': 'G', 'parents': ['F']},  # сначала отнаследуем от F, потом его объявим: корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B', 'C']},
    {'name': 'E', 'parents': ['D']},
    {'name': 'F', 'parents': ['D']},
    # а теперь другая ветка наследования
    {'name': 'X', 'parents': []},
    {'name': 'Y', 'parents': ['X', 'A']},  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    {'name': 'Z', 'parents': ['X']},
    {'name': 'V', 'parents': ['Z', 'Y']},
    {'name': 'W', 'parents': ['V']},
]'''

# A : 10
# B : 5
# C : 5
# D : 4
# E : 1
# F : 2
# G : 1
# V : 2
# W : 1
# X : 5
# Y : 3
# Z : 3

# inp = [{"name": "G", "parents": ["ZZZ"]}, {"name": "TH", "parents": ["ZZZ"]}, {"name": "G", "parents": ["ZY"]}, {"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]
# A : 10
# B : 5
# C : 5
# D : 4
# E : 1
# F : 2
# G : 1
# TH : 1
# V : 2
# W : 1
# X : 5
# Y : 3
# Z : 3
# ZY : 2
# ZZZ : 3
classes = {}
for dicts in inp:
    for par in dicts['parents']:
        if par not in classes or classes[par] == 0:
            classes[par] = set()
            classes[par].add(dicts['name'])
        else:
            classes[par].add(dicts['name'])
    if dicts['name'] not in classes:
        classes[dicts['name']] = 0

final = {}
print(classes)



def recur(node, start):
    global visited
    if classes[node] != 0:
        if start not in final:
            final[start] = classes[node]
        else:
            final[start].update(classes[node])
        for j in list(classes[node]):
            print(j)
            if j not in visited:
                visited.append(j)
                print(f'j: {j}')
                recur(j, start)
    else:
        final[node] = 0


for parent in classes:
    print(parent)
    visited = []
    recur(parent, parent)

for ans in sorted(final.keys()):
    if final[ans] == 0:
        print(f'{ans} : {1}')
    else:
        print(f'{ans} : {len(final[ans]) + 1}')
