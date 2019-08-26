import sys
num_steps = int(sys.argv[1])


def steps(step):
    for i in range(1,step+1):
        print(" "*(step-i)+"#"*i)


steps(num_steps)

