#!/usr/bin/python3

from PIL import Image, ImageDraw

im_artix = Image.open("images/artix_tuxo.png")
im_debian = Image.open("images/debian_tuxo.png")

cd_center = (418, 397)
cd_radius = 109
elipse_pos1 = (cd_center[0] - cd_radius, cd_center[1] - cd_radius)
elipse_pos2 = (cd_center[0] + cd_radius, cd_center[1] + cd_radius)

steps = 40
step_size = 360 / steps
gif_images = []

def cycle(im_from, im_to):
    degree = 0
    for step in range(steps):
        degree -= step_size
        mask = Image.new("1", im_artix.size)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([elipse_pos1, elipse_pos2], degree, 0, fill="white")
        res = Image.composite(im_from, im_to, mask)
        gif_images.append(res)


cycle(im_artix, im_debian)
cycle(im_debian, im_artix)

gif_images[0].save(
    "out.gif", append_images=gif_images[1:], save_all=True, duration=50, loop=0
)
