import numpy as np


def h1(p, k):
    upper = -((p / k) ** 2)
    ans = np.exp(upper)
    return ans


def h2(p, k):
    down = 1 + ((p / k) ** 2)
    ans = 1.0/down
    return ans


def diffuse(h, k, lamb, top, down, center, left, right):
    ni = left - center
    si = right - center
    ei = top - center
    wi = down - center

    cn = h(np.absolute(ni), k)
    cs = h(np.absolute(si), k)
    ce = h(np.absolute(ei), k)
    cw = h(np.absolute(wi), k)

    second_part = lamb * (cn*ni + cs*si + ce*ei + cw*wi)
    ans = center + second_part

    return ans


def images_path():
    path = ['Images/bunny.jpg', 'Images/textura.jpg', 'Images/fruits_gray.jpg', 'Images/frutas.jpg',
            'Images/hedgehog.jpg', 'Images/lenna.png', 'Images/lion_face.jpg', 'Images/notredame.jpg',
            'Images/puppy.jpg', 'Images/woman_face.jpg']
    return path


