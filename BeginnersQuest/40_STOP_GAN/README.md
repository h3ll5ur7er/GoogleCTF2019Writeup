<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">STOP GAN</h1>
<h1 class="glitch glitch__color glitch__color--green">STOP GAN</h1>
<h1 class="glitch glitch__color glitch__color--blue">STOP GAN</h1>
<h1 class="glitch glitch__color">STOP GAN</h1>
<br />
<br />

## Task
Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

`buffer-overflow.ctfcompetition.com 1337`

[Attachment](https://storage.googleapis.com/gctf-2019-attachments/4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a)

## Solution 1
`console.c` contains a comment that says 
> Crashing bof will trigger the 1st flag.

ok, so if we insert a lot of input data, we should be able to crash that thing.. using `python3 -c "print('a'*1024)"` we can generate a lot of input data. copy pasting lots of 'a's into the application causes a seg fault, which reveals the first [flag](../flags.html#40_stop_gan).

## Solution 2
`console.c` contains another comment that states
> Controlling the buffer overflow in bof will trigger the 2nd flag.

Using Ghidra to look at the program shows, the new return address and offset to overwrite the old return address on the stack.

using `overflow.py` we get the second [flag](../flags.html#40_stop_gan).
