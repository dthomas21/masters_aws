from wtforms import Form, StringField, SelectField


class UserSearchForm(Form):
    choices = [('Email', 'Email'), ('golfer_1', 'Golfer')]

    select = SelectField('Search by:', choices=choices)
    search = StringField('Search your email to view your entries:')


class EntryForm(Form):
    golfers = [('--Select golfer--', '--Select golfer--'),
 ('Ancer, Abraham', 'Ancer, Abraham'),
 ('Cantlay, Patrick', 'Cantlay, Patrick'),
 ('Casey, Paul', 'Casey, Paul'),
 ('Champ, Cameron', 'Champ, Cameron'),
 ('Day, Jason', 'Day, Jason'),
 ('DeChambeau, Bryson', 'DeChambeau, Bryson'),
 ('Finau, Tony', 'Finau, Tony'),
 ('Fitzpatrick, Matthew', 'Fitzpatrick, Matthew'),
 ('Fleetwood, Tommy', 'Fleetwood, Tommy'),
 ('Fowler, Rickie', 'Fowler, Rickie'),
 ('Garcia, Sergio', 'Garcia, Sergio'),
 ('Hatton, Tyrrell', 'Hatton, Tyrrell'),
 ('Jae, Sung', 'Jae, Sung'),
 ('Kisner, Kevin', 'Kisner, Kevin'),
 ('Koepka, Brooks', 'Koepka, Brooks'),
 ('Kuchar, Matt', 'Kuchar, Matt'),
 ('Matsuyama, Hideki', 'Matsuyama, Hideki'),
 ('Mickelson, Phil', 'Mickelson, Phil'),
 ('Molinari, Francesco', 'Molinari, Francesco'),
 ('Morikawa, Collin', 'Morikawa, Collin'),
 ('Oosthuizen, Louis', 'Oosthuizen, Louis'),
 ('Poulter, Ian', 'Poulter, Ian'),
 ('Reed, Patrick', 'Reed, Patrick'),
 ('Rose, Justin', 'Rose, Justin'),
 ('Schauffele, Xander', 'Schauffele, Xander'),
 ('Scheffler, Scottie', 'Scheffler, Scottie'),
 ('Scott, Adam', 'Scott, Adam'),
 ('Simpson, Webb', 'Simpson, Webb'),
 ('Spieth, Jordan', 'Spieth, Jordan'),
 ('Stenson, Henrik', 'Stenson, Henrik'),
 ('Watson, Bubba', 'Watson, Bubba'),
 ('Westwood, Lee', 'Westwood, Lee'),
 ('Wolff, Matthew', 'Wolff, Matthew'),
 ('Woodland, Gary', 'Woodland, Gary'),
 ('Woods, Tiger', 'Woods, Tiger')]

    yes_no = [('No', 'No'), ('Yes', 'Yes')]
    entry_email = StringField('Entrant Email')
    team_name = StringField('Team Name')
    golfer_1 = SelectField('Golfer 1', choices=golfers)
    golfer_2 = SelectField('Golfer 2', choices=golfers)
    golfer_3 = SelectField('Golfer 3', choices=golfers)
    golfer_4 = SelectField('Golfer 4', choices=golfers)
    tie_breaker = StringField('Tie Breaker')
    has_paid = SelectField('Have you paid?', choices=yes_no, default='No')
