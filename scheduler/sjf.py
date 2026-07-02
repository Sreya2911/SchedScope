from scheduler.metrics import Metrics


class SJF:
    """
    Non-Preemptive Shortest Job First Scheduling
    """

    def __init__(self, processes):
        self.processes = processes

    def run(self):
        processes = sorted(
            self.processes,
            key=lambda p: (p.arrival_time, p.pid)
        )

        n = len(processes)
        completed = 0
        current_time = 0
        visited = [False] * n
        gantt = []

        while completed < n:

            available = []

            # Find all processes that have arrived
            for i in range(n):
                if (
                    not visited[i]
                    and processes[i].arrival_time <= current_time
                ):
                    available.append((i, processes[i]))

            # If no process is available, CPU is idle
            if not available:

                next_arrival = min(
                    p.arrival_time
                    for i, p in enumerate(processes)
                    if not visited[i]
                )

                gantt.append({
                    "pid": "Idle",
                    "start": current_time,
                    "end": next_arrival
                })

                current_time = next_arrival
                continue

            # Select process with shortest burst time
            index, process = min(
                available,
                key=lambda x: (
                    x[1].burst_time,
                    x[1].arrival_time,
                    x[1].pid
                )
            )

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
            visited[index] = True
            completed += 1

        return Metrics.calculate(processes, gantt)