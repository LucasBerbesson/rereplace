import re


class _FormatDict(dict):
    """
    Override of the dict class to handle non existing keys
    """

    def __missing__(self, key):
        """
        :param key: key asked for the dict instance
        :return: the key in brackets instead of an error message
        """
        return "{%s}" % key


class RegexReplace():
    def __init__(self, regexA, regexB):

        self.regexA = regexA
        self.regexB = regexB

        self.argsA = self.find_args(regexA)
        self.argsB = self.find_args(regexB)

        self.cleaned_regexA = self.clean_regex(regexA, self.argsA)
        self.cleaned_regexB = self.clean_regex(regexB, self.argsB)

        self.formatA = self.regex_to_stringformat(self.regexA)
        self.formatB = self.regex_to_stringformat(self.regexB)

    @staticmethod
    def find_args(regex):
        return re.findall(r'\<([^\)]+)\>', regex)

    @staticmethod
    def clean_regex(regex, args):
        """
        Clean regexes with groups occuring multiple times
        """
        for arg in set(args):
            new_regex = ""
            for counter, chunk in enumerate(regex.split(arg)):
                if counter == 0:
                    new_regex += chunk
                elif counter == 1:
                    new_regex += arg + chunk
                else:
                    new_regex += "{}_occurence_{}{}".format(arg,counter,chunk)
            regex = new_regex
        return regex

    @staticmethod
    def regex_to_stringformat(regex):
        """
        Transforms a regex to a string format

        >>> regex_to_stringformat(r'^(?P<SiteA>.{5})L(?P<U>\d)(?P<N>\d)(?P<SiteB>.{5})')
        '{SiteA}L{U}{N}{SiteB}'
        """
        regex = regex.replace('\\', '')
        regex = regex.rstrip('$')
        regex = regex.lstrip('^')
        args = re.findall(r'\<([^\)]+)\>', regex)
        return re.sub(r'\(([^\)]+)\)', "{%s}", regex) % tuple(args)

    def replace(self, input):
        """
        transforms a string matching regexA into a string matching regexB and vice-versa.
        """
        matchA = re.match(self.cleaned_regexA, input)
        matchB = re.match(self.cleaned_regexB, input)
        output = None
        if matchA:
            output = self.formatB.format_map(_FormatDict(matchA.groupdict()))
        elif matchB:
            output = self.formatA.format_map(_FormatDict(matchB.groupdict()))
        return output


reg = RegexReplace(r'^(?P<A>.{2})\.(?P<B>.{2})\.(?P<C>.{2})\.(?P<D>.{2})\.(?P<E>.{2})$', r'(?P<A>.{2})(?P<B>.{2})(?P<C>.{2})(?P<D>.{2})(?P<E>.{2})$')