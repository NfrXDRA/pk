import os,sys,time
os.system('clear')
def d(g):
	for n in g+'\n':
		sys.stdout.write(n)
		sys.stdout.flush()
		time.sleep(00000.005)
d('''\033[1;32m	
            .-""""-.       .-""""-.
           /        \     /        \
          /_        _\   /_        _\
         // \      / \\\033[0;32m // \      / \\
         |\__\    /__/| |\__\    /\033[0;32m__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
\033[0;32m    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        \
  /_        _\|  /_        _\|  /_        _\
 // \      / \\ // \      / \\ // \      / \\
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
 jgs  |  |           |  |           |  |
      |  |           |  |           |  |
''')
print ("'repeat number'(",sender,')')
x=input('Start?  [y] [n] :')	
if x =='Y' or 'y' or 'yes' or 'YES':
	while True:
		os.system('clear')
		d('\033[1;36m  __   _       ___   _____       ___   _____   ')
		d('\033[0;36m |  \ | |     /   | |  ___|     /   | |  _  \  ')
		d('\033[1;35m |   \| |    / /| | | |__      / /| | | |_| |  ')
		d('\033[0;35m | |\   |   / / | | |  __|    / / | | |  _  /  ')
		d('\033[1;32m | | \  |  / /  | | | |      / /  | | | | \ \  ')
		d('\033[0;32m |_|  \_| /_/   |_| |_|     /_/   |_| |_|  \_\ ')
		name=input('name    :     ')
		if name == 'reg':
			os.system('mv reg.p /sdcard/')
		elif name == 'coin':
			os.system('mv coins.p /sdcard/')
		elif name == 'invite':
			os.system('mv invite.p /sdcard/')
		elif name == 'del':
			os.system('mv delete.p /sdcard/')
		elif name == 'blog':
			os.system('mv blog.p /sdcard/')