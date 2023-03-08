# Process

```python
# run bash subprocesses
import subprocess
subprocess.run('echo "hello world"', shell=True)
# subprocess.Popen also works but it's said to be low-level
process = subprocess.Popen(cmd, shell=True) # return PID of subprocess
[3] https://qa.try2explore.com/questions/11285153
```

## Reference

\[1] [https://stackoverflow.com/questions/4256107/running-bash-commands-in-python/51950538](https://stackoverflow.com/questions/4256107/running-bash-commands-in-python/51950538)

\[2] [https://www.saltycrane.com/blog/2011/04/how-use-bash-shell-python-subprocess-instead-binsh/](https://www.saltycrane.com/blog/2011/04/how-use-bash-shell-python-subprocess-instead-binsh/)

\[3] [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)

\[4] [https://qa.try2explore.com/questions/11285153](https://qa.try2explore.com/questions/11285153)
