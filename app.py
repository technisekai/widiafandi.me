import json
from flask import Flask, render_template, url_for, render_template_string, Markup
from flask_flatpages import FlatPages, pygmented_markdown
from datetime import datetime
import os
import json

# flask conf
app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
# for markdown files
articles = FlatPages(app)

# render markdown
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

# articles
posts = [p for p in articles if "date" in p.meta]
sorted_pages = sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%B %d, %Y")) # sort articles by date
# json data about myself
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# index page
@app.route('/')
def home():
	return render_template('index.html', data=data, title="Home")
# blogs 
@app.route('/blog/')    
def blog():
	sum_articles = len(sorted_pages)
	return render_template('blogs.html', sum_articles=sum_articles, articles=sorted_pages, title="Blogs")
# article page
@app.route('/blog/<path:path>.html')
def article(path):
    article = articles.get_or_404(path)
    return render_template('article.html', article=article, title=article.meta['title'])

if __name__ == '__main__':
	app.run(debug=True)