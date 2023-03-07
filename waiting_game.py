#  Copyright (c) 2023. Daniel Arnold
#  All rights reserved
import random
from timeit import default_timer as timer


def main(targettime):
    print(targettime)
    input('---Press Enter to Begin---')
    input(f'...Press Enter again after {targettime} seconds...')
    start_time = timer()
    input()
    delte_t = timer() - start_time
    print(f'Elapsed time: {delte_t} seconds')
    diff_t = delte_t - targettime
    if diff_t < 0:
        print(f'({abs(diff_t)} to fast)')
    elif diff_t > 0:
        print(f'({abs(diff_t)} to slow)')
    else:
        print('YOU PERFECTLY HIT THE TIME')




if __name__ == '__main__':
    targettime = random.randint(1,5)
    main(targettime)