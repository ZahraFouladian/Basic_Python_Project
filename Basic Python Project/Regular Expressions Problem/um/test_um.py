from um import count


def test_count():
    assert count('yoooum') == 0
    assert count('mummu') == 0
    assert count('um') == 1
    assert count('um, hellooo baby!') == 1
    assert count(' um hdjd kcdm um ') == 2
    assert count('Um, uM, UM') == 3
    assert count('UM UMM UUM?') == 1