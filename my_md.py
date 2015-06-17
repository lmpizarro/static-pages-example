import markdown
import codecs
from markdown.extensions.headerid import HeaderIdExtension

def get_html(page, extensions):
    input_file = codecs.open(page, mode="r", encoding="utf-8")
    text = input_file.read()
    md = markdown.Markdown( extensions=extensions )
    html = md.convert(text)
    return html

def index():
    return get_html("pages/index.md", ['markdown.extensions.toc'])

def page1():
    return get_html("pages/page1.md", ['markdown.extensions.toc'])

def page2():
    return get_html("pages/page2.md", ['markdown.extensions.toc',\
            'markdown.extensions.tables'])

print page1()

