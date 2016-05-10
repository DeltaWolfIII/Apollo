import sys
import subprocess

if sys.version_info[0] <= 3:
	subprocess.Popen("python py2.py", shell=True).communicate()
if sys.version_info[0] >= 3:
	subprocess.Popen("python3 py3.py", shell=True).communicate()