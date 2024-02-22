from flask import Blueprint, jsonify
from flaskapp import projects
from flaskapp.models.Package import Package
from flaskapp.models.Changelog import Changelog

bp = Blueprint('changelog', __name__)

@bp.route('/service/<int:project_id>/new/changelog', methods=['POST'])
def create_changelog(project_id):
    project = projects.get(project_id)

    if not project:
        return jsonify({'error': 'Invalid project id'}),  400
    
    project.createChangelog()
    return jsonify({'message': 'Created changelog successfully for package {}'.format(project_id)}),  200

@bp.route('/service/<int:project_id>/package/<string:package_name>', methods=['GET'])
def retrieve_changelog(project_id, package_name):
    project = projects.get(project_id)

    if not project:
        return jsonify({'error': 'Invalid project id'}),  400
    
    package_lst = filter(lambda package: package.path == project.path + "/src/" + package_name, project.getPackages())

    if not package_lst:
        return jsonify({'error': 'Could not find package'}),  400
    
    package = package_lst[0]
    changeLog = Changelog(package)
    
    return jsonify({'message': 'Retrieving changelog for package {} of project {}'.format(package_name, project_id), 'changelog': changeLog}),  200
