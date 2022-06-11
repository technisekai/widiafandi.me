from flask import Flask, render_template, url_for, render_template_string, Markup
from flask_flatpages import FlatPages, pygmented_markdown
from datetime import datetime
import os

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
# markdown
pages = FlatPages(app)
# render jinja after markdown
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja
# artikel
posts = [p for p in pages if "date" in p.meta]
sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%B %d, %Y"))
# name resources for web
nav_link = ['Home', 'Artikel']
skill_icon = os.listdir('static/assets/img/icon-skill/')
porto = os.listdir('static/assets/img/portofolio/')

@app.route('/')
def home():
	return render_template('home.html', nav_link = nav_link, skill = skill_icon, porto = porto, judul='Home')

@app.route('/artikel/')    
def artikel():
	i = len(sorted_pages)
	return render_template('artikel.html', nav_link = nav_link, pages=sorted_pages, i = i, judul='Artikel')

@app.route('/artikel/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    path = path.replace('_', ' ')
    path = path.title()
    return render_template('page.html', nav_link = nav_link, page=page, judul=path)

if __name__ == '__main__':
	app.run(debug=True)
