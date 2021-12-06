
def read_input():
    lines = None
    with open('input.txt') as f:
    # with open('test.txt') as f:
        lines = f.readlines()

    if lines == None:
        exit
    else:
        return lines   

# From https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
def binaryToDecimal(n):
    return int(n,2)

# Create a new list from bit_list (column based data) with only values from the index_list
def purge(index_list, bit_list):
    # print(f"purging index list {index_list} from bit_list: {bit_list}")

    purged = [None] * num_bits

    for col in range(len(bit_list)):
        purged[col] = []

        for idx in index_list:
            purged[col].append(bit_list[col][idx])


    # print(f"purged bit list now: {purged}")

    return purged


# Recursively apply the bit criterea starting from bit "msb".
# max_or_min is the toggle for o2 or co2 (1 is o2)
# bit_list is a list of lists.. a columnar view of the data so that bit_list[0] is a list of the first digits in all the rows
def process(bit_list, msb, max_or_min):
    num_bits = len(bit_list)

    most_common = 0
    least_common = 0

    one_idx_list = []
    zero_idx_list = []

    total_1s = 0
    total_0s = 0

    row_idx = 0
    for i in bit_list[msb]:
        if i == "1":
            total_1s = total_1s + 1
            one_idx_list.append(row_idx)
        else:
            zero_idx_list.append(row_idx)
            total_0s = total_0s + 1
        row_idx = row_idx + 1

    if total_1s > total_0s or total_1s == total_0s:
        most_common = 1
    else:
        most_common = 0


    if most_common == 1:
        o2_index_list = one_idx_list
        co2_index_list = zero_idx_list
    else:
        o2_index_list = zero_idx_list
        co2_index_list = one_idx_list
        
    new_data = []
    if max_or_min == 1:
        new_data = purge(o2_index_list, bit_list)
    else:
        new_data = purge(co2_index_list, bit_list)


    print(f"msb now {msb}, num_bits: {num_bits}")
    if msb < num_bits - 1:
        print(f"calling process with msb {msb + 1}")

        # Make sure there's more than one row
        if len(new_data[0]) > 1:
            new_data = process(new_data, msb + 1,  max_or_min)
    
    return new_data

# We end up with a weird list structure like [['0'], ['1'], ['0'], ['1'], ['0']], unwravel it to the decimal form
def unwravel(bit_list):
    row_as_list = []
    for n in bit_list:
        row_as_list.append(n[0])

    return binaryToDecimal("".join(row_as_list))




data = read_input()


num_bits = len(data[0].strip())

print(f"num_bits: {num_bits}")

bit_list = [None] * num_bits

# Declare/init columns (list) for each bit
for n in range(num_bits):
    bit_list[n] = []

for line in data:
    for n in range(num_bits):
        bit_list[n].append(line[n])


# print(f"bit_list: {bit_list}")

o2 = process(bit_list, 0, 1)
co2 = process(bit_list, 0, 0)

print(f"o2 rate: {o2}")
print(f"co2 rate: {co2}")

print(f"unwravelled: {unwravel(o2)}")


o2_dec = unwravel(o2)
co2_dec = unwravel(co2)

print(f"product: {o2_dec * co2_dec}")

# 2990784