
<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">Work computer</h1>
<h1 class="glitch glitch__color glitch__color--green">Work computer</h1>
<h1 class="glitch glitch__color glitch__color--blue">Work computer</h1>
<h1 class="glitch glitch__color">Work computer</h1>
<br />
<br />

## Task
With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer. This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things. Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings? Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party? SarahH, who appears to be a programmer with several clients, has left open a terminal. Oops. Sorry clients! Aliens will be poking around attempting to access your networks.. looking for Cauliflower. That is, *if* they can learn to navigate such things.

`readme.ctfcompetition.com 1337`

## Solution 1
The cat command doesn't seem to exist.
busybox can't be called directly.
- `env busybox cat README.flag` reveals the first [flag](../flags.html).

## Solution 2
`ORME.flag` is still not accessible.
by changing the file security attributes using `env busybox chmod 777 ORME.flag` we now have full access.
the second [flag](../flags.html) can be found using `env busybox cat ORME.flag`
