#  Copyright (c) 2023. Daniel Arnold
#  All rights reserved
import sys

EXAMPLE = [[[1,2,3],2,[1,3]],[1,2,3],2]

def index_all(search_list:list, search_entry):
    inds = []
    for pos, ent in enumerate(search_list):
        if ent == search_entry:
            inds.append([pos])
        elif isinstance(ent, list):
            for i in index_all(ent, search_entry):
                inds.append([pos]+i)
    return inds


def main(*args):
    return index_all(EXAMPLE, 2)


if __name__ == '__main__':
    indices = main(sys.argv[1:])
    print('result:', indices)