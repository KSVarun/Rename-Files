import os
import re


def sorted_alphanumeric(data):
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


dir_path = "/Users/idks/Downloads/MastertheCodingInterviewDataStructures+AlgorithmsCOPY/"
i = 1
path = sorted_alphanumeric(os.listdir(dir_path))
for x in path:
    if(x == '.DS_Store'):
        path.remove(x)

for file in path:
    """file_path = os.path.join(dir_path, file)
    with open(file_path, 'r') as file:
        print(file.read())"""
    # if(file != '.DS_STORE'):

    inside_dir_path = dir_path+file+"/"
    # print(file)
    path2 = sorted_alphanumeric(os.listdir(inside_dir_path))
    mpfiles = '\d+\.(\w*\s)*\w*.mp4$'
    # print(path2)
    for file_inside in path2:
        pattern = re.compile(mpfiles)
        matches = pattern.finditer(file_inside)
        for match in matches:
            print(match)
