# 🚀 FallVision Quick Start Guide

## Prerequisites Check ✅

Before starting, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip package manager
- ✅ A modern web browser (Chrome, Firefox, Edge, Safari)
- ✅ Basic command line knowledge

---

## Step 1: Installation (2 minutes)

### Open Terminal/Command Prompt

**Windows:**
```powershell
cd D:\Users\akedarsetty\Desktop\AIT\Sample-Dashboard\anthropic
```

**Mac/Linux:**
```bash
cd ~/Desktop/AIT/Sample-Dashboard/anthropic
```

### Install Flask (if not already installed)

```bash
pip install flask
```

---

## Step 2: Start the Server (30 seconds)

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* FallVision Application Started
```

---

## Step 3: Access the Application

1. Open your web browser
2. Go to: **http://localhost:5000**
3. You'll see the landing/login page

---

## Step 4: Create an Account

1. Click **"Sign Up"** button
2. Fill in the form:
   - **Name:** Your Full Name
   - **Email:** your.email@example.com
   - **Password:** (minimum 6 characters)
   - **Role:** Select "Patient" or "Caregiver"
3. Click **"Create Account"**

---

## Step 5: Explore New Features 🎯

### A. Threshold Monitor
1. Click **"Threshold Monitor"** in sidebar
2. **What you'll see:**
   - Real-time limb angles for all 4 limbs
   - Color-coded alert badges (🟢 Safe, 🟡 Caution, 🟠 Warning, 🔴 Critical)
   - Composite fall risk score
   - Brain-movement sync status
   - Recommended actions

**Try this:** Click "Notify Guardian" to see alert system

---

### B. Brain Heatmap
1. Click **"Brain Heatmap"** in sidebar under "Brain Analytics"
2. **What you'll see:**
   - 24-hour grid showing brain activity levels
   - Peak and low activity hours
   - Morning/evening pattern charts
   - Time-based activity recommendations

**Try this:** Click any hour cell for detailed analysis

---

### C. Coordination Matrix
1. Click **"Coordination"** in sidebar
2. **What you'll see:**
   - 4x4 correlation matrix showing limb relationships
   - Symmetry scores (Arm, Leg, Overall)
   - Abnormal pattern alerts
   - Individual limb movement charts

**Try this:** Click any matrix cell to see inter-limb correlation details

---

### D. Neural Fatigue
1. Click **"Neural Fatigue"** in sidebar under "Brain Analytics"
2. **What you'll see:**
   - Current fatigue level (0-100)
   - 24-hour fatigue pattern
   - Fatigue-fall risk correlation
   - Rest effectiveness analysis
   - Personalized recommendations

**Try this:** Click any hour in the fatigue grid for detailed advice

---

## Step 6: Understand the Alerts 🚨

### Alert Levels Explained

| Level | Color | Deviation | Action Required |
|-------|-------|-----------|-----------------|
| 🟢 **SAFE** | Green | Within range | Continue normal activities |
| 🟡 **YELLOW** | Yellow | 5-10° outside | Take caution, monitor closely |
| 🟠 **ORANGE** | Orange | 10-15° outside | Reduce activity, notify caregiver |
| 🔴 **RED** | Red | >15° outside | STOP activities, immediate help |

### Brain Sync Thresholds

| Status | Value | Risk Level |
|--------|-------|------------|
| ✅ Excellent | > 0.80 | Low |
| ⚠️ Caution | 0.75 - 0.80 | Moderate |
| ⚠️ Warning | 0.65 - 0.75 | High |
| 🚨 Critical | < 0.65 | Very High |

---

## Step 7: Test the SOS System 🆘

1. Go to **Threshold Monitor** page
2. Scroll down to **Brain-Movement Synchronization** section
3. Click **"Alert Guardian Now"** button (if brain sync is low)
4. Confirm the alert

**What happens:**
- Guardians receive notifications (SMS/Email/Push)
- Alert logged in notification history
- Emergency protocol activated

---

## Common Tasks

### View Past Data
- Click **"Past Records"** to see historical metrics
- Click **"Trends"** for 60-day analysis

### Check Fall Risk
- Go to **Dashboard** for overview
- Check **Threshold Monitor** for real-time risk
- Review **Emergency Hub** for active alerts

### Track Progress
- **Trends** page shows improvement over time
- **Coordination Matrix** tracks symmetry changes
- **Neural Fatigue** identifies pattern changes

---

## Troubleshooting 🔧

### Server won't start
```bash
# Check if port 5000 is in use
# On Windows:
netstat -ano | findstr :5000

# On Mac/Linux:
lsof -i :5000

# Kill the process if needed, then restart
```

### Can't login
- Make sure you created an account first
- Check password is at least 6 characters
- Try signing up with a different email

### Charts not loading
- Check your internet connection (Chart.js loads from CDN)
- Try refreshing the page
- Clear browser cache

### "Module not found" error
```bash
# Make sure you're in the correct directory
pwd  # Should show .../anthropic

