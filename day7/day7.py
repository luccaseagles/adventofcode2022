from collections import defaultdict
import time
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
subdirs = {}
dirs_size = defaultdict(int)
with open('input', 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines if l != '$ ls\n' ]
    curr_dir = ''
    for l in lines:
        tokens = l.split()
        if tokens[0]  == "$":
            if tokens[2] == "..":
                split_dir = curr_dir.split("/")
                split_dir.pop()
                curr_dir = '/'.join(split_dir)
            else:
                curr_dir = curr_dir + "/"+ tokens[2] 
            
        elif tokens[0] == "dir":
            subdirs.setdefault(curr_dir, []).append(curr_dir + "/"+ tokens[1] )
        else:
            dirs_size[curr_dir] += int(tokens[0]) 

def get_size(root_dir):
    if root_dir in subdirs.keys():
        for subdir in subdirs[root_dir]:
            dirs_size[root_dir] += get_size(subdir)
    return dirs_size[root_dir] 

size = get_size('//')
print(dirs_size)

print(sum([v for v in dirs_size.values() if v < 100000]))

free_space = 70000000 -dirs_size['//']
space_to_clear = 30000000 - free_space

filt_sizes = {k: v for (k,v) in dirs_size.items() if v > space_to_clear}
dir = min(filt_sizes, key=filt_sizes.get)
print(dirs_size['///fvhmzqc/wrzzq/mqqlhnvh'])


