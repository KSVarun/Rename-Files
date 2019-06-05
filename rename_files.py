import os
import re

dir_path = "/Users/idks/Downloads/MastertheCodingInterviewDataStructures+AlgorithmsCOPY/"
i = 1
for file in os.listdir(dir_path):
    """file_path = os.path.join(dir_path, file)
    with open(file_path, 'r') as file:
        print(file.read())"""
    inside_dir_path = dir_path+file+"/"
    for file_inside in os.listdir(inside_dir_path):
        """src=inside_dir_path+file_inside
        str_i = str(i)
        dest=inside_dir_path+str_i+file_inside
        os.rename(src,dest)
        i=i+1"""
        searched_string = re.search('[^\w+].mp4$', file_inside)
        print(searched_string)

    # for testing
    # print(file)
