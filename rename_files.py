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
    # print(inside_dir_path)
    # print(file)
    path2 = sorted_alphanumeric(os.listdir(inside_dir_path))
    mpfiles = '.*\.mp4'
    digits = '\d+\.'
    # print(path2)
    for file_inside in path2:
        """src=inside_dir_path+file_inside
        str_i = str(i)
        dest=inside_dir_path+str_i+file_inside
        os.rename(src,dest)
        i=i+1"""
        pattern = re.compile(mpfiles)
        matches = pattern.finditer(file_inside)
        # print(file_inside)
        for match in matches:
            str_match = str(match.group(0))
            # print(str_match)
            pattern_digit = re.search(digits, str_match)
            str_digit = str(pattern_digit.group(0))
            # print(type(str_match))
            # print(str_digit + ":" + str_match)
            str_match_updated = str_match.replace(str_digit, str(i))
            i += 1
            # print(inside_dir_path+str_match)
            os.rename(inside_dir_path+str_match,
                      inside_dir_path+str_match_updated)

            # print(i)
            # print(str_match)
        # print(path)
