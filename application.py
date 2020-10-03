from flask import Flask, flash, render_template, request, redirect, session, url_for
from application.models import Entry, Golfer
from application.forms import UserSearchForm, EntryForm
from application import db
from config import USERNAME, PASSWORD
# from db_setup import init_db, db
from application.tables import Results
from sqlalchemy import or_

app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'noclue'


@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    search = UserSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            flash('User name is different')
        elif request.form['password'] != PASSWORD:
            flash('Password is different')
        else:
            session['logged_in'] = True
            flash('Login successful')
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged Out')
    return redirect(url_for('index'))


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Email':
            qry = db.query(Entry, Golfer).filter(
                Golfer.id==Entry.entry_email_id).filter(
                Golfer.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'golfer_1':
            qry = db.query(Entry).filter(or_(
                Entry.golfer_1.contains(search_string), Entry.golfer_2.contains(search_string),
                Entry.golfer_3.contains(search_string), Entry.golfer_4.contains(search_string)
            ))
            results = qry.all()

    else:
        qry = db.query(Entry)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
    """
    add new entry
    """
    form = EntryForm(request.form)

    #     save the entry
    if request.method == 'POST' and form.validate():
        entry = Entry()
        save_changes(entry, form, new=True)
        flash('Entry successfully submitted')
        return redirect('/')

    return render_template('new_entry.html', form=form)

# editing:
@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db.query(Entry).filter(Entry.id==id)
    entry = qry.first()

    if entry:
        form = EntryForm(formdata=request.form, obj=entry)
        if request.method == 'POST' and form.validate():
#           save edits:
            save_changes(entry, form)
            flash('Entry successfully updated')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return f"Error loading {id}"

# deleting:
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete entry in database matching the specified id in the URL
    """
    qry = db.query(Entry).filter(
        Entry.id==id
    )
    entry = qry.first()

    if entry:
        form = EntryForm(formdata=request.form, obj=entry)
        if request.method == 'POST' and form.validate():
#             delete from database
            db.delete(entry)
            db.commit()
            flash('Entry successfully deleted')
            return redirect('/')
        return render_template('delete_entry.html', form=form)
    else:
        return f"Error deleting {id}"

def save_changes(entry, form, new=False):
    """
    Save the changes to the database
    """
#     Get data from form and assign it to the correct attributes of the SQLAlchemy table object
    entry_email = Golfer()
    entry_email.name = form.entry_email.data

    entry.entry_email = entry_email
    entry.golfer_1 = form.golfer_1.data
    entry.golfer_2 = form.golfer_2.data
    entry.golfer_3 = form.golfer_3.data
    entry.golfer_4 = form.golfer_4.data
    entry.tie_breaker = form.tie_breaker.data

    if new:
#        add new entry to database
        db.add(entry)

#     commit to database
    db.commit()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

