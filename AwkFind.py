__author__ = 'nipunchawla'

import subprocess as sb

sb.Popen(['ls -la | grep -i L'], shell=True)




import subprocess
import shlex
proc1 = subprocess.Popen(shlex.split('ps cat'),stdout=subprocess.PIPE)
proc2 = subprocess.Popen(shlex.split('grep python'),stdin=proc1.stdout,
                         stdout=subprocess.PIPE,stderr=subprocess.PIPE)

proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
out,err=proc2.communicate()
print('out: {0}'.format(out))
print('err: {0}'.format(err))


#sb.Popen('grep -i --line-buffered grave data/*.txt', shell=True)
