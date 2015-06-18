import markdown
import codecs

def get_html(page, extensions):
    input_file = codecs.open(page, mode="r", encoding="utf-8")
    text = input_file.read()
    md = markdown.Markdown( extensions=extensions )
    html = md.convert(text)
    return html

def index():
    return get_html("pages/index.md", ['toc'])

def page1():
    return get_html("pages/page1.md", ['toc'])

def page2():
    return get_html("pages/page2.md", ['extra', 'toc'])

def page2_extra():
    return get_html("pages/page2_extra.md", ['extra'])

print page1()

