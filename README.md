# EGEN 310 - Multidisciplinary Design

## Understanding this project

### Primary files for consideration
- main.py
  - Primary Client executable file
  - Establishes SSH
  - Creates GUI
  - Loops over controller and gui events
- appy.py
  - Primary file for GUI
- nav.py
  - TkInter label with controller object
- configurations/config\*.py
  - Four separate configuration options for the controller
- reader.py
  - Primary Host executable file
  - Read stdin over ssh and write to Raspberry Pi GPIO

### Other files
- tests
  - Miscellaneous tests used for exploration and ideation

### Resources Used
- [pygame](https://www.pygame.org/news)
- [TkInter](https://wiki.python.org/moin/TkInter)
- [iNNext Controller](https://www.amazon.com/gp/product/B07474JYNX/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- [Paramiko](http://www.paramiko.org)
- [Python3](https://www.python.org/downloads/release/python-361/)
- [RPi GPIO](https://pypi.org/project/RPi.GPIO/)
- [pigpio](http://abyz.me.uk/rpi/pigpio/)
- [Raspberry Pi Pinouts](https://pinout.xyz)
- [VLC](https://pypi.org/project/python-vlc/)
