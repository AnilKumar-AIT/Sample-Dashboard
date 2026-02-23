import json
import os
import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'fallvision_premium_system_2026'
USER_DB = 'users.json'

# --- Initialization ---
def init_db():
    if not os.path.exists(USER_DB):
        with open(USER_DB, 'w') as f:
            json.dump({}, f)

def get_health_metrics():
    """Generates premium-grade mock health telemetry."""
    return {
        "mobility_score": random.randint(84, 96),
        "posture_stability": random.randint(78, 92),
        "fall_risk": random.choice(["Minimal", "Low", "Optimal"]),
        "correlation": round(random.uniform(0.88, 0.98), 2),
        "angles": {
            "r_arm": random.randint(18, 32),
            "l_arm": random.randint(18, 32),
            "r_leg": random.randint(14, 26),
            "l_leg": random.randint(14, 26)
        },
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }

# --- Authentication Middleware ---
@app.context_processor
def inject_user():
    return dict(user=session.get('user'))

# --- Routes ---

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        users = json.load(open(USER_DB))
        email = request.form.get('email')
        pw = request.form.get('password')
        
        if 'signup' in request.form:
            if email in users:
                flash("This email is already registered.")
                return redirect(url_for('auth'))
            
            users[email] = {
                "name": request.form.get('name'),
                "email": email,
                "pw": generate_password_hash(pw),
                "role": "Senior Resident",
                "joined": datetime.now().strftime("%Y-%m-%d")
            }
            with open(USER_DB, 'w') as f:
                json.dump(users, f)
            flash("Account created successfully! Please login.")
            
        else:
            user = users.get(email)
            if user and check_password_hash(user['pw'], pw):
                session['user'] = user
                return redirect(url_for('dashboard'))
            flash("Invalid email or password.")
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('auth'))
    return render_template('dashboard.html', data=get_health_metrics())

@app.route('/detection')
def detection():
    if 'user' not in session: return redirect(url_for('auth'))
    return render_template('detection.html', data=get_health_metrics())

@app.route('/records')
def records():
    if 'user' not in session: return redirect(url_for('auth'))
    # Generate mock history for the table
    history = [get_health_metrics() for _ in range(8)]
    return render_template('records.html', history=history)

@app.route('/emergency')
def emergency():
    if 'user' not in session: return redirect(url_for('auth'))
    caregivers = [
        {"name": "Dr. Sarah Jenkins", "relation": "Primary Physician", "phone": "+1-555-0101", "status": "Online"},
        {"name": "Mark Thompson", "relation": "Emergency Contact", "phone": "+1-555-0909", "status": "Available"}
    ]
    alerts = [
        {"type": "Balance Shift", "severity": "Moderate", "time": "14:20", "description": "Lateral stability drift detected."},
        {"type": "System Check", "severity": "Low", "time": "09:00", "description": "IoT Wearable recalibration successful."}
    ]
    return render_template('emergency.html', caregivers=caregivers, alerts=alerts, data=get_health_metrics())

@app.route('/resources')
def resources():
    if 'user' not in session: return redirect(url_for('auth'))
    return render_template('resources.html')

@app.route('/faq')
def faq():
    if 'user' not in session: return redirect(url_for('auth'))
    return render_template('faq.html')

@app.route('/services')
def services():
    if 'user' not in session: return redirect(url_for('auth'))
    return render_template('services.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)