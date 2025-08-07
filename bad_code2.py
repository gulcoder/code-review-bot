1c1
< # bad_code2.py
---
> # improved_code.py
3a4
> import logging
6c7
<     subprocess.call("ls -la", shell=True)
---
>     subprocess.call(["ls", "-la"])
9,10d9
< def duplicate_code():
<     subprocess.call("ls -la", shell=True)
13,17c12,13
< for i in range(0, 10):
<     if i % 2 == 0:
<         logging.info(i)
<     else:
<         logging.info(i)
---
> # Korrekt loggning av i
> for i in range(0, 10):