<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">FriendSpaceBookPlusAllAccessRedPremium</h1>
<h1 class="glitch glitch__color glitch__color--green">FriendSpaceBookPlusAllAccessRedPremium</h1>
<h1 class="glitch glitch__color glitch__color--blue">FriendSpaceBookPlusAllAccessRedPremium</h1>
<h1 class="glitch glitch__color">FriendSpaceBookPlusAllAccessRedPremium</h1>
<br />
<br />

## Task
Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com"  But unbeknownst to you, it was only the  700nm Wavelength herring rather than a delicious cookie that you could have found.   It looks exactly like a credential for another system.  You find yourself in search of a friendly book to read.

Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here.  It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

But not much Cauliflower here.  They must be very private creatures.  SarahH has left open some proprietary tools, surely running this will take you to them.  Decipher this language and move forth!

[Attachment](https://storage.googleapis.com/gctf-2019-attachments/775e97ff94e7dfe79293b62abed7e1ad17cdc6ebc82c4873cdca201c40569624)


## Solution
The program is in a emoji based instruction set.
The vm runs the program, but the output is generated extremely slowly.
printing out the vm's state when characters are printed shows there are palindromic primes calculated.
There are 3 sections in the program that push a bunch of data onto the sack.
the data on the stack is xored with the palPrimes to reveal the next charcter.
`decoder.py` contains the data on the stack combined with the palPrime offset. `palprimes.txt` contains a large list of palindromic prime numbers.
the compleed algorithm prints `http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/`.
The page of `Amber` contains the [flag](../flags.html#52_friendspacebookplusallaccessredpremium)
