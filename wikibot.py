import wikipedia
wikipedia.set_lang("en")

def scrape(name, length=3):
    try:
        summary = wikipedia.summary(name, sentences=length)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
result = wikipedia.summary("Python (programming language)") 
print(result)
print(scrape("Microsoft"))
