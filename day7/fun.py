curr_dir = "hi/abc/def"
split_dir = curr_dir.split("/")
split_dir.pop()
curr_dir = '/'.join(split_dir)
print(curr_dir)