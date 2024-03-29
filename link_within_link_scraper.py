import requests
from bs4 import BeautifulSoup

url_input = input('URL: ')

def get_links(url):
    print('PROGRAM STARTING')
    print()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    list_of_links = []
    for link in links:
        try:
            if link.get('href')[:4] == 'http':
                print('LINKS IN', link.get('href'))
                list_of_links.append(link.get('href'))
                # Optionally write links to a file
                # with open('links.txt', 'a') as f:
                # file.write ('\n' + 'LINKS IN ' + link.get('href') + '\n')
                #     f.write('LINKS IN ' + link.get('href') + '\n')
                sub_r = requests.get(link.get('href'))
                sub_soup = BeautifulSoup(sub_r.text, 'html.parser')
                sub_links = sub_soup.find_all('a')
                for sub_link in sub_links:
                    try:
                        if sub_link.get('href')[:4] == 'http':
                            print(sub_link.get('href'))
                            list_of_links.append(sub_link.get('href'))
                            # Optionally write links to a file
                            # with open('links.txt', 'a') as f:
                            #     f.write(sub_link.get('href') + '\n')
                    except:
                        pass
                print()
        except:
            pass
    unique_links = set(list_of_links)
    links_ranked_tuples = []
    for link in unique_links:
        links_ranked_tuples.append((link, list_of_links.count(link)))
    links_ranked_tuples.sort(key=lambda x: x[1], reverse=True)
    print('LINKS RANKED***********************************************************************************************')
    # Optionally write ranked links to a file
    # with open('links.txt', 'a') as f:
    for link in links_ranked_tuples:
        print(link)
    #         f.write(str(link) + '\n')


get_links(url_input)
