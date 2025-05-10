data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]


for idx, (op, cl) in enumerate(data):
    if idx == 0:
        data[idx].append('')
    else:
        # we have to watch out here, since we appended an extra element to the previous
        # row in the previous iteration, we now actually have 3 values to unpack!
        prev_op, prev_cl, trend = data[idx-1]
        if op > prev_cl:
            data[idx].append('up')
        elif op < prev_cl:
            data[idx].append('down')
        else:
            data[idx].append('same')
print(data)