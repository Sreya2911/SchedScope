from scheduler.metrics import Metrics


class FCFS:
    """
    First Come First Serve Scheduling
    Non-preemptive
    """

    def __init__(self, processes):
        # Sort by arrival time first, then PID
        self.processes = sorted(
            processes,
            key=lambda p: (p.arrival_time, p.pid)
        )

    def run(self):
        current_time = 0
        gantt = []

        for process in self.processes:

            # CPU Idle
            if current_time < process.arrival_time:
                gantt.append({
                    "pid": "Idle",
                    "start": current_time,
                    "end": process.arrival_time
                })

                current_time = process.arrival_time

            # Process starts
            process.start_time = current_time

            start = current_time
            end = current_time + process.burst_time

            process.completion_time = end

            gantt.append({
                "pid": process.pid,
                "start": start,
                "end": end
            })

            current_time = end

        return Metrics.calculate(self.processes, gantt)