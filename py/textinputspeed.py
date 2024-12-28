from time import *
import random as r

data = ['i am pias this is my new projet to track time speed', 'its been a long day without you my friend']
test = r.choice(data)
def typing(inp):
    erorr = 0
    for i,j in zip(data,inp):
        if i != j :
            erorr += 1
        erorr +=1

    return erorr

print(test)
print()
start_time = time()
inp = input('type')
end_time = time()
print(f'Time taken: {round(end_time - start_time)} seconds')
erorrs= typing(inp)

print(f'Total errors: {erorrs}')
