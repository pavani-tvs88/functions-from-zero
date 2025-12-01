import wikipedia
def scrape(name, length=3):
    summary = wikipedia.summary(name, sentences=length)
    return summary    
