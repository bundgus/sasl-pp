# sasl-pp
Pure Python (Python 3) SASL PLAIN Implementation for Impyla and Apache HiveServer2 Based on the python-sasl API

This pure Python implementation of SASL for Impyla uses the python-sasl API from toddlipcon combined with the pure-sasl implementation from thobbs.

https://github.com/cloudera/impyla

https://github.com/thobbs/pure-sasl

https://github.com/toddlipcon/python-sasl

To allow the Impyla package (pure Python Cloudera Impala client) to connect to Apache Hive, which uses the same HiveServer2 server interface as Impala it is necessary to have a SASL implementation when using the default Hive configuration, which uses SASL PLAIN.  Although there is an existing Python sasl package for *nix (python-sasl), it was much more difficult to configure a compatible SASL package for Windows that would work with Impyla as the underlying Cyrus-SASL C code relies on Unix only C libraries.

This drop-in replacement for python-sasl does not require any modifications to Impyla, but does depend on the pure-sasl package.

Tested on Python 3.5 (Anaconda)
