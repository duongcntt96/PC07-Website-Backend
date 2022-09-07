def doc_replace(doc, findText, replaceText):
    for p in doc.paragraphs:
        if findText in p.text:
            inline = p.runs
            for i in range(len(inline)):
                if findText in inline[i].text:
                    text = inline[i].text.replace(
                        findText, replaceText)
                    inline[i].text = text
