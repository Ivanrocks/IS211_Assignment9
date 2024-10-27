from bs4 import BeautifulSoup
import requests

def main():
    page = requests.get('https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/')
    parsedHTML = BeautifulSoup(page.text, 'html.parser')
    rows = parsedHTML.find_all(class_='TableBase-bodyTr')
    counter = 1
    for column in rows:
        print('-'*100)
        print("ID:", counter)
        #Getting the player's name
        player_name = column.find_all('a')
        print("Name: " + player_name[1].getText().strip())

        #Getting the [player's position
        player_position = column.find_all(class_="CellPlayerName-position")
        print("Position: " + player_position[0].getText().strip())

        #Getting the player's team
        player_team = column.find_all(class_="CellPlayerName-team")
        print("Team: " + player_team[0].getText().strip())

        #Getting the player's touchdown passes
        player_stats = column.find_all('td')
        print("Touchdown Passes: " + player_stats[8].getText().strip())
        print()
        if counter >= 20:
            break
        else:
            counter+=1
    #print(rows)
if __name__ == "__main__":
    main()
