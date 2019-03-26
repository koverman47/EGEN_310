#!/usr/bin/env python3

import sys
import paramiko
from configurations import *


host = "zeropythirty"
ip = "10.152.183.190"
user = "pi"
passw = "pi"

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=user, password=passw)
except BadHostKeyException:
    print("Host could not be found.")
    sys.exit(0)
except AuthenticationException:
    print("Host could not be found")
    sys.exit(0)
except SSHException:
    print("Unkown SSH error.")
    sys.exit(0)

try:
    while True:
        result = None
        result = ssh.exec_command()
except KeyboardInterrupt:
    pass
except NotImplementedError:
    pass
except SSHException:
    if result:
        print(result)
    else:
        print("Unkown SSH error.")
finally:
    ssh.close()
    config.close()
    sys.exit(0)
