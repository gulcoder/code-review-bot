3a4
> import subprocess
6c7
<     subprocess.call("ls -la", shell=True)
---
>     subprocess.run(["ls", "-la"], check=True)
9,10d9
< def duplicate_code():
<     subprocess.call("ls -la", shell=True)
13,17c12,15
< for i in range(0, 10):
<     if i % 2 == 0:
<         logging.info(i)
<     else:
<         logging.info(i)
---
> for i in range(10):
>     if i % 2 == 0:
>         logging.info(f"{i} is even")
>     else:
>         logging.info(f"{i} is odd")