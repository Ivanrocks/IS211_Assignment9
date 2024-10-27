from bs4 import BeautifulSoup
import urllib.request

def downloadData(url):
    """Downloads the data from provided URL"""
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

def main():
    html = downloadData('https://en.wikipedia.org/wiki/2020_United_States_census')
    parsedHTML = BeautifulSoup(html, 'html.parser')
    table = parsedHTML.find_all("tbody")[2]
    rows = table.find_all("tr")
    rows.pop(0)
    for col in rows:
        print("="*100)
        state = col.find_all("a")
        print("State:",state[0].getText())

        population = col.find_all("td")
        print("Population 2020:",population[3].getText())
        print("Population 2010:", population[4].getText())
        print("Population change:", population[5].getText())



if __name__ == "__main__":
    main()
