
from math import ceil
from sympy import integer_nthroot, isprime
isqrt = lambda x: integer_nthroot(x, 2)

n = 17450892350509567071590987572582143158927907441748820483575144211411640241849663641180283816984167447652133133054833591585389505754635416604577584488321462013117163124742030681698693455489404696371546386866372290759608301392572928615767980244699473803730080008332364994345680261823712464595329369719516212105135055607592676087287980208987076052877442747436020751549591608244950255761481664468992126299001817410516694015560044888704699389291971764957871922598761298482950811618390145762835363357354812871474680543182075024126064364949000115542650091904557502192704672930197172086048687333172564520657739528469975770627

e = 65537

msg = 0x50fb0b3f17315f7dfa25378fa0b06c8d955fad0493365669bbaa524688128ee9099ab713a3369a5844bdd99a5db98f333ef55159d3025630c869216889be03120e3a4bd6553d7111c089220086092bcffc5e42f1004f9888f25892a7ca007e8ac6de9463da46f71af4c8a8f806bee92bf79a8121a7a34c3d564ac7f11b224dc090d97fdb427c10867ad177ec35525b513e40bef3b2ba3e6c97cb31d4fe3a6231fdb15643b84a1ce704838d8b99e5b0737e1fd30a9cc51786dcac07dcb9c0161fc754cda5380fdf3147eb4fbe49bc9821a0bcad98d6df9fbdf63cf7d7a5e4f6cbea4b683dfa965d0bd51f792047e393ddd7b7d99931c3ed1d033cebc91968d43f

def partition(l, x):
    for i in range(len(l)//x):
        a = ""
        for c in range(x):
            a += l[i*x + c]
        yield a

def decode(value):
    gen = partition(value, 2)
    a = "b'"
    for t in gen:
        a += "\\x"+t
    a += "'"
    return eval(a).decode()

def solve(a, b, x):
    delta = x**2 + 4*a*b*n
    sqrt_delta = isqrt(delta)[0]

    for sign_x in [-1, 1]:
        for sign_delta in [-1, 1]:
            p = (sign_x * x + sign_delta * sqrt_delta)//(2*a)
            if isprime(p):
                return p, n//p

def check(a,b):

    delta_approx = 4*a*b*n
    root = isqrt(delta_approx)[0]+1
    root_squared = root**2
    candidate = isqrt(root_squared- delta_approx)

    if candidate[1]:
        p, q = solve(a,b, candidate[0])
        return p, q
    return None, None


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('no muliplicative inverse mod n found')
    else:
        return x % m

def loop():
    for a in range(1, 1001):
        for b in range(1, 1001):
            p, q = check(a, b)
            if p is not None:
                l = (p-1)*(q-1)
                d = modinv(e, l)
                cleartext = pow(msg, d, n)
                print("decrypted ", decode(hex(cleartext)[2:]))
                return cleartext
    print("key not found")

if __name__ == "__main__":
    loop()
