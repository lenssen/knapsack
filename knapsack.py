
with open('ps1_cow_data.txt') as f:
    read = f.readlines()
    for line in read:
        stripped_line = line.rstrip('\n')
        split = stripped_line.split(',')
        it = iter(split)
        res_dct = dict(zip(it, it))

        print(res_dct)
    f.close()
