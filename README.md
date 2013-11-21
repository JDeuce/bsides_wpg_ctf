BSides Winnipeg CTF
===================

other answers
-------------
DJSBX already has a [great writeup](https://github.com/DJSymBiotiX/bsideswpg_ctf/)
for most of the problems.

I added a few of my interesting solutions here, as well as
bootliqour and cosmo which he didn't touch.

tapdat
------
The key is to realize it is a linear shift register.
Once you figure that out you just need to determine the mapping used from bits to lit up segments.

Turns out you only need to do one cycle of the shift register, but
when I approached this problem I thought there could be multiple cycles,
so my solution ended up being way too complicated.

I solved this with 2 scripts:

1. Some python code in /tapdat/ that generates a JSON file that contains
the binary output for the first million possible shift register states.
See [here](tapdat/tapdat.py)

2. A jsfiddle that creates an HTML interface for viewing the output of various states.
I figured this would be easier to write than the same code in python.  http://jsfiddle.net/tfm8U/4/

rascal
------
This one was just a complicated one liner in haskell.
I didn't know haskell very well so I had to read a few quick guides.
Once I figured out what it was doing, I dropped into python
and wrote another complicated liner that can solve it.

See [here](rascal/rascal.py)


bootliquor
----------
The first step in this challenge is identifying the unknown binary.
When dealing with unknown files, it's best to start with the file command.

```shell
$ file bootliqour.img
bootliquor.img: x86 boot sector, code offset 0x30
```

Once I knew it was a boot sector, I went ahead and booted it just like
demo, by configuring VirtualBox to boot it as a floppy disk.

Upon booting the bianry you are greeted with a prompt.
Typing something into the prompt returns the string Lose.

Ok so we're going to have to figure out what's inside this image.
I was able to get a disassembly with the following command:

```shell
$ objdump -D -b binary -mi386 -Maddr16,data16 bootliquor.img > dump.txt
```

I then proceeded to analyze the assembly to figure out which string
would make the program output "Win".

I've added my disassembly with some helpful commands to in [dump.txt](bootliqour/dump.txt)


cosmo
-----
I didn't quite get cosmo during the competition, but I tried quite hard
and cussed Mak out quite a bit.

I decided to run the png through imagemagick, to see what it did to the filesize.
```shell
convert cosmo.png output.png
```

Output.png was about 6k smaller than cosmo.png, so I knew there had to be something
it was throwing out.

With nowhere else to turn, I quickly glanced through the PNG spec here
http://www.libpng.org/pub/png/spec/1.0/PNG-Contents.html and learned that
png allows for private, ancillary chunks that can be marked as safe to ignore.

So I went ahead and installed pypng, a python module for reading into PNGs
```shell
pip install pypng
```

And then I wrote a quick script, get_chunks.py to pull out the indvidual chunks.

```shell
python get_chunks.py
```

See [get_chunks.py](cosmo/get_chunks.py)

Looking inside the chunks I found a bunch of seemingly random chunks of base64 data.
Pulling it out and decoding the base64 didn't lead me anywhere.

Looking closer at the chunks you can find a non-base64 character after the first 2 bytes.
So I thuoght there might be something interesting in those first 2 bytes.

```shell
$ for file in chunk.*; do head -c 2 $file; done
tso_ecny_sTomare
```

The string `tso_ecny_sTomare` is an anagram for the solution.
I got stuck trying to find something with one_star or no_star during the competition,
but as Mak pointed out the T is capatalized and is a pretty big hint that
it should be at the beginning.

I'll leave it to the reader to find the final answer.

