import requests
from lxml import etree

# r = requests.get("https://gelbooru.com/index.php?page=post&s=view&id=4578487")
# html = etree.HTML(r.text)

# with open('./test.html','w') as f:
#     f.write(r.text)

# print(
#     html.xpath("//ul[@id='tag-list']/div/li[contains(text(),'Rating')]/text()")
# )

with open('./test.html','r') as f:
    page_data = f.read()

print(
    etree.HTML(page_data).xpath("//img/@alt")
)

