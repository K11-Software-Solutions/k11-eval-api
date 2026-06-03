def test_search_found(): assert len(search('widget')) > 0
def test_search_empty(): assert search('zzz_nonexistent') == []
def test_search_special_chars(): assert search("o'malley") is not None
