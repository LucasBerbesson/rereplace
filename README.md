# Rereplace

Rereplace is a module to transform a string matching a regex A into a string matching a regex B (and vice-versa).  
It automatically detects the regex of the input and transfers it into the other regex format.  

You just need to write down 2 correct regexes with matching named groups and the package will handle the transformations. 

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

