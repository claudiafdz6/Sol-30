from flask import current_app as app
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import TicketSupervisor, User

@app.route('/')
@login_required
def index():
    tickets = TicketSupervisor.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index.html'))
        else:
            print('Invalid username or password')
    
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

@app.route('/add', methods=['POST'])
@login_required
def add_ticket():
    if request.method == 'POST':
        id = request.form.get('id')
        utente_apertura = request.form['utente_apertura']
        utente_segnalato = request.form['utente_segnalato']
        id_task = request.form['id_task']
        note = request.form.get('note')
        tag = request.form.get('tag')
        data_apertura = request.form['data_apertura']
        data_chiusura = request.form['data_chiusura']

        new_ticket = TicketSupervisor(
            id=id,
            utente_apertura=utente_apertura,
            utente_segnalato=utente_segnalato,
            id_task=id_task,
            note=note,
            tag=tag,
            data_apertura=data_apertura,
            data_chiusura=data_chiusura
        )
        
        db.session.add(new_ticket)
        db.session.commit()
        
        print('Ticket has been added')
        return redirect(url_for('index.html'))
