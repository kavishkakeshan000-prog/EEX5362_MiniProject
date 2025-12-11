"""
Passenger generation from Dataset
"""
import simpy

def passenger_generator(env, checkpoint, passenger_data):
    """
    Generate passengers based on the CSV dataset.
    
    Parameters:
    - passenger_data: pandas DataFrame containing the schedule
    """
    # Ensure data is sorted by arrival time
    sorted_data = passenger_data.sort_values('Arrival_Time')
    
    for index, row in sorted_data.iterrows():
        # Calculate time until this passenger arrives
        time_until_arrival = row['Arrival_Time'] - env.now
        
        # Wait until arrival time (if time is positive)
        if time_until_arrival > 0:
            yield env.timeout(time_until_arrival)
            
        # Extract attributes from dataset
        p_id = row['Passenger_ID']
        
        # Determine priority based on 'Lane_Type' in CSV
        is_priority = (row['Lane_Type'].strip() == 'Priority')
        
        # Extract the Service Time from CSV
        # IMPORTANT: This allows us to replicate the exact workload
        service_time = row['Service_Time']
        
        # Extract flags
        has_check = (str(row['Random_Check']).strip() == 'Yes')
        has_delay = (str(row['Operational_Delay']).strip() == 'Yes')
        
        # Start security screening process with FORCED values
        env.process(checkpoint.security_screening(
            passenger_id=p_id, 
            is_priority=is_priority,
            fixed_service_time=service_time,
            forced_random_check=has_check,
            forced_delay=has_delay
        ))
        
        checkpoint.total_passengers += 1

def monitor_queue(env, checkpoint, interval=5):
    """Monitor queue lengths at regular intervals"""
    while True:
        regular_queue = len(checkpoint.regular_lanes.queue)
        priority_queue = len(checkpoint.priority_lanes.queue)
        
        if regular_queue > 10:
            print(f"🚨 Time {env.now:.1f}: HIGH QUEUE ALERT! Regular lanes: {regular_queue} waiting")
        
        yield env.timeout(interval)