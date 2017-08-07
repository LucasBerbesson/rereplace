# Rereplace

![Travis build](https://travis-ci.org/LucasBerbesson/rereplace.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/rereplace.svg)](https://badge.fury.io/py/rereplace)
[![codecov](https://codecov.io/gh/LucasBerbesson/rereplace/branch/master/graph/badge.svg)](https://codecov.io/gh/LucasBerbesson/rereplace)

Rereplace is a module to transform a string matching a regex A into a string matching a regex B (and vice-versa).  
It automatically detects the regex of the input and transfers it into the other regex format.  

You just need to write down 2 correct regexes with matching named groups and the package will handle the transformations. 

Works with Python 3+

# Getting started

```
pip install rereplace
```

```python

from rereplace import RegexReplace
rer = RegexReplace(r"^(?P<A>\d{2})\.(?P<B>\d{2})$",r"^(?P<B>\d{2})(?P<A>\d{2})$")
rer.replace("01.02")
# => 0201
rer.replace("0201")
# => 01.02
```

It is also possible to reuse some named groups multiple times (unlike the python re module) : 

```python

from rereplace import RegexReplace
rer = RegexReplace(r"^(?P<WORD>.{5})$",r"^(?P<WORD>.{5})(?P<WORD>.{5})(?P<WORD>.{5})$")
rer.replace("HELLO")
# => HELLOHELLOHELLO
rer.replace("HELLOHELLOHELLO")
# => HELLO
```

Other examples : 

```python

from rereplace import RegexReplace
rer = RegexReplace(r"^(?P<WORD1>.{3})-(?P<CODE>\d{3})-(?P<WORD2>.{4})-(?P<CODE2>\d{3})-(?P<WORD3>.{5})$",
                    r"^(?P<WORD1>.{3})/(?P<CODE2>\d{3})/(?P<WORD2>.{4})/(?P<CODE>\d{3})/(?P<WORD3>.{5})$")
rer.replace("ABC-123-ABCD-456-ABCDE")
# => ABC/456/ABCD/123/ABCDE
rer.replace("ABC/456/ABCD/123/ABCDE")
# => ABC-123-ABCD-456-ABCDE
```


```python

from rereplace import RegexReplace
rer = RegexReplace(r"^(?P<DD>\d{2})-(?P<MM>\d{2})-(?P<YYYY>\d{4})$",
                    r"^(?P<MM>\d{2})/(?P<DD>\d{2})/(?P<YYYY>\d{4})$")
rer.replace("31-12-2017")
# => "12/31/2017"
rer.replace("12/31/2017")
# => "31-12-2017"
```


## Lightweight,tested, no dependency