#!/usr/bin/env python3
import os
from MyQR import myqr
version, level, qr_name = myqr.run(
	'https://vincent0628.github.io/pinjie_2022_0214/',
    version=1,
    level='H',
    picture='pic-icon.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='ip_pinjie_2022_0214.png',
    save_dir=os.getcwd()
)
print('version',version)
print('level',level)
print('qr_name',qr_name)
# os.system('pause')
