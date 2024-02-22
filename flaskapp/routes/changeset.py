from flask import Blueprint, request, jsonify
from flaskapp import projects

bp = Blueprint('changeset', __name__)

@bp.route('/service/<int:project_id>/new/changeset', methods=['POST'])
def create_changeset(project_id):
    project = projects.get(project_id)

    if not project:
        return jsonify({'error': 'Invalid project id'}),  400
    
    changeset = project.createChangeset()

    return jsonify({'message': 'Successfully created changeset for project {}'.format(project_id), 'changeset_description': changeset.getDescription()}),  200