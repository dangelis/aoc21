
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


gamma_rate = []
epsilon_rate = []

for n in range(num_bits):
    total_1s = 0
    total_0s = 0
    for i in bit_list[n]:
        if i == "1":
            total_1s = total_1s + 1
        else:
            total_0s = total_0s + 1
    
    if total_1s > total_0s:
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")
    
    print(f"For bit {n}, total 0s: {total_0s}, total 1s: {total_1s}, gamma_rate: {gamma_rate}, epsilon_rate: {epsilon_rate}")


gamma_dec = binaryToDecimal("".join(gamma_rate))
epsilon_dec = binaryToDecimal("".join(epsilon_rate))

print(f"product: {gamma_dec * epsilon_dec}")

