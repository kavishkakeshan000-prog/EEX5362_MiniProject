"""
Configuration settings for the simulation
"""

# Simulation parameters
DEFAULT_CONFIG = {
    'num_regular_lanes': 3,
    'num_priority_lanes': 1,
    'arrival_rate': 5,
    'priority_prob': 0.20,
    'random_check_prob': 0.15,
    'delay_prob': 0.10,
    'duration': 120
}

# Scanning time ranges (min, max) in minutes
REGULAR_SCAN_TIME = (2, 4)
PRIORITY_SCAN_TIME = (1.5, 3)

# Random check additional time range
RANDOM_CHECK_TIME = (3, 8)

# Delay time range
DELAY_TIME = (1, 3)

# Queue monitoring interval
MONITOR_INTERVAL = 5

# High queue alert threshold
HIGH_QUEUE_THRESHOLD = 10