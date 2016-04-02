__author__ = 'nichawla'

import subprocess

com_str='uname -a'
command=subprocess.Popen([com_str],stdout=subprocess.PIPE,shell=True)
(output,error)=command.communicate()
print output