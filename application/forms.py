from wtforms import Form, StringField, SelectField


class UserSearchForm(Form):
    choices = [('Email', 'Email'), ('golfer_1', 'Golfer')]

    select = SelectField('Search by:', choices=choices, default='Email')
    search = StringField('')#"Enter masters2020 below and click search to view all entries. To view only your own entries, enter your email")


class EntryForm(Form):
    golfers = [('--Select golfer--', '--Select golfer--'),
               ('An, Byeong Hun', 'An, Byeong Hun'),
               ('Ancer, Abraham', 'Ancer, Abraham'),
               ('Bezuidenhout, Christiaan', 'Bezuidenhout, Christiaan'),
               ('Cabrera, Angel', 'Cabrera, Angel'),
               ('Cabrera Bello, Rafael', 'Cabrera Bello, Rafael'),
               ('Cantlay, Patrick', 'Cantlay, Patrick'),
               ('Casey, Paul', 'Casey, Paul'),
               ('Champ, Cameron', 'Champ, Cameron'),
               ('Conners, Corey', 'Conners, Corey'),
               ('Couples, Fred', 'Couples, Fred'),
               ('Day, Jason', 'Day, Jason'),
               ('DeChambeau, Bryson', 'DeChambeau, Bryson'),
               ('Duncan, Tyler', 'Duncan, Tyler'),
               ('Finau, Tony', 'Finau, Tony'),
               ('Fitzpatrick, Matthew', 'Fitzpatrick, Matthew'),
               ('Fleetwood, Tommy', 'Fleetwood, Tommy'),
               ('Fowler, Rickie', 'Fowler, Rickie'),
               ('Frittelli, Dylan', 'Frittelli, Dylan'),
               ('Glover, Lucas', 'Glover, Lucas'),
               ('Griffin, Lanto', 'Griffin, Lanto'),
               ('Hadwin, Adam', 'Hadwin, Adam'),
               ('Harding, Justin', 'Harding, Justin'),
               ('Hatton, Tyrrell', 'Hatton, Tyrrell'),
               ('Homa, Max', 'Homa, Max'),
               ('Horschel, Billy', 'Horschel, Billy'),
               ('Howell III, Charles', 'Howell III, Charles'),
               ('Im, Sungjae', 'Im, Sungjae'),
               ('Imahira, Shugo', 'Imahira, Shugo'),
               ('Immelman, Trevor', 'Immelman, Trevor'),
               ('Janewattananond, Jazz', 'Janewattananond, Jazz'),
               ('Johnson, Dustin', 'Johnson, Dustin'),
               ('Johnson, Zach', 'Johnson, Zach'),
               ('Kang, Sung', 'Kang, Sung'),
               ('Kim, Si Woo', 'Kim, Si Woo'),
               ('Kisner, Kevin', 'Kisner, Kevin'),
               ('Koepka, Brooks', 'Koepka, Brooks'),
               ('Kokrak, Jason', 'Kokrak, Jason'),
               ('Kuchar, Matt', 'Kuchar, Matt'),
               ('Landry, Andrew', 'Landry, Andrew'),
               ('Langer, Bernhard', 'Langer, Bernhard'),
               ('Lashley, Nate', 'Lashley, Nate'),
               ('Leishman, Marc', 'Leishman, Marc'),
               ('Lowry, Shane', 'Lowry, Shane'),
               ('Lyle, Sandy', 'Lyle, Sandy'),
               ('Matsuyama, Hideki', 'Matsuyama, Hideki'),
               ('McDowell, Graeme', 'McDowell, Graeme'),
               ('McIlroy, Rory', 'McIlroy, Rory'),
               ('Mickelson, Phil', 'Mickelson, Phil'),
               ('Mize, Larry', 'Mize, Larry'),
               ('Molinari, Francesco', 'Molinari, Francesco'),
               ('Morikawa, Collin', 'Morikawa, Collin'),
               ('Munoz, Sebastian', 'Munoz, Sebastian'),
               ('Na, Kevin', 'Na, Kevin'),
               ('Olazabal, Jose Maria', 'Olazabal, Jose Maria'),
               ('Oosthuizen, Louis', 'Oosthuizen, Louis'),
               ('Pan, C.T.', 'Pan, C.T.'),
               ('Perez, Victor', 'Perez, Victor'),
               ('Poston, J.T.', 'Poston, J.T.'),
               ('Poulter, Ian', 'Poulter, Ian'),
               ('Putnam, Andrew', 'Putnam, Andrew'),
               ('Rahm, Jon', 'Rahm, Jon'),
               ('Reavie, Chez', 'Reavie, Chez'),
               ('Reed, Patrick', 'Reed, Patrick'),
               ('Rose, Justin', 'Rose, Justin'),
               ('Schauffele, Xander', 'Schauffele, Xander'),
               ('Scheffler, Scottie', 'Scheffler, Scottie'),
               ('Schwartzel, Charl', 'Schwartzel, Charl'),
               ('Scott, Adam', 'Scott, Adam'),
               ('Simpson, Webb', 'Simpson, Webb'),
               ('Singh, Vijay', 'Singh, Vijay'),
               ('Smith, Cameron', 'Smith, Cameron'),
               ('Snedeker, Brandt', 'Snedeker, Brandt'),
               ('Spieth, Jordan', 'Spieth, Jordan'),
               ('Stenson, Henrik', 'Stenson, Henrik'),
               ('Taylor, Nick', 'Taylor, Nick'),
               ('Thomas, Justin', 'Thomas, Justin'),
               ('Todd, Brendon', 'Todd, Brendon'),
               ('Van Rooyen, Erik', 'Van Rooyen, Erik'),
               ('Walker, Jimmy', 'Walker, Jimmy'),
               ('Wallace, Matt', 'Wallace, Matt'),
               ('Watson, Bubba', 'Watson, Bubba'),
               ('Weir, Mike', 'Weir, Mike'),
               ('Westwood, Lee', 'Westwood, Lee'),
               ('Wiesberger, Bernd', 'Wiesberger, Bernd'),
               ('Willett, Danny', 'Willett, Danny'),
               ('Wolff, Matthew', 'Wolff, Matthew'),
               ('Woodland, Gary', 'Woodland, Gary'),
               ('Woods, Tiger', 'Woods, Tiger')]

    yes_no = [('No', 'No'), ('Yes', 'Yes')]
    entry_email = StringField('Entrant Email')
    entrant_full_name = StringField('Entrant Full Name')
    team_name = StringField('Team Name')
    golfer_1 = SelectField('Golfer 1', choices=golfers)
    golfer_2 = SelectField('Golfer 2', choices=golfers)
    golfer_3 = SelectField('Golfer 3', choices=golfers)
    golfer_4 = SelectField('Golfer 4', choices=golfers)
    tie_breaker = StringField('Tie Breaker')
    has_paid = SelectField('Have you paid?', choices=yes_no, default='No')
