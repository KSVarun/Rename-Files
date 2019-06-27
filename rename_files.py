import os
import re

dir_path = "/Users/idks/Downloads/MastertheCodingInterviewDataStructures+AlgorithmsCOPY/"
i = 1
for file in os.listdir(dir_path):
    """file_path = os.path.join(dir_path, file)
    with open(file_path, 'r') as file:
        print(file.read())"""
    print(file)
    """inside_dir_path = dir_path+file+"/"
    # print(inside_dir_path)
    for file_inside in os.listdir(inside_dir_path):
        
        # print(file_inside)
        searched_string = re.search(
            '\d+\.(\w*\s)*\w*.mp4$', file_inside)
        print(searched_string)"""

    # for testing
    # print(file)
