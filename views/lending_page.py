from flask import render_template, current_app, abort
from hackkings import app, db
from hackkings.models import User
from hackkings.constants import ROLES

@app.route('/user/<id:int>')
def profile_page(id=None):
    if id == None:
        abort(404)
    user = User.find(id)
    if user == None:
        abort(404)

    landing_page_data = {}
    if user.role == DEVELOPER:
        landing_page_data = { 'avatar': user.avatar,
                              'username': user.username,
                              'ongoing_projects': user.get_ongoing_projects(),
                              'completed_projects': user.get_completed_projects(),
                              'suggested_projects': [] }
    elif user.role == PROPOSER:
        langing_page_data = { 'avatar': user.avatar,
                              'name': user.name, 
                              'ongoing_proposals': user.get_ongoing_proposals(),
                              'pending_proposals': user.get_pending_proposals(),
                              'completed_proposals': user.get_completed_proposals() }
    else
        abort(400)

    return render_template('landing_page.html', landing_page_data)
    

