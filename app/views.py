from app import app, models
from flask import render_template, redirect, url_for

#To-DO: auto-generate pages for models, providers, topics, majors

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/comp-sci')
def comp_sci():
    return render_template('comp-sci-example.html')

@app.route('/major')
@app.route('/major/<major>')
def major(major=None):

    major = major.replace("-"," ")

    if models.Major.query.filter(models.Major.name.ilike(major)).first():
        major = models.Major.query.filter(models.Major.name.ilike(major)).first().name

    print major

    description = "Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Aenean lacinia bibendum nulla sed consectetur."

    if models.Major.query.filter(models.Major.name.ilike(major)).first() is not None:
        return render_template('major.html', major=major, description = description, provider='Harvard', provider_link="http://example.com")

    else:
        return redirect(url_for('index'))

@app.route('/course')
@app.route('/course/<course>')
def course(course=None):

    course = course.replace("-"," ")

    if models.Course.query.filter(models.Course.name.ilike(course)).first():
        course = models.Course.query.filter(models.Course.name.ilike(course)).first().name

    print course

    description = "Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Aenean lacinia bibendum nulla sed consectetur."

    if models.Course.query.filter(models.Course.name.ilike(course)).first() is not None:
        return render_template('course.html', course=course, description = description, provider='Harvard', provider_link="http://example.com")

    else:
        return redirect(url_for('index'))

@app.route('/provider')
@app.route('/provider/<provider>')
def provider(provider=None):

    provider = provider.replace("-"," ")

    if models.Provider.query.filter(models.Provider.name.ilike(provider)).first():
        provider = models.Provider.query.filter(models.Provider.name.ilike(provider)).first().name

    print provider

    description = "Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Aenean lacinia bibendum nulla sed consectetur."

    if models.Provider.query.filter(models.Provider.name.ilike(provider)).first() is not None:
        return render_template('provider.html', provider = provider, description= description, provider_link="http://example.com")

    else:
        return redirect(url_for('index'))
