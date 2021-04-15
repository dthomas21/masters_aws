from flask import Flask, flash, render_template, request, redirect, session, url_for
from application.models import Entry, Golfer
from application.forms import UserSearchForm, EntryForm, LeaderboardForm
from application import db
from application import application
from config import USERNAME, PASSWORD
# from db_setup import init_db, db
from application.tables import Results, UserResults
from sqlalchemy import or_
import pandas as pd
import requests
from bs4 import BeautifulSoup


@application.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    search = UserSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            flash('League Name is different')
        elif request.form['password'] != PASSWORD:
            flash('Access Code is different')
        else:
            session['logged_in'] = True
            # flash('Login successful')
            return redirect(url_for('index'))
    return render_template('login.html')


@application.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged Out')
    return redirect(url_for('index'))

@application.route('/leaderboard')
def get_leaderboard():
    # read in manual entries
    df = pd.read_csv('static/dump-2021.csv', sep='\t')

    # scrape
    url = 'https://www.augusta.com/masters/leaderboard'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="LargeLeaderboard")
    job_elems = results.find_all('tr')

    # loop to scrape
    scores = []
    for i in range(3, len(job_elems)):
        name = job_elems[i].find('a').text.strip()
        if len(name.split()) > 2:
            name = f'{name.split()[2]}, {name.split()[0]} {name.split()[1]}'
        elif job_elems[i].find('a').text.strip() == 'Matthew Fitzpatrick':
            name = 'Fitzpatrick, Matt'
        else:
            name = f'{name.split()[1]}, {name.split()[0]}'

        if job_elems[i].find('td', class_='center score').text == 'E':
            score = 0
        else:
            try:
                score = int(job_elems[i].find('td', class_='center score').text)
            except:
                score = None

        try:
            standing = int(job_elems[i].find('td').text.replace('T', ''))
        except:
            standing = None

        scores.append([name, score, standing])

    live_results = pd.DataFrame(scores, columns=['golfer', 'score', 'standing'])

    # combine
    df['golfer_1_score'] = ''
    df['golfer_2_score'] = ''
    df['golfer_3_score'] = ''
    df['golfer_4_score'] = ''

    for i in range(len(df)):
        df.golfer_1_score[i] = live_results.loc[live_results.golfer == df.golfer_1[i]]['score'].values[0]
        df.golfer_2_score[i] = live_results.loc[live_results.golfer == df.golfer_2[i]]['score'].values[0]
        df.golfer_3_score[i] = live_results.loc[live_results.golfer == df.golfer_3[i]]['score'].values[0]
        df.golfer_4_score[i] = live_results.loc[live_results.golfer == df.golfer_4[i]]['score'].values[0]
    df['total_team_score'] = df.golfer_1_score + df.golfer_2_score + df.golfer_3_score + df.golfer_4_score

    df = df.drop(columns=['id', 'entry_email_id', 'has_paid'])
    df['tie_breaker'] = df['tie_breaker'].apply(lambda x: abs(x)*-1)



    df = df.sort_values(by='total_team_score').reset_index(drop=True)
    df.index = df.total_team_score.rank(method='dense')
    df.index = df.index.map(int)
    df.index.name = None

    df = df.rename(columns={"entrant_full_name": "Participant", "team_name": "Team Name",
                        "golfer_1": "Golfer 1", "golfer_2": "Golfer 2", "golfer_3": "Golfer 3", "golfer_4": "Golfer 4",
                        "golfer_1_score": "Golfer 1 Score", "golfer_2_score": "Golfer 2 Score",
                        "golfer_3_score": "Golfer 3 Score", "golfer_4_score": "Golfer 4 Score",
                        "tie_breaker": "Tie Breaker", "total_team_score": "Total"})


    flash('This online leaderboard (unofficial) displays estimated rankings based on a team’s total strokes under par.')
    flash('REMINDER: First, second and third places will be determined by the top three team aggregate tournament money winners upon the conclusion of the tournament.')
    return render_template('leaderboard.html', tables=[df.to_html(classes='data')], titles=[df.columns.values])


