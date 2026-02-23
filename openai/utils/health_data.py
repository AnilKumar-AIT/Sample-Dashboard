import random

def generate_angles():
    return {
        "right_arm": random.randint(20, 160),
        "left_arm": random.randint(20, 160),
        "right_leg": random.randint(10, 140),
        "left_leg": random.randint(10, 140),
    }

def brain_activity():
    return random.uniform(0.6, 1.0)

def mobility_score(angles, brain):
    avg_angle = sum(angles.values()) / 4
    score = (avg_angle / 160) * brain * 100
    return round(score, 2)

def fall_risk(score):
    if score > 75:
        return "Low"
    elif score > 50:
        return "Moderate"
    else:
        return "High"