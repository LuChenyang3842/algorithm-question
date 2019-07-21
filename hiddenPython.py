
print('\n'.join([''.join([('LiuLiuNo.1 '[(x-y) % len('liuliuNo.1 ')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))