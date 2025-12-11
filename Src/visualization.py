"""
Visualization and plotting functions
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_results(checkpoint):
    """Create visualization of simulation results"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Airport Security Checkpoint Simulation Analysis', 
                 fontsize=16, fontweight='bold')
    
    if not checkpoint.passenger_stats:
        print("No data to plot")
        return
    
    # 1. Wait Time Distribution
    wait_times = [s.queue_wait_time for s in checkpoint.passenger_stats]
    axes[0, 0].hist(wait_times, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0, 0].set_xlabel('Wait Time (minutes)')
    axes[0, 0].set_ylabel('Number of Passengers')
    axes[0, 0].set_title('Queue Wait Time Distribution')
    axes[0, 0].axvline(np.mean(wait_times), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(wait_times):.2f}m')
    axes[0, 0].legend()
    
    # 2. Service Time Distribution
    service_times = [s.service_time for s in checkpoint.passenger_stats]
    axes[0, 1].hist(service_times, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
    axes[0, 1].set_xlabel('Service Time (minutes)')
    axes[0, 1].set_ylabel('Number of Passengers')
    axes[0, 1].set_title('Security Screening Time Distribution')
    axes[0, 1].axvline(np.mean(service_times), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(service_times):.2f}m')
    axes[0, 1].legend()
    
    # 3. Total Time Distribution
    total_times = [s.total_time for s in checkpoint.passenger_stats]
    axes[0, 2].hist(total_times, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
    axes[0, 2].set_xlabel('Total Time (minutes)')
    axes[0, 2].set_ylabel('Number of Passengers')
    axes[0, 2].set_title('Total Processing Time Distribution')
    axes[0, 2].axvline(np.mean(total_times), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(total_times):.2f}m')
    axes[0, 2].legend()
    
    # 4. Wait Time Over Time
    arrival_times = [s.arrival_time for s in checkpoint.passenger_stats]
    axes[1, 0].scatter(arrival_times, wait_times, alpha=0.5, color='purple')
    axes[1, 0].set_xlabel('Arrival Time (minutes)')
    axes[1, 0].set_ylabel('Wait Time (minutes)')
    axes[1, 0].set_title('Wait Time vs Arrival Time')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 5. Lane Utilization
    lane_names = list(checkpoint.lane_usage.keys())
    lane_counts = list(checkpoint.lane_usage.values())
    colors = ['steelblue' if 'Regular' in name else 'gold' for name in lane_names]
    axes[1, 1].bar(range(len(lane_names)), lane_counts, color=colors, edgecolor='black')
    axes[1, 1].set_xlabel('Security Lane')
    axes[1, 1].set_ylabel('Passengers Processed')
    axes[1, 1].set_title('Lane Utilization')
    axes[1, 1].set_xticks(range(len(lane_names)))
    axes[1, 1].set_xticklabels(lane_names, rotation=45, ha='right')
    
    # 6. Random Checks and Delays Impact
    checked = [s for s in checkpoint.passenger_stats if s.had_random_check]
    not_checked = [s for s in checkpoint.passenger_stats if not s.had_random_check]
    delayed = [s for s in checkpoint.passenger_stats if s.had_delay]
    not_delayed = [s for s in checkpoint.passenger_stats if not s.had_delay]
    
    categories = ['Random\nCheck', 'No Random\nCheck', 'Delayed', 'Not Delayed']
    avg_times = [
        np.mean([s.total_time for s in checked]) if checked else 0,
        np.mean([s.total_time for s in not_checked]) if not_checked else 0,
        np.mean([s.total_time for s in delayed]) if delayed else 0,
        np.mean([s.total_time for s in not_delayed]) if not_delayed else 0
    ]
    colors_bar = ['red', 'green', 'orange', 'lightblue']
    axes[1, 2].bar(categories, avg_times, color=colors_bar, edgecolor='black')
    axes[1, 2].set_ylabel('Average Total Time (minutes)')
    axes[1, 2].set_title('Impact of Random Checks and Delays')
    axes[1, 2].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('airport_security_simulation.png', dpi=300, bbox_inches='tight')
    print("\n📈 Visualization saved as 'airport_security_simulation.png'")
    plt.show()
