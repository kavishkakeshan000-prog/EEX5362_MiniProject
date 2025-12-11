"""
Airport Security Checkpoint implementation
"""
import simpy
import random
from collections import defaultdict
from models import PassengerStats

class AirportSecurityCheckpoint:
    """
    Airport Security Checkpoint Simulation
    """
    
    def __init__(self, env, num_regular_lanes=3, num_priority_lanes=1,
                 regular_scan_time=(2, 4), priority_scan_time=(1.5, 3),
                 random_check_prob=0.15, delay_prob=0.10):
        self.env = env
        
        # Resources (security lanes)
        self.regular_lanes = simpy.Resource(env, capacity=num_regular_lanes)
        self.priority_lanes = simpy.Resource(env, capacity=num_priority_lanes)
        
        # Configuration
        self.num_regular_lanes = num_regular_lanes
        self.num_priority_lanes = num_priority_lanes
        self.regular_scan_time = regular_scan_time
        self.priority_scan_time = priority_scan_time
        self.random_check_prob = random_check_prob
        self.delay_prob = delay_prob
        
        # State tracking
        self.total_passengers = 0
        self.random_checks = 0
        self.delays = 0
        self.passenger_stats = []
        self.queue_lengths = defaultdict(list)
        self.queue_times = defaultdict(list)
        self.lane_usage = defaultdict(int)

    def security_screening(self, passenger_id, is_priority=False, 
                         fixed_service_time=None, 
                         forced_random_check=False, 
                         forced_delay=False):
        """Process a passenger through security screening using provided data"""
        arrival_time = self.env.now
        
        # Select lane
        if is_priority:
            lane_resource = self.priority_lanes
            lane_type = 'priority'
        else:
            lane_resource = self.regular_lanes
            lane_type = 'regular'
        
        # Record queue length
        queue_length = len(lane_resource.queue) + len(lane_resource.users)
        self.queue_lengths[lane_type].append((self.env.now, queue_length))
        
        queue_entry_time = self.env.now
        
        # Request a security lane
        with lane_resource.request() as request:
            yield request
            
            service_start_time = self.env.now
            queue_wait_time = service_start_time - queue_entry_time
            self.queue_times[lane_type].append(queue_wait_time)
            
            # Determine specific lane ID
            lane_id = f"{lane_type.capitalize()}-{len(lane_resource.users)}"
            self.lane_usage[lane_id] += 1
            
            # --- LOGIC CHANGE: USE DATASET VALUES IF AVAILABLE ---
            if fixed_service_time is not None:
                # Use the exact service time from the dataset
                scan_time = fixed_service_time
                had_random_check = forced_random_check
                had_delay = forced_delay
                
                # Log checks/delays (Trace Data)
                if had_random_check:
                    self.random_checks += 1
                if had_delay:
                    self.delays += 1
            
            else:
                # Fallback to original random logic
                scan_time = random.uniform(*(self.priority_scan_time if is_priority else self.regular_scan_time))
                had_random_check = False
                had_delay = False
                
                # Check for random security check
                if random.random() < self.random_check_prob:
                    had_random_check = True
                    self.random_checks += 1
                    # Add extra time for check
                    scan_time += random.uniform(3, 8) 

                # Check for operational delay
                if random.random() < self.delay_prob:
                    had_delay = True
                    self.delays += 1
                    scan_time += random.uniform(1, 3)

            # Process through security
            yield self.env.timeout(scan_time)
            
            service_end_time = self.env.now
            total_time = service_end_time - arrival_time
            
            # Record statistics
            stats = PassengerStats(
                id=passenger_id,
                arrival_time=arrival_time,
                queue_entry_time=queue_entry_time,
                service_start_time=service_start_time,
                service_end_time=service_end_time,
                departure_time=service_end_time,
                lane_used=len(lane_resource.users),
                had_random_check=had_random_check,
                had_delay=had_delay,
                queue_wait_time=queue_wait_time,
                service_time=scan_time,
                total_time=total_time
            )
            self.passenger_stats.append(stats)