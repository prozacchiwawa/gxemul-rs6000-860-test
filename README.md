Test data for gxemul-rs6000-860
===

A fork of gxemul: [gxemul-rs6000-860](https://github.com/prozacchiwawa/gxemul-rs6000-860)

New tests should be added to perform-tests.sh by scripting the emulator and evaluating outputs with compare-image.py via json descriptions.

As time progresses, new forms of evaluation can be added, such as reading the serial port.  Since gxemul runs an xterm-like program to interact over serial, a program is needed to forward or use serial data like this one:

[serialwrap.py](https://gist.github.com/prozacchiwawa/7b56fb606dc95e08b675a31d01057981).

When needed, some disk tools might be added here to be able to check filesystem contents.
