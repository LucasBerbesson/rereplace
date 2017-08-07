from rereplace import RegexReplace

ELEMENTS = [
    {
        "regex_A": r"^(?P<SiteA>.{5})L(?P<U>\d)(?P<N>\d)(?P<SiteB>.{5})$",
        "regex_B": r"^(?P<SiteA>.{5})(?P<U>\d)(?P<SiteB>.{5})(?P<N>\d)$",
        "example_A": "CROQUL41ERNEE",
        "example_B": "CROQU4ERNEE1",
    },
    {
        "regex_A": r"^(?P<SiteA>.{5})Z(?P<U>\d)(?P<N>\d)(?P<SiteB>.{5})$",
        "regex_B": r"^(?P<SiteA>.{5})(?P<U>\d)(?P<SiteB>.{5})(?P<N>\d)M$",
        "example_A": "CTAURZ41RQROU",
        "example_B": "CTAUR4RQROU1M",
    },
    {
        "regex_A": r"^(?P<SiteA>.{5})$",
        "regex_B": r"^(?P<SiteA>.{5})(?P<SiteA>.{5})$",
        "example_A": "ABCDE",
        "example_B": "ABCDEABCDE",
    },
    {
        "regex_A": r"^(?P<A>\d{2})\.(?P<B>\d{2})\.(?P<C>\d{2})$",
        "regex_B": r"^(?P<C>\d{2})(?P<B>\d{2})(?P<A>\d{2})$",
        "example_A": "01.02.03",
        "example_B": "030201",
    }

]


def test_rereplace():
    for element in ELEMENTS:
        rer = RegexReplace(element['regex_A'],element['regex_B'])
        assert rer.replace(element['example_A']) == element['example_B']
        assert rer.replace(element['example_B']) == element['example_A']

