import re

def run_markdown(input_text):
    convertStrong = re.compile('\*\*')
    convertEm = re.compile('\*')

    if convertStrong.match(input_text):
        print 'strong'
        input_text = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', input_text)
        input_text = re.sub(r'__(.*)__', r'<strong>\1</strong>', input_text)
        return ('<p>' + input_text + '</p>').rstrip()
    elif convertEm.match(input_text):
        print 'em'
        input_text = re.sub(r'\*(.*)\*', r'<em>\1</em>', input_text)
        input_text = re.sub(r'_(.*)_', r'<em>\1</em>', input_text)
        return ('<p>' + input_text + '</p>').rstrip()
    else:
        print 'normal'
        return '<p>' + input_text + '</p>'
