import json
from url_joiner import transform
def test_transform():
    value='["https://example.test/a/", "b"]'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'https://example.test/a/b' in json.dumps(result,ensure_ascii=False)
