# %%
import lxml.html
# %%
tree = lxml.html.parse("dp.html")
html = tree.getroot()

# %%
print(html)

# %%
html.make_links_absolute('https://gihyo.jp/')

# %%
for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    # a要素のhref属性から書籍のURLを取得する。
    url = a.get('href')

    # 書籍のタイトルは itemprop="name" という属性を持つp要素から取得する。
    p = a.cssselect('p[itemprop="name"]')[0]
    title = p.text_content()  # wbr要素などが含まれるのでtextではなくtext_content()を使う。

    # 書籍のURLとタイトルを出力する。
    print(url, title)

# %%
