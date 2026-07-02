class Process:
    """
    Represents a CPU process.
    Stores both input values and scheduling results.
    """

    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)

        # Used by preemptive algorithms
        self.remaining_time = self.burst_time

        # Calculated during scheduling
        self.start_time = None
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1

    def calculate_metrics(self):
        """
        Calculate waiting, turnaround and response time.
        """
        self.turnaround_time = self.completion_time - self.arrival_time

        self.waiting_time = (
            self.turnaround_time - self.burst_time
        )

        if self.start_time is None:
            self.response_time = 0
        else:
            self.response_time = (
                self.start_time - self.arrival_time
            )

    def to_dict(self):
        """
        Convert object into JSON format.
        """
        return {
            "pid": self.pid,
            "arrival": self.arrival_time,
            "burst": self.burst_time,
            "priority": self.priority,
            "completion": self.completion_time,
            "waiting": self.waiting_time,
            "turnaround": self.turnaround_time,
            "response": self.response_time
        }

    def reset(self):
        """
        Reset scheduling values.
        Useful when running multiple algorithms.
        """
        self.remaining_time = self.burst_time
        self.start_time = None
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1

    def __repr__(self):
        return (
            f"{self.pid} "
            f"(AT={self.arrival_time}, "
            f"BT={self.burst_time}, "
            f"P={self.priority})"
        )