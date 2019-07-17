<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">Crypto Caulilingo</h1>
<h1 class="glitch glitch__color glitch__color--green">Crypto Caulilingo</h1>
<h1 class="glitch glitch__color glitch__color--blue">Crypto Caulilingo</h1>
<h1 class="glitch glitch__color">Crypto Caulilingo</h1>
<br />
<br />


## Task

Well you've done it, you're now an admin of the Cookie World Order. The clandestine organisation that seeks to control the world through a series of artfully placed tasty treats, bringing folks back in to their idea of what a utopian society would look like. Strangely enough, the webcam data is being fed to understand the properties of the entities you had originally seen. They seem to be speaking back into the camera (an unadvertised microphone) but it's hard to understand what they want. You must- if nothing else ever was important in your life, you must make contact with these beautiful creatures! Also, what exactly is a "cauliflower"?

## RSA
### Key generation
$p$ and $q$ are large prime numbers
the modulus $n$ is calculated as $n = p\ q$

$\lambda(x)$ is [Carmichael's totient function](https://en.wikipedia.org/wiki/Carmichael_function) function
if x is prime, $\lambda(x) = \phi(x) = x-1$
this implies that $\lambda(n) = lcm((p-1)\ (q-1))$

pick $e$ such that $1<e<\lambda(n)$ and $gcd(e, \lambda(n)) = 1$

$d$ is the modular multiplicative inverse of $e\ mod\ \lambda(n)$
therefor $(d*e)\ mod\ \lambda(n) = 1$

the extended euclidean algorithm can be used to calculate $d$ efficiently. 

the public key is composed of $e$ and $n$.
the private key is composed of $d$ and $n$.

### Encryption

to encrypt a cleartext $m$ to cipher $c$
$c = m^e\ mod\ p$

### Decryption

to decrypt cipher $c$ to cleartext $m$
$m = c^d\ mod\ p$

## Solution
Given in the text file are _n_, _e_ and the _msg_

We can assume _n_ to be the RSA modulus $N$, _e_ to be the public key $E$ and _msg_ the ciphertext to decrypt.

From the pdf we know that:
$AP \approx BQ$
$AP + x = BQ$ with $|x| < 10000$
$1 \leq A,B \leq 1000$

We can work out:
$AP + x = BQ$  :arrow_right: $*P$
$AP^2 + xP = BQP = BN$
$AP^2 + xP -  BN = 0$

We now have a second degree polynominal with unknown $P$

We can solve for $P$:
$\Delta = x^2+4ABN$
$P = \frac{-x \pm \sqrt{\Delta}}{2A}$
We know $A$, $B$, $P$ and $Q$ (and therefor $N$ aswell) have to be $\in \N$ 

For $\Delta$ to be $\in \N$ $x^2$ has to be a perfect square. 

Since $x \ll 4ABN$
$\sqrt{\Delta} \in \N$ $\implies$ $\Delta = \lceil \sqrt{4ABN} \rceil ^2$
$x^2 = \Delta - 4ABN = \lceil \sqrt{4ABN}\rceil^2 - 4ABN$

This shows that we only have to bruteforce $A$ and $B$ and check if $\lceil \sqrt{4ABN}\rceil^2 - 4ABN$ is a perfect square to find a solution for $P$

$A$ and $B$ are known to be in the range $[1, 1000]$ so this should be more than feasible.

We use `solver.py` to bruteforce $A$ and $B$, which reveals the [flag](../flags.html#71_cryptocaulilingo).