# Reinstall Flask
pip install --upgrade flask
```

---

## Understanding the Data 📊

### What's Being Monitored

1. **Limb Angles**
   - Right Arm: 70-110° (Optimal: 85°)
   - Left Arm: 70-110° (Optimal: 82°)
   - Right Leg: 155-175° (Optimal: 168°)
   - Left Leg: 155-175° (Optimal: 165°)

2. **Brain-Movement Correlation**
   - Measures how well brain signals translate to actual movement
   - Range: 0.00 - 1.00
   - Target: > 0.80

3. **Neural Fatigue**
   - Cognitive-motor tiredness
   - Range: 0 - 100
   - Target: < 30

4. **Fall Risk Score**
   - Composite calculation from all factors
   - Range: 0% - 100%
   - Target: < 20%

---

## Best Practices 🌟

### For Patients

1. **Check Threshold Monitor daily** - Ideally 2-3 times per day
2. **Review Brain Heatmap weekly** - Identify your personal patterns
3. **Monitor fatigue** - Take breaks during high-fatigue hours
4. **Follow recommendations** - The system learns from your data

### For Caregivers

1. **Set up alert notifications** - Ensure you receive critical alerts
2. **Review coordination matrix** - Track symmetry trends
3. **Check emergency hub** - Monitor active alerts
4. **Weekly review** - Discuss trends page with patient

---

## Next Steps 🎯

### After Setup

1. ✅ **Day 1:** Familiarize yourself with all 4 new features
2. ✅ **Day 2-7:** Establish baseline (system learns your patterns)
3. ✅ **Week 2:** Review coordination matrix for asymmetries
4. ✅ **Week 3:** Optimize activity schedule based on brain heatmap
5. ✅ **Week 4:** Track improvements in trends page

### Advanced Usage

- **Customize thresholds** - Adjust for your specific needs
- **Add guardians** - Set up multiple emergency contacts
- **Export data** - Generate reports for doctor visits
- **Set goals** - Track milestones and achievements

---

## Feature Navigation Map 🗺️

```
Dashboard (Home)
├── Overview KPIs
├── Quick Charts
└── Recent Alerts

🎯 Monitoring Section
├── Detection (Existing)
│   ├── Individual limb analysis
│   └── Full body scan
├── Threshold Monitor (NEW)
│   ├── Real-time angle monitoring
│   ├── Alert system
│   └── Risk scoring
└── Coordination (NEW)
    ├── 4x4 correlation matrix
    ├── Symmetry analysis
    └── Pattern detection

🧠 Brain Analytics Section
├── Brain Heatmap (NEW)
│   ├── 24-hour activity map
│   ├── Peak/low identification
│   └── Time recommendations
└── Neural Fatigue (NEW)
    ├── Current fatigue level
    ├── 24-hour pattern
    └── Rest recommendations

📊 Historical Data
├── Past Records
└── Trends (60-day analysis)

🚨 Safety
└── Emergency Hub
    ├── Active alerts
    ├── SOS button
    └── Guardian contacts
```

---

## Keyboard Shortcuts ⌨️

| Shortcut | Action |
|----------|--------|
| `Alt + H` | Go to Dashboard |
| `Alt + T` | Open Threshold Monitor |
| `Alt + B` | Open Brain Heatmap |
| `Alt + C` | Open Coordination Matrix |
| `Alt + F` | Open Neural Fatigue |
| `Alt + E` | Open Emergency Hub |
| `Esc` | Close modals |

---

## Getting Help 💬

### In-App Resources
- **FAQ Page** - Common questions answered
- **Support Page** - Contact information
- **Resources Page** - Educational materials

### Emergency Contact
- **Email:** support@fallvision.com
- **Phone:** [Your emergency number]
- **Hours:** 24/7 for critical alerts

---

## Performance Tips 💡

### For Best Experience

1. **Use Chrome or Edge** - Best Chart.js performance
2. **Enable JavaScript** - Required for real-time updates
3. **Stable internet** - For live monitoring
4. **Desktop recommended** - Mobile works but desktop is optimal

### Auto-Refresh
- Threshold Monitor refreshes every 5 seconds
- Charts update in real-time
- Alerts appear instantly

---

## Data Privacy & Security 🔒

### Your Data is Safe
- ✅ Password hashing (SHA-256)
- ✅ Session-based auth
- ✅ No data shared without consent
- ✅ Audit trail for all alerts
- ✅ HIPAA-compliant design

---

## Success Checklist ✅

After following this guide, you should:
- ✅ Have the server running
- ✅ Be logged into your account
- ✅ Understand all 4 new features
- ✅ Know how to read alerts
- ✅ Understand your risk scores
- ✅ Know when to take action

---

## Quick Reference Card 📋

**Print this for daily use:**

```
┌─────────────────────────────────────┐
│   FALLVISION QUICK REFERENCE        │
├─────────────────────────────────────┤
│ SAFE: 🟢 Continue normal activities │
│ CAUTION: 🟡 Monitor closely         │
│ WARNING: 🟠 Reduce activity         │
│ CRITICAL: 🔴 Stop & notify guardian │
├─────────────────────────────────────┤
│ Brain Sync Target: > 0.80           │
│ Fatigue Target: < 30                │
│ Fall Risk Target: < 20%             │
├─────────────────────────────────────┤
│ Emergency: Press SOS button         │
│ Questions: FAQ page or Support      │
└─────────────────────────────────────┘
```

---

**🎉 You're all set! Start monitoring your health professionally with FallVision!**

**Questions? Check the main README.md or contact support.**
