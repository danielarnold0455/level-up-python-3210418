#  Copyright (c) 2023. Daniel Arnold
#  All rights reserved
import json
import os
import pathlib


def write_data(data:dict, filename:pathlib.Path):
    with filename.open(mode='w') as fh:
        json.dump(data, fh)


def read_data(filename:pathlib.Path):
    with filename.open(mode='r') as fh:
        return json.load(fh)


def main():
    filename = pathlib.Path().cwd() / 'data.json'
    testdata = {'a': 1, 'b': {'c': 2}}

    write_data(testdata, filename)

    print(f're-read data: {read_data(filename)}')



if __name__ == '__main__':
    main()