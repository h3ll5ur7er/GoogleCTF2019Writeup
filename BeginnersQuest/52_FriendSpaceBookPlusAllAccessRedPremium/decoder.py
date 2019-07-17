from sys import stdout

with open("palprimes.txt", "r") as prime_list:
    palprimes = list(map(int, [line for line in prime_list.readlines() if line]))

block1 = [17488,16758,16599,16285,16094,15505,15417,14832,14450,13893,13926,13437,12833,12741,12533,11504,11342,10503,10550,10319,975,1007,892,893,660,743,267,344,264,339,208,216,242,172,74,49,119,113,119,106]
block1_offset = 1

block2 = [98426,97850,97604,97280,96815,96443,96354,95934,94865,94952,94669,94440,93969,93766]
block2_offset = 99



block3 = [101141058,101060206,101030055,100998966,100887990,100767085,100707036,100656111,100404094,100160922,100131019,100111100,100059926,100049982,100030045,9989997,9981858,9980815,9978842,9965794,9957564,9938304,9935427,9932289,9931494,9927388,9926376,9923213,9921394,9919154,9918082,9916239]
block3_offset = 765

def process_block(block, offset):
    r_block = list(reversed(block))
    for i in range(len(block)):
        prime = palprimes[offset + i-1]
        mask = r_block[i]
        stdout.write(chr(prime ^ mask))
        stdout.flush()

process_block(block1, block1_offset)
process_block(block2, block2_offset)
process_block(block3, block3_offset)

print()

