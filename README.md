# sasl-pp
Pure Python SASL PLAIN Implementation for Impyla and Apache Hive Server 2 Based on the python-sasl API

This pure Python implementation of SASL for Impyla uses the python-sasl API from toddlipcon combined with the pure-sasl implementation from thobbs.

https://github.com/thobbs/pure-sasl

https://github.com/toddlipcon/python-sasl

To allow the Impyla package (pure Python Cloudera Impala client) to connect to Apache Hive, which uses the same hive server 2 server interface it is necessary to have a SASL implementation when using the default Hive configuration, which is to use SASL PLAIN.  Although there is an existing Python sasl package for *nix (python-sasl), it was much more difficult to configure a compatible SASL package for Windows that would work with Impyla as the underlying Cyrus-SASL C code relies on Unix only C libraries.
