from PIL import Image

def mandelbrot(c: complex, m: int) -> int:
    z = 0
    i = 0
    while abs(z) <= 2:  #terminates if z unstable
        i += 1
        z = z ** 2 + c
        if i == m:
            return m
    return i

assert mandelbrot(0.5, 50) == 5
assert mandelbrot(0.5, 4) == 4

def sample(z1: complex, z2: complex, x: int, y: int, sx: int, sy: int) -> complex:
    xstrecke = z2.real - z1.real
    ystrecke = z2.imag - z1.imag
    xanteil = x / sx
    yanteil = y / sy
    xwert = z1.real + xanteil * xstrecke
    ywert = z1.imag + yanteil * ystrecke
    return complex(xwert, ywert)

assert sample(1+2j, 3+4j, 0, 0, 800, 600) == 1+2j
assert sample(5+6j, 7+8j, 0, 600, 800, 600) == 5+8j
assert sample(9+10j, 11+12j, 800, 0, 800, 600) == 11+10j
assert sample(13+14j, 15+16j, 800, 600, 800, 600) == 15+16j
assert sample(17+18j, 19+20j, 400, 300, 800, 600) == 0.5*(17+18j) + 0.5*(19+20j)

def render_mandelbrot(z1: complex, z2: complex, sx: int, sy: int, m: int, name: str):
    size = (sx, sy)
    img = Image.new('HSV', size)
    for x in range(sx):
        for y in range(sy):
            colour = color(mandelbrot(sample(z1, z2, x, y, sx, sy), m), m)
            img.putpixel((x,y), colour)
    img.convert('RGB').save(name, quality=95)

def color(i: int, max_i: int) -> tuple[int, int, int]:
    hue = int(255 * (i / max_i))
    value = 255 if i < max_i else 0
    saturation = 255
    return (hue, saturation, value)
