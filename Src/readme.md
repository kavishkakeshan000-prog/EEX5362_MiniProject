- https://www.python.org/downloads/
- https://simpy.readthedocs.io/
- https://opensource.org/licenses/MIT

A discrete-event simulation framework for analyzing airport security checkpoint performance, resource utilization, and passenger flow optimization.


# 🎯 Overview

This simulation models a realistic airport security checkpoint with multiple screening lanes, priority passenger processing, random security checks, and operational delays. It enables airport operators and analysts to:

    - Evaluate checkpoint configurations (number of lanes, staffing levels)
    - Optimize resource allocation between regular and priority lanes
    - Assess the impact of security protocols on throughput
    - Predict performance under varying passenger loads
    - Identify bottlenecks and operational inefficiencies

The simulation uses SimPy, a process-based discrete-event simulation framework, to model passenger arrivals, queueing, and security screening processes.

# ✨ Features

### Core Simulation Capabilities

    - Multi-lane checkpoint modeling with separate regular and priority lanes
    - Stochastic passenger arrivals using exponential inter-arrival times
    - Random security checks (baggage inspection, pat-downs) with configurable probability
    - Operational delays (alarms, repacking, confusion) with realistic time distributions
    - Priority passenger processing (TSA PreCheck, CLEAR, etc.)
    - Real-time queue monitoring with high-queue alerts

### Analytics and Reporting

    - Comprehensive statistics on wait times, service times, and throughput
    - Lane utilization tracking across all security lanes
    - Performance comparison between regular and priority lanes
    - Impact analysis of random checks and delays
    - Time-series data for queue length and system state

### Visualization

    - 6-panel analysis dashboard with publication-quality plots
    - Wait time, service time, and total time distributions
    - Lane utilization bar charts
    - Time-series scatter plots
    - Impact comparison of security measures

# 🚀 Installation

### Prerequisites
    - Python 3.7 or higher
    - pip package manager

### Required Dependencies

pip install simpy numpy matplotlib

### Verify Installation

python main.py

If installation is successful, you should see simulation output and a generated visualization PNG file.

# 🎬 Quick Start

### Run Default Simulation

python main.py

This runs a 120-minute simulation with default parameters:

    - 3 regular security lanes
    - 1 priority lane
    - Passenger arrival every ~5 minutes
    - 20% priority passengers
    - 15% random check probability
    - 10% delay probability

### Basic Customization

from main import run_simulation

<!-- Run with custom parameters -->
checkpoint = run_simulation(
    num_regular_lanes=5,
    num_priority_lanes=2,
    arrival_rate=3,  # Passengers arrive every 3 minutes (busier)
    duration=180     # Run for 3 hours
)

# 📁 Project Structure

airport-security-simulation/
│
├── main.py              # Main simulation runner and entry point
├── checkpoint.py        # AirportSecurityCheckpoint class implementation
├── generator.py         # Passenger generation and monitoring processes
├── models.py            # Data models (PassengerStats dataclass)
├── config.py            # Configuration parameters and constants
├── statistics1.py       # Statistical analysis and reporting
├── visualization.py     # Plotting and visualization functions
├── README.md            # This file
└── requirements.txt     # Python dependencies

Generated files:
├── airport_security_simulation.png  # Visualization output

### Module Descriptions

| Module | Purpose | Key Components |
|--------|---------|----------------|
| `main.py` | Orchestrates simulation execution and coordinates all components |`run_simulation()` - Main entry point |
| `checkpoint.py` | Core simulation logic: security screening, random checks, delays | `AirportSecurityCheckpoint` class, `security_screening()` method |
| `generator.py` | Passenger arrival process and queue monitoring | `passenger_generator()`, `monitor_queue()` |
| `models.py` | Data structures for storing passenger statistics | `PassengerStats` dataclass |
| `config.py` | Centralized configuration management | `DEFAULT_CONFIG`, time range constants |
| `statistics1.py` | Calculates metrics and generates reports | `print_statistics()` function |
| `visualization.py` | Creates multi-panel analysis charts | `plot_results()` function |

---

# ⚙️ Configuration

### Default Configuration (config.py)

DEFAULT_CONFIG = {
    'num_regular_lanes': 3,      # Number of regular security lanes
    'num_priority_lanes': 1,     # Number of priority lanes (TSA PreCheck)
    'arrival_rate': 5,           # Average minutes between arrivals
    'priority_prob': 0.20,       # 20% of passengers have priority access
    'random_check_prob': 0.15,   # 15% chance of random security check
    'delay_prob': 0.10,          # 10% chance of operational delay
    'duration': 120              # Simulation length in minutes
}

