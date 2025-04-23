from flask import Blueprint, render_template

charity = Blueprint('charity', __name__)


@charity.route('/dashboard')
def charity_dashboard():
    return render_template('charity_dashboard.html')


@charity.route('/event_creation')
def charity_event_creation():
    return render_template('charity_event_creation.html')


@charity.route('/event_management')
def charity_event_management():
    return render_template('charity_event_management.html')


@charity.route('/volunteer_applications')
def charity_volunteer_applications():
    return render_template('charity_volunteer_applications.html')
