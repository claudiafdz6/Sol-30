from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import TicketSupervisor

@app.route('/')
def index():
    tickets = TicketSupervisor.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/add', methods=['POST'])
def add_ticket():
    if request.method == 'POST':
        id = request.form.get['id']
        utente_apertura = request.form['utente_apertura']
        utente_segnalato = request.form['utente_segnalato']
        id_task = request.form['id_task']
        note = request.form.get('note')
        tag = request.form.get('tag')
        
        new_ticket = TicketSupervisor(
            id=id,
            utente_apertura=utente_apertura,
            utente_segnalato=utente_segnalato,
            id_task=id_task,
            note=note,
            tag=tag
        )
        
        db.session.add(new_ticket)
        db.session.commit()
        
        print('Ticket has been correctly added')
        return redirect(url_for('index'))
