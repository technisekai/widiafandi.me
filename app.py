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
ARTICLES = FlatPages(app)

# render markdown
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

# articles
posts = [p for p in ARTICLES if "date" in p.meta]
sorted_pages = sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%B %d, %Y")) # sort articles by date
# json data about myself
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# index page
@app.route('/')
def home():
	return render_template('index.html', data=data, title="Home")

# projects 
@app.route('/projects/')    
def projects():
	# json data about my projects
	projects = ['porto-tableau', 'porto-ml-dl', 'porto-flutter']
	get_projects = []
	for project in projects:
		with open('static/assets/images/'+project+'/export.json', 'r', encoding='utf-8') as f:
			get_projects.append(json.load(f))
	return render_template('projects/projects.html', projects=get_projects, title="Projects")

# achievements 
@app.route('/achievements/')    
def achievements():
	return render_template('achievements.html', title="Achievements")

# artciles 
@app.route('/articles/')    
def articles():
	sum_articles = len(sorted_pages)
	return render_template('articles/articles.html', sum_articles=sum_articles, articles=sorted_pages, title="Articles")

# article page
@app.route('/articles/<path:path>.html')
def article(path):
    article = ARTICLES.get_or_404(path)
    return render_template('articles/article.html', article=article, title=article.meta['title'])

if __name__ == '__main__':
	app.run(debug=True)