from html.parser import HTMLParser


class HeadingParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.indentation = 0
	def handle_starttag(self, tag, attrs):
		if tag.lower()[0] == 'h' and len(tag)>=2 and tag[1:].isdigit():
			# check if the tag is h1,h2,h3, and so on
			self.indentation = int(tag[1:])-1	
		else:
			self.indentation = -10
	def handle_data(self, data):
		if self.indentation != -10 and data.strip() != "":
			# only heading tags have non -10 indentation, so we skip all the other types of tags
			heading_line = ' '*self.indentation+ data.strip()
			print(heading_line)

# infile = open('w3c.html')
# content = infile.read()
# infile.close()
# hp = HeadingParser()
# hp.feed(content)
