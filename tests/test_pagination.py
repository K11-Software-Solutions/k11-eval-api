def test_default_limit(): assert len(paginate(items)) == 20
def test_custom_offset(): assert paginate(items, offset=5)[0] == items[5]
