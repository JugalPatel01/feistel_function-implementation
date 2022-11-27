# Implementation of Fiestel function

- A **Feistel cipher**(also known as **Luby–Rackoff** block cipher) is a **symmetric
  key cipher** used in the construction of block ciphers.
- Feistel cipher is working on simple principle of exor that exor's inverse function is exor itself
````key ⊕ key = 0```` or
````data ⊕ key ⊕ key = data````
- Feistel function **uses invertible components** like : exclusive-or,circular
  shift, complement,etc... and **non invertible components** like : and
  operation, or operation, right shift operation, etc...
- Many ciphers like : DES, Blowfish, Triple DES, Lucifer, RC5, etc... are
  using feistel function implementation.
- For more you can visit on the [WikiPedia Page of Feistel cipher](https://en.wikipedia.org/wiki/Feistel_cipher)

---

### You can also make you own Feistel function Like

````
def comjfun (a,b) :
  ac = complement (a)
  bc = complement (b)
  ac = lshift_str (ac,5)
  bc = rshift_str (bc,5)
  bc = lshift_str (bc,5)
  ac = com_and_num (ac,bc)
  bc = com_or_num (ac,bc)
  ans = bin (int(ac,2) ˆ int(bc,2))
  return ans[2:]

````
---
## Feistel cipher working on the simple mechanism that shown in the below figure
![image](https://user-images.githubusercontent.com/57848389/205368456-35363da1-aa39-4dad-b9e6-51e7cee5c50b.png)

