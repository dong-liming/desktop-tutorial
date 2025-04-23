from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')


@admin.route('/user_management')
def admin_user_management():
    return render_template('admin_user_management.html')


@admin.route('/event_approval')
def admin_event_approval():
    return render_template('admin_event_approval.html')
