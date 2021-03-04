from re import compile

TAG_RE = compile(r'<[^>]+>')
def removeTags(text):
	return TAG_RE.sub('', text)