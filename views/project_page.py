from flask import render_template, current_app, abort
from hackkings import app
from hackkings.models import Project

@app.route('/project/<id:int>')
def project_page(id=None):
    if id == None:
        abort(404)         
    project = Project.find(id)
    if project == None:
        abort(404)
    
    project_data = { 'proposer': project.proposer,
                     'difficulty': project.difficulty,
                     'time_estimate': project.time_estimate,
                     'description': project.description,
                     'attachments': project.attachments,
                     'skills_needed': project.get_skills(),
                     'currently_working': project.get_current_developers() }

    return render_template('project.html', project_data)