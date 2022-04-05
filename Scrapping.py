def scrap():
    import requests as req
    from bs4 import BeautifulSoup as bs
    import pandas as pd

    scheme ='https'
    Url_tag = 'bustekmedia.com/technologie'
    Access = f'{scheme}://{Url_tag}'

    req = req.get(Access)
    Bsoup = bs(req.text, 'html.parser')

    data = []


    if (req.status_code == 200):
        print('There is connections!!!')

    article = Bsoup.find_all("div",{"class":"td-animation-stack"})

    for div in article:
        Article = Bsoup.find("div", {"class":"td-category-title-holder"}).text
        Article = Article.strip().replace('\t','').replace('\n','')
        for date in article:
            Date =Bsoup.find('time', {'class':'entry-date updated td-module-date'}).text
            for autor in article:
                Author = Bsoup.find('a')['href']
                Author = Author.strip().replace('\t','').replace('\n','')


    data.append({
        'Article':Article,
        'Date':Date,
        'Author': Author
    })
    # My first code

    print(data)

    dataf = pd.DataFrame(data)
    dataf.to_csv('data.csv')
scraper = scrap()