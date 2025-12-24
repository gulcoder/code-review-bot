3a4
> import logging
9,10d9
< def duplicate_code():
<     subprocess.call("ls -la", shell=True)
13,17c12,14
< for i in range(0, 10):
<     if i % 2 == 0:
<         logging.info(i)
<     else:
<         logging.info(i)
---
> logging.basicConfig(level=logging.INFO)
> 
> for i in range(10):
>     parity = "even" if i % 2 == 0 else "odd"
>     logging.info(f"{i} is {parity}")