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
    },
    {
        "regex_A": r"^(?P<A>\d{2})\.(?P<B>\d{2})\.(?P<C>\d{2})$",
        "regex_B": r"^(?P<C>\d{2})(?P<B>\d{2})(?P<A>\d{2})$",
        "example_A": "01.02.03",
        "example_B": "030201",
    },
    {
        "regex_A": r"^(?P<WORD>.{5})$",
        "regex_B": r"^(?P<WORD>.{5})(?P<WORD>.{5})(?P<WORD>.{5})$",
        "example_A": "HELLO",
        "example_B": "HELLOHELLOHELLO",
    },
    {
        "regex_A": r"^(?P<WORD1>.{3})-(?P<CODE>\d{3})-(?P<WORD2>.{4})-(?P<CODE2>\d{3})-(?P<WORD3>.{5})$",
        "regex_B": r"^(?P<WORD1>.{3})/(?P<CODE2>\d{3})/(?P<WORD2>.{4})/(?P<CODE>\d{3})/(?P<WORD3>.{5})$",
        "example_A": "ABC-123-ABCD-456-ABCDE",
        "example_B": "ABC/456/ABCD/123/ABCDE",
    },
    {
        "regex_A": r"^(?P<DD>\d{2})-(?P<MM>\d{2})-(?P<YYYY>\d{4})$",
        "regex_B": r"^(?P<MM>\d{2})/(?P<DD>\d{2})/(?P<YYYY>\d{4})$",
        "example_A": "31-12-2017",
        "example_B": "12/31/2017",
    },
    {
        "regex_A": r"^(?P<WORD1>.{3})-(?P<CODE1>\d{3})-(?P<WORD2>.{4})-(?P<CODE2>\d{3})$",
        "regex_B": r"^(?P<CODE1>\d{3})-(?P<CODE2>\d{3})-(?P<WORD1>.{3})-(?P<WORD2>.{4})$",
        "example_A": "ABC-123-DEFG-456",
        "example_B": "123-456-ABC-DEFG",
    }

]


def test_rereplace():
    for element in ELEMENTS:
        rer = RegexReplace(element['regex_A'], element['regex_B'])
        assert rer.replace(element['example_A']) == element['example_B']
        assert rer.replace(element['example_B']) == element['example_A']


def test_missing():
    rer = RegexReplace(r"^(?P<DD>\d{2})-(?P<MM>\d{2})-(?P<YYYY>\d{4})$",
                       r"^(?P<MM>\d{2})/(?P<YYYY>\d{4})$")

    assert rer.replace("31-12-2017") == "12/2017"
    assert rer.replace("12/2017") == "{DD}-12-2017"
