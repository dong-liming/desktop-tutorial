from flask import Blueprint, render_template

volunteer = Blueprint('volunteer', __name__)


@volunteer.route('/dashboard')
def volunteer_dashboard():
    return render_template('volunteer_dashboard.html')


@volunteer.route('/events')
def volunteer_events():
    return render_template('volunteer_events.html')


@volunteer.route('/event_details')
def volunteer_event_details():
    return render_template('volunteer_event_details.html')


@volunteer.route('/my_events')
def volunteer_my_events():
    return render_template('volunteer_my_events.html')
