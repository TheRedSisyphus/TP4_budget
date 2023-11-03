import os

bad_hash = 'HEAD'
good_hash = 'c0509c5acef90386f59d729cfcb4c1c3ae03e3d0'
os.system(f'git bisect start {bad_hash} {good_hash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
