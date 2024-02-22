from flask import Blueprint, request, jsonify
from flaskapp.models.Project import Project
from flaskapp import projects
import json

import random

bp = Blueprint('service', __name__)

@bp.route('/new/project', methods=['POST'])
def create_project():
    directory_path = request.json.get('directory')
    if not directory_path:
        return jsonify({'error': 'Directory parameter is required'}),  400
    
    new_project = Project(directory_path)
    project_id = random.randint(1, 100)

    projects[project_id] = new_project

    return jsonify({'project_id': project_id}),  200

@bp.route('/project/<int:project_id>/packages', methods=['GET'])
def retrieve_packages(project_id):
    project = projects.get(project_id)

    if not project:
        return jsonify({'error': 'Invalid project id'}),  400
    
    packages = project.getPackages()

    package_names = []
    for package in packages:
        manifestData = json.loads(package.manifestData)
        package_names += [manifestData.name]

    return jsonify({'message': 'Retrieving packages for project {}'.format(project_id), 'packages': package_names}), 200


@bp.route('/service/<int:project_id>/changesets', methods=['GET'])
def retrieve_changesets(project_id):
    project = projects.get(project_id)

    if not project:
        return jsonify({'error': 'Invalid project id'}),  400
    
    return jsonify({'message': 'Retrieving changesets for service {}'.format(project.getChangesets())}),  200