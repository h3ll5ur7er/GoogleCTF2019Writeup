<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">Home computer</h1>
<h1 class="glitch glitch__color glitch__color--green">Home computer</h1>
<h1 class="glitch glitch__color glitch__color--blue">Home computer</h1>
<h1 class="glitch glitch__color">Home computer</h1>
<br />
<br />

## Task
Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.

[Attachment](https://storage.googleapis.com/gctf-2019-attachments/86863db246859897dda6ba3a4f5801de9109d63c9b6b69810ec4182bf44c9b75)

## Solution
Mount the given ntfs volume using `mount -t ntfs family.ntfs ./family`.
The user's `Documents` directory could be interesting, use `cd family/Users/Family/Documents` to navigate there.
use `ls` to list all files.
> credentials.txt  creds.png  document.pdf  preview.pdf

This looks too easy.. Looking at `credentials.txt` using the command `cat ./credentials.txt` reveals:
> I keep pictures of my credentials in extended attributes.

Ok, so we look at the extended attributes of `credentials.txt` using `getfattr ./credentials.txt`
which reveals.

> \# file: credentials.txt
> user.FILE0

Let's look at the data..
```getfattr --only-values -n user.FILE0 credentials.txt | head | xxd -c16 | head```

> ```00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR```
> ```00000010: 0000 04d2 0000 0153 0802 0000 0073 b9b6  .......S.....s..```
> ```00000020: 5e00 0000 0373 4249 5408 0808 dbe1 4fe0  ^....sBIT.....O.```
> ```00000030: 0000 0019 7445 5874 536f 6674 7761 7265  ....tEXtSoftware```
> ```00000040: 0067 6e6f 6d65 2d73 6372 6565 6e73 686f  .gnome-screensho```
> ```00000050: 74ef 03bf 3e00 0020 0049 4441 5478 9cec  t...>.. .IDATx..```
> ```00000060: dd79 600c f7ff 07fe d9dc f7e1 48dc 672e  .y`.........H.g.```
> ```00000070: 399a b8e3 6888 a884 24d4 11c4 d96a b54a  9...h...$....j.J```
> ```00000080: 5bea a84f dd55 75ab 1eaa 14a5 6804 5514  [..O.Uu.....h.U.```
> ```00000090: 7155 8420 2134 21c4 1121 a808 09b9 afcd  qU. !4!..!......```

Looks like a png image.. when piping the content into a file using `getfattr --only-values -n user.FILE0 credentials.txt > c.png` we get a image containing the [flag](../flags.html#20_homecomputer).

