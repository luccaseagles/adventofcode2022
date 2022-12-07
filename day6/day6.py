
with open("input", "r") as f:
    lines = f.readlines()
    code = lines[0]
    N = 14
    candidate_markers = [set(code[i-N:i]) for i in range(N,len(code))]
    marker_idx = 0
    for i,candidate in enumerate(candidate_markers):
        if len(candidate) == N:
            marker_idx = i+N
            break
    print(marker_idx)