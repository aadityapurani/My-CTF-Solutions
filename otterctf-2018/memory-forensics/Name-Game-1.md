# Name Game 1
Points: 100

Description:
```
We know that the account was logged in to a channel called Lunar-3. what is the account name?

format: CTF{flag}
```

# Solution:

If he is logged in under `Lundar-3` user, it must be present as a string inside the `vmem` file. We use our grepping skills thereafter to search regions near what we want to match

```
$ strings OtterCTF.vmem | grep Lunar-3 -A 2 -B 3
disabled
mouseOver
keyFocused
Lunar-3
0tt3r8r33z3
Sound/UI.img/
--
c+Yt
tb+Y4c+Y
b+YLc+Y
Lunar-3
Lunar-4
L(dNVxdNV
```

We can find out the odd string.

##### CTF{0tt3r8r33z3}
