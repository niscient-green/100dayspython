import requests
from bs4 import BeautifulSoup

# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchors = soup.find_all(name="a")
# for tag in all_anchors:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name='h1', id='name')
# print(heading)

# find_class = soup.find(name='h3', class_='heading')
# print(find_class)

# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name)

# headings = soup.select(selector='.heading')
# print(headings)

response = requests.get("https://news.ycombinator.com/")
yc_content = response.text
soup = BeautifulSoup(markup=yc_content, features='html.parser')

articles = [element for element in soup.select(selector=".titleline a") if not element.find(name="span")]
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(element.getText().split()[0]) for element in soup.find_all(class_="score")]

max_val = max(article_upvotes)
ind_max = article_upvotes.index(max_val)

print(f"Max story: {article_texts[ind_max]}, {article_upvotes[ind_max]}")