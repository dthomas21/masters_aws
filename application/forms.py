from wtforms import Form, StringField, SelectField


class UserSearchForm(Form):
    choices = [('Email', 'Email'), ('golfer_1', 'Golfer')]
    select = SelectField('Search by:', choices=choices)
    search = StringField('Type search here (or press search while blank to view all entries):')


class EntryForm(Form):
    golfers = [('Rory McIlroy', 'Rory McIlroy'), ('Dustin Johnson', 'Dustin Johnson'),
               ('Justin Rose', 'Justin Rose'), ('Jon Rahm', 'Jon Rahm')]
    entry_email = StringField('Entry Email')
    golfer_1 = SelectField('Golfer 1', choices=golfers)
    golfer_2 = SelectField('Golfer 2', choices=golfers)
    golfer_3 = SelectField('Golfer 3', choices=golfers)
    golfer_4 = SelectField('Golfer 4', choices=golfers)
    tie_breaker = StringField('Tie Breaker')