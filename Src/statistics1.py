"""
Statistics calculation and reporting
"""
import numpy as np

def print_statistics(checkpoint):
    """Print comprehensive statistics"""
    print("\n" + "="*80)
    print("AIRPORT SECURITY CHECKPOINT - SIMULATION RESULTS")
    print("="*80)
    
    # Basic statistics
    print(f"\n📊 OVERALL STATISTICS")
    print(f"   Total Passengers Processed: {checkpoint.total_passengers}")
    print(f"   Random Security Checks: {checkpoint.random_checks} ({checkpoint.random_checks/checkpoint.total_passengers*100:.1f}%)")
    print(f"   Delays Encountered: {checkpoint.delays} ({checkpoint.delays/checkpoint.total_passengers*100:.1f}%)")
    
    # Wait time statistics
    if checkpoint.passenger_stats:
        wait_times = [s.queue_wait_time for s in checkpoint.passenger_stats]
        service_times = [s.service_time for s in checkpoint.passenger_stats]
        total_times = [s.total_time for s in checkpoint.passenger_stats]
        
        print(f"\n⏱️  WAIT TIME ANALYSIS")
        print(f"   Average Queue Wait: {np.mean(wait_times):.2f} minutes")
        print(f"   Max Queue Wait: {np.max(wait_times):.2f} minutes")
        print(f"   Min Queue Wait: {np.min(wait_times):.2f} minutes")
        print(f"   Std Dev: {np.std(wait_times):.2f} minutes")
        
        print(f"\n🔍 SERVICE TIME ANALYSIS")
        print(f"   Average Service Time: {np.mean(service_times):.2f} minutes")
        print(f"   Max Service Time: {np.max(service_times):.2f} minutes")
        print(f"   Min Service Time: {np.min(service_times):.2f} minutes")
        
        print(f"\n⏰ TOTAL TIME ANALYSIS")
        print(f"   Average Total Time: {np.mean(total_times):.2f} minutes")
        print(f"   Max Total Time: {np.max(total_times):.2f} minutes")
        print(f"   Min Total Time: {np.min(total_times):.2f} minutes")
        
        # Lane utilization
        print(f"\n🛂 LANE UTILIZATION")
        for lane, count in sorted(checkpoint.lane_usage.items()):
            print(f"   {lane}: {count} passengers")
        
        # Regular vs Priority comparison
        regular_passengers = [s for s in checkpoint.passenger_stats 
                            if s.lane_used <= checkpoint.num_regular_lanes]
        priority_passengers = [s for s in checkpoint.passenger_stats 
                             if s.lane_used > checkpoint.num_regular_lanes]
        
        if regular_passengers and priority_passengers:
            print(f"\n✈️  REGULAR vs PRIORITY LANES")
            print(f"   Regular Lane Avg Wait: {np.mean([p.queue_wait_time for p in regular_passengers]):.2f} min")
            print(f"   Priority Lane Avg Wait: {np.mean([p.queue_wait_time for p in priority_passengers]):.2f} min")
            print(f"   Regular Lane Avg Total: {np.mean([p.total_time for p in regular_passengers]):.2f} min")
            print(f"   Priority Lane Avg Total: {np.mean([p.total_time for p in priority_passengers]):.2f} min")
