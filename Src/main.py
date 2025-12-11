import pandas as pd
import simpy
from checkpoint import AirportSecurityCheckpoint
from generator import passenger_generator, monitor_queue
from statistics1 import print_statistics
from visualization import plot_results

def run_simulation(data_file, num_regular_lanes=3, num_priority_lanes=1):
    """
    Run the simulation using Trace Data from CSV
    """
    # Load Dataset
    try:
        df = pd.read_csv(data_file)
        print(f"📂 Loaded dataset '{data_file}' with {len(df)} passengers.")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Calculate simulation duration based on last arrival + buffer
    duration = df['Arrival_Time'].max() + 60
    
    print("🛫 AIRPORT SECURITY - TRACE DRIVEN SIMULATION")
    print("="*80)
    print(f"Configuration:")
    print(f"  - Regular Lanes: {num_regular_lanes}")
    print(f"  - Priority Lanes: {num_priority_lanes}")
    print(f"  - Input Data: {data_file}")
    print("="*80 + "\n")
    
    env = simpy.Environment()
    
    # Initialize Checkpoint 
    # (Note: probabilities are ignored in trace-driven mode)
    checkpoint = AirportSecurityCheckpoint(
        env, 
        num_regular_lanes=num_regular_lanes,
        num_priority_lanes=num_priority_lanes
    )
    
    # Start processes
    # Pass the dataframe 'df' to the generator
    env.process(passenger_generator(env, checkpoint, df))
    env.process(monitor_queue(env, checkpoint))
    
    # Run simulation
    env.run(until=duration)
    
    # Results
    print_statistics(checkpoint)
    plot_results(checkpoint)
    
    return checkpoint

if __name__ == "__main__":
    # SPECIFY YOUR DATASET FILE NAME HERE
    dataset_file = 'dataset.csv'
    
    # Run the simulation
    # You can change num_regular_lanes here to test different scenarios
    checkpoint = run_simulation(
        data_file=dataset_file,
        num_regular_lanes=3,  
        num_priority_lanes=1
    )
    
    print("\n" + "="*80)
    print("Simulation complete! Check the visualization.")
    print("="*80)