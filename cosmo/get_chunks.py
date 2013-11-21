import base64
import png

reader = png.Reader("cosmo.png")

data = ""
i = 1
for c in reader.chunks():
    if c[0] == "miME":
        with open("chunk.%d" % i, "w") as f:
            data = "".join(c[1].split())
            print i, len(data)
            f.write(data)
            i += 1
