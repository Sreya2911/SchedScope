from collections import deque
from scheduler.metrics import Metrics


class RoundRobin:
    """
    Round Robin CPU Scheduling
    """

    def __init__(self, processes, quantum):
        self.processes = sorted(
            processes,
            key=lambda p: (p.arrival_time, p.pid)
        )
        self.quantum = quantum

    def run(self):
        processes = self.processes

        n = len(processes)

        current_time = 0
        completed = 0

        ready_queue = deque()
        gantt = []

        visited = [False] * n

        while completed < n:

            # Add newly arrived processes
            for i in range(n):
                if (
                    not visited[i]
                    and processes[i].arrival_time <= current_time
                ):
                    ready_queue.append(processes[i])
                    visited[i] = True

            # CPU Idle
            if not ready_queue:

                future = [
                    p.arrival_time
                    for i, p in enumerate(processes)
                    if not visited[i]
                ]

                if not future:
                    break

                next_arrival = min(future)

                gantt.append({
                    "pid": "Idle",
                    "start": current_time,
                    "end": next_arrival
                })

                current_time = next_arrival

                continue

            process = ready_queue.popleft()

            # Record response time
            if process.start_time is None:
                process.start_time = current_time

            execution = min(
                self.quantum,
                process.remaining_time
            )

            start = current_time
            end = current_time + execution

            gantt.append({
                "pid": process.pid,
                "start": start,
                "end": end
            })

            current_time = end

            process.remaining_time -= execution

            # Add any processes that arrived during execution
            for i in range(n):
                if (
                    not visited[i]
                    and processes[i].arrival_time <= current_time
                ):
                    ready_queue.append(processes[i])
                    visited[i] = True

            # Finished?
            if process.remaining_time == 0:

                process.completion_time = current_time
                completed += 1

            else:

                ready_queue.append(process)

        return Metrics.calculate(processes, gantt)