@application.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        allow_edit = False
        if search_string == 'admin8':
            qry = db.session.query(Entry)
            results = qry.all()
            allow_edit = True

        elif search_string == 'greenjacket8':
            qry = db.session.query(Entry)
            results = qry.all()

        elif search.data['select'] == 'Email':
            qry = db.session.query(Entry, Golfer).filter(
                Golfer.id==Entry.entry_email_id).filter(
                Golfer.name==search_string)
            results = [item[0] for item in qry.all()]

        elif search.data['select'] == 'golfer_1':
            qry = db.session.query(Entry, Golfer).filter(or_(
                Entry.golfer_1.contains(search_string), Entry.golfer_2.contains(search_string),
                Entry.golfer_3.contains(search_string), Entry.golfer_4.contains(search_string)
            ))
            results = [item[0] for item in qry.all()]

    # else:
    #     flash('No results found')
        # qry = db.session.query(Entry)
        # results = qry.all()

    if not results:
        flash('No results found')
        return redirect('/')
    else:
        # display results
        if allow_edit:
            table = Results(results)
            table.border = True
            return render_template('results.html', table=table)
        else:
            table = UserResults(results)
            table.border = True
            return render_template('results.html', table=table)



@application.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
    """
    add new entry
    """
    form = EntryForm(request.form)

    #     save the entry
    if request.method == 'POST' and form.validate():
        entry = Entry()
        if request.form['entry_email'] == '':
            flash('Entry Email not provided, entry was not submitted')
        elif request.form['team_name'] == '':
            flash('Team Name not provided, entry was not submitted')
        elif request.form['tie_breaker'] ==  '':
            flash('Tie Breaker not provided, entry was not submitted')
        elif request.form['entrant_full_name'] == '':
            flash('Entrant full name not provide, entry was not submitted')
        elif request.form['golfer_1'] == '--Select golfer--' or request.form['golfer_2'] == '--Select golfer--' or \
                request.form['golfer_3'] == '--Select golfer--' or request.form['golfer_4'] == '--Select golfer--':
            flash('One or more golfers have not been selected properly, entry was not submitted')
        else:
            save_changes(entry, form, new=True)
            flash('Entry successfully submitted, good luck!')
            return redirect('/')

    return render_template('new_entry.html', form=form)

# editing:
@application.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db.session.query(Entry).filter(Entry.id==id)
    entry = qry.first()

    if entry:
        form = EntryForm(formdata=request.form, obj=entry)
        if request.method == 'POST' and form.validate():
#           save edits:
            save_changes(entry, form)
            flash('Entry successfully updated')
            db.session.commit()
            # return redirect('/')
            qry = db.session.query(Entry)
            results = qry.all()
            table = Results(results)
            table.border = True
            return render_template('results.html', table=table)
        return render_template('edit_album.html', form=form)
    else:
        return f"Error loading {id}"

# deleting:
@application.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete entry in database matching the specified id in the URL
    """
    qry = db.session.query(Entry).filter(
        Entry.id==id
    )
    entry = qry.first()

    if entry:
        form = EntryForm(formdata=request.form, obj=entry)
        if request.method == 'POST' and form.validate():
#             delete from database
            db.session.delete(entry)
            db.session.commit()
            flash('Entry successfully deleted')
            # return redirect('/')
            qry = db.session.query(Entry)
            results = qry.all()
            table = Results(results)
            table.border = True
            return render_template('results.html', table=table)
        return render_template('delete_entry.html', form=form)
    else:
        return f"Error deleting {id}"

def save_changes(entry, form, new=False):
    """
    Save the changes to the database
    """
#     Get data from form and assign it to the correct attributes of the SQLAlchemy table object
    entry_email = Golfer(name=form.entry_email.data)
    # entry_email.name = form.entry_email.data

    entry.entry_email = entry_email
    entry.entrant_full_name = form.entrant_full_name.data
    entry.team_name = form.team_name.data
    entry.golfer_1 = form.golfer_1.data
    entry.golfer_2 = form.golfer_2.data
    entry.golfer_3 = form.golfer_3.data
    entry.golfer_4 = form.golfer_4.data
    entry.tie_breaker = form.tie_breaker.data
    entry.has_paid = form.has_paid.data

    if new:
#        add new entry to database
        try:
            db.session.add(entry)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()

#     commit to database
#     db.session.commit()


if __name__ == '__main__':
    db.create_all()
    application.run(debug=True)