### Scanning Time Ranges

REGULAR_SCAN_TIME = (2, 4)       # Min-max screening time (minutes)
PRIORITY_SCAN_TIME = (1.5, 3)    # Faster screening for priority passengers
RANDOM_CHECK_TIME = (3, 8)       # Additional time for random checks
DELAY_TIME = (1, 3)              # Additional time for delays

### Monitoring Settings

MONITOR_INTERVAL = 5             # Queue check frequency (minutes)
HIGH_QUEUE_THRESHOLD = 10        # Alert threshold for queue length

# 📊 Usage Examples

### Example 1: Peak Hour Analysis

Simulate a busy morning rush with high passenger volume:

from main import run_simulation

checkpoint = run_simulation(
    num_regular_lanes=5,
    num_priority_lanes=2,
    arrival_rate=2,              # Passenger every 2 minutes (high volume)
    priority_prob=0.30,          # 30% priority passengers
    duration=180                 # 3-hour simulation
)

### Example 2: Enhanced Security Protocol

Test impact of increased random security checks:

checkpoint = run_simulation(
    num_regular_lanes=3,
    num_priority_lanes=1,
    arrival_rate=5,
    random_check_prob=0.30,      # Doubled from 15% to 30%
    delay_prob=0.10,
    duration=120
)

### Example 3: Off-Peak Operations

Model low-traffic periods to optimize staffing:

checkpoint = run_simulation(
    num_regular_lanes=2,         # Reduced capacity
    num_priority_lanes=1,
    arrival_rate=10,             # Passenger every 10 minutes (low volume)
    priority_prob=0.15,
    duration=240                 # 4-hour simulation
)

### Example 4: Programmatic Access to Results

from main import run_simulation
import numpy as np

<!-- Run simulation -->
checkpoint = run_simulation(duration=120)

<!-- Access detailed statistics -->
wait_times = [s.queue_wait_time for s in checkpoint.passenger_stats]
service_times = [s.service_time for s in checkpoint.passenger_stats]

<!-- Calculate custom metrics -->
percentile_95_wait = np.percentile(wait_times, 95)
avg_service = np.mean(service_times)

print(f"95th percentile wait time: {percentile_95_wait:.2f} minutes")
print(f"Average service time: {avg_service:.2f} minutes")

<!-- Access specific passenger data -->
for passenger in checkpoint.passenger_stats[:5]:  # First 5 passengers
    print(f"Passenger {passenger.id}: Total time = {passenger.total_time:.2f}m")

# 📈 Output and Metrics

### Console Output

The simulation provides real-time event logging:


🛫 AIRPORT SECURITY CHECKPOINT SIMULATION
================================================================================
Configuration:
  - Regular Lanes: 3
  - Priority Lanes: 1
  - Average Arrival Rate: Every 5 minutes
  ...
================================================================================

⚠️  Time 23.4: Passenger 5 selected for random security check (+5.2 min)
⏱️  Time 45.7: Passenger 10 delayed due to metal detector alarm (+1.8 min)
✓ Time 48.2: Passenger 11 (Priority) completed security (wait: 0.0m, service: 2.3m)
🚨 Time 67.3: HIGH QUEUE ALERT! Regular lanes: 12 passengers waiting


### Statistical Summary
Comprehensive performance metrics are calculated and displayed:
#### Overall Statistics

    - Total passengers processed
    - Number and percentage of random checks
    - Number and percentage of delays

#### Wait Time Analysis

    - Average, maximum, minimum queue wait time
    - Standard deviation
    - Distribution characteristics

#### Service Time Analysis

    - Average, maximum, minimum screening time
    - Impact of random checks and delays

#### Total Time Analysis

    - End-to-end processing time metrics
    - Comparison across passenger types

#### Lane Utilization

    - Passengers processed per lane
    - Utilization rate for each lane
    - Load balancing assessment

#### Regular vs Priority Comparison

    - Wait time differences
    - Service time differences
    - Total processing time comparison

### Data Structures
Each passenger's journey is captured in a `PassengerStats` object:

@dataclass
class PassengerStats:
    id: int                      # Unique passenger identifier
    arrival_time: float          # When passenger arrived
    queue_entry_time: float      # When passenger joined queue
    service_start_time: float    # When screening began
    service_end_time: float      # When screening completed
    departure_time: float        # When passenger left checkpoint
    lane_used: int               # Which lane served this passenger
    had_random_check: bool       # Whether random check occurred
    had_delay: bool              # Whether delay occurred
    queue_wait_time: float       # Time spent waiting
    service_time: float          # Time spent in screening
    total_time: float            # Total time in system

# 📊 Visualization

The simulation automatically generates a comprehensive 6-panel visualization:

## Panel Descriptions

### 1. Queue Wait Time Distribution (Top-Left)

Histogram of passenger wait times
Mean wait time indicator
Identifies queue congestion patterns


### 2. Security Screening Time Distribution (Top-Middle)

Histogram of service durations
Shows impact of checks and delays
Mean service time indicator


### 3. Total Processing Time Distribution (Top-Right)

End-to-end time distribution
Combined effect of waiting + service
Performance overview metric


### 4. Wait Time vs Arrival Time (Bottom-Left)

Scatter plot showing temporal patterns
Identifies peak congestion periods
Reveals time-dependent behavior


### 5. Lane Utilization (Bottom-Middle)

Bar chart of passengers per lane
Color-coded by lane type (regular/priority)
Load balancing assessment


### 6. Impact of Random Checks and Delays (Bottom-Right)

Comparison of average times
Quantifies cost of security measures
Supports policy decision-making

## Customizing Visualizations

Modify `visualization.py` to customize plots:

    # Change color schemes
colors = ['skyblue', 'lightgreen', 'lightcoral']

    # Adjust figure size
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    # Add additional plots
axes[2, 0].plot(new_data)

    # Change save resolution
plt.savefig('output.png', dpi=600)

# 🔧 Extending the Simulation

## Adding New Features

### 1. Time-Varying Arrival Rates

Model realistic daily traffic patterns:

def time_varying_arrival_rate(env):
    """Arrival rate that varies by time of day"""
    hour = (env.now / 60) % 24
    if 6 <= hour < 9:
        return 2  # Morning rush
    elif 16 <= hour < 19:
        return 2.5  # Evening rush
    else:
        return 7  # Off-peak

### 2. Equipment Failures
Add reliability modeling:

def equipment_failure(env, checkpoint, lane_id, mtbf=300):
    """Simulate random equipment failures"""
    while True:
        yield env.timeout(random.expovariate(1/mtbf))
        print(f"⚠️  Lane {lane_id} equipment failure!")
        yield env.timeout(random.uniform(10, 30))  # Repair time
        print(f"✓ Lane {lane_id} back online")

### 3. Passenger Groups
Handle families traveling together:
def group_generator(env, checkpoint, group_prob=0.3):
    """Generate passenger groups (families)"""
    while True:
        if random.random() < group_prob:
            group_size = random.randint(2, 5)
            for _ in range(group_size):
                env.process(checkpoint.security_screening(...))
        else:
            env.process(checkpoint.security_screening(...))
        yield env.timeout(...)

### 4. Staff Breaks and Shifts
Model realistic workforce constraints:

def staff_breaks(env, checkpoint):
    """Reduce capacity during break times"""
    while True:
        yield env.timeout(120)  # Work 2 hours
        checkpoint.regular_lanes._capacity -= 1
        yield env.timeout(15)  # 15-minute break
        checkpoint.regular_lanes._capacity += 1

## Adding New Metrics
Track additional performance indicators in `checkpoint.py`:

    # In AirportSecurityCheckpoint.__init__:
self.missed_flights = 0
self.vip_passengers = 0
self.max_queue_length = 0

    # In security_screening method:
if queue_length > self.max_queue_length:
    self.max_queue_length = queue_length

# 🤝 Contributing
Contributions are welcome! Areas for enhancement:

    - Advanced queueing disciplines (FIFO, priority queues, reservation systems)
    - Machine learning integration for demand forecasting
    - Multi-terminal modeling with passenger transfers
    - Cost optimization algorithms
    - Real-time data integration from actual airport systems
    - Interactive dashboards using Plotly or Streamlit
    - Sensitivity analysis tools
    - Optimization algorithms for capacity planning

## Development Setup

    # Clone the repository
git clone https://github.com/yourusername/airport-security-simulation.git
cd airport-security-simulation

    # Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies
pip install -r requirements.txt

    # Run tests (if available)
python -m pytest tests/