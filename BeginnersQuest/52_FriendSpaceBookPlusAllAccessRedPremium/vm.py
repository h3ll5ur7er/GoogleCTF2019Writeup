
import sys
from collections import deque
from pprint import pprint
# Implements a simple stack-based VM
class VM:

  def __init__(self, rom):
    self.cmd_queue = deque(maxlen=50)
    self.rom = rom
    self.accumulator1 = 0
    self.accumulator2 = 0
    self.instruction_pointer = 1
    self.stack = []

  def step(self):
    cur_ins = self.rom[self.instruction_pointer]
    self.instruction_pointer += 1

    fn = VM.OPERATIONS.get(cur_ins, None)

    if cur_ins[0] == '🖋':
      return
    if fn is None:
      raise RuntimeError("Unknown instruction '{}' at {}".format(
          repr(cur_ins), self.instruction_pointer - 1))
    else:
      fn(self)

  def add(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v1 + v2
    self.cmd_queue.appendleft("add {} + {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  def sub(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v2 - v1
    self.cmd_queue.appendleft("sub {} - {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  def if_zero(self):
    if self.stack[-1] == 0:
      while self.rom[self.instruction_pointer] != '😐':
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def if_not_zero(self):
    if self.stack[-1] != 0:
      while self.rom[self.instruction_pointer] != '😐':
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def find_first_endif(self):
    while self.rom[self.instruction_pointer] != '😐':
      self.instruction_pointer += 1

  def jump_to(self):
    marker = self.rom[self.instruction_pointer]
    if marker[0] != '💰':
      print('Incorrect symbol : ' + marker[0])
      raise SystemExit()
    marker = '🖋' + marker[1:]
    self.instruction_pointer = self.rom.index(marker) + 1

    self.cmd_queue.appendleft("jmp {} @ {}".format(marker[1:], self.instruction_pointer))


  def jump_top(self):
    addr = self.stack.pop()
    self.cmd_queue.appendleft("jmp {}".format(addr))
    self.instruction_pointer = addr

  def exit(self):
    print('\nDone.')
    raise SystemExit()

  def print_top(self):
    self.cmd_queue.appendleft("print")
    val = self.stack.pop()
    print("char: '{}' ascii: {} acc1: {} acc2: {}".format(
      chr(val),
      val,
      self.accumulator1,
      self.accumulator2))
    for cmd in self.cmd_queue:
      print("\t", cmd)
    #sys.stdout.write(chr(self.stack.pop()))
    #sys.stdout.flush()

  def push(self):
    if self.rom[self.instruction_pointer] == '🥇':
      self.stack.append(self.accumulator1)
      self.cmd_queue.appendleft("push {} @ {}".format("acc1", self.accumulator1))
    elif self.rom[self.instruction_pointer] == '🥈':
      self.stack.append(self.accumulator2)
      self.cmd_queue.appendleft("push {} @ {}".format("acc2", self.accumulator2))
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop(self):
    if self.rom[self.instruction_pointer] == '🥇':
      self.accumulator1 = self.stack.pop()
      self.cmd_queue.appendleft("pop {} @ {}".format("acc1", self.accumulator1))
    elif self.rom[self.instruction_pointer] == '🥈':
      self.accumulator2 = self.stack.pop()
      self.cmd_queue.appendleft("pop {} @ {}".format("acc2", self.accumulator2))
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop_out(self):
    self.cmd_queue.appendleft("pop /dev/null")
    self.stack.pop()

  def load(self):
    num = 0

    if self.rom[self.instruction_pointer] == '🥇':
      acc = 1
    elif self.rom[self.instruction_pointer] == '🥈':
      acc = 2
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

    while self.rom[self.instruction_pointer] != '✋':
      num = num * 10 + (ord(self.rom[self.instruction_pointer][0]) - ord('0'))
      self.instruction_pointer += 1

    if acc == 1:
      self.accumulator1 = num
    else:
      self.accumulator2 = num
    self.cmd_queue.appendleft("mov acc{} {}".format(acc, num))

    self.instruction_pointer += 1

  def clone(self):
    top = self.stack[-1]
    self.cmd_queue.appendleft("clone top of stack {}".format(top))
    self.stack.append(top)

  def multiply(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v1 * v2
    self.cmd_queue.appendleft("mul {} * {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  def divide(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v2 // v1
    self.cmd_queue.appendleft("div {} / {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  def modulo(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v2 % v1
    self.cmd_queue.appendleft("mod {} % {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  def xor(self):
    v1 = self.stack.pop()
    v2 = self.stack.pop()
    v3 = v2 ^ v1
    self.cmd_queue.appendleft("xor {} ^ {} = {}".format(v1, v2, v3))
    self.stack.append(v3)

  OPERATIONS = {
      '🍡': add,
      '🤡': clone,
      '📐': divide,
      '😲': if_zero,
      '😄': if_not_zero,
      '🏀': jump_to,
      '🚛': load,
      '📬': modulo,
      '⭐': multiply,
      '🍿': pop,
      '📤': pop_out,
      '🎤': print_top,
      '📥': push,
      '🔪': sub,
      '🌓': xor,
      '⛰': jump_top,
      '⌛': exit
  }


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Missing program')
    raise SystemExit()

  with open(sys.argv[1], 'r') as f:
    print('Running ....')
    all_ins = ['']
    all_ins.extend(f.read().split())
    vm = VM(all_ins)

    while 1:
      vm.step()
