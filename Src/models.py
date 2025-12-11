"""
Data models for the airport security simulation
"""
from dataclasses import dataclass

@dataclass
class PassengerStats:
    """Store statistics for each passenger"""
    id: int
    arrival_time: float
    queue_entry_time: float
    service_start_time: float
    service_end_time: float
    departure_time: float
    lane_used: int
    had_random_check: bool
    had_delay: bool
    queue_wait_time: float
    service_time: float
    total_time: float

