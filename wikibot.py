import wikipedia
wikipedia.set_lang("en")

def scrape(name, length=3):
    summary = wikipedia.summary(name, sentences=length)
    return summary
print(scrape("Microsoft"))
