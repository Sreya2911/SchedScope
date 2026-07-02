from scheduler.metrics import Metrics


class Priority:

    def __init__(self, processes):
        self.processes = sorted(
            processes,
            key=lambda x: x.arrival_time
        )

    def run(self):

        n = len(self.processes)

        completed = 0
        current_time = 0

        visited = [False] * n

        gantt = []

        while completed < n:

            idx = -1
            best_priority = float("inf")

            for i in range(n):

                if (
                    self.processes[i].arrival_time <= current_time
                    and not visited[i]
                ):

                    if self.processes[i].priority < best_priority:

                        best_priority = self.processes[i].priority
                        idx = i

            if idx == -1:
                current_time += 1
                continue

            if self.processes[idx].start_time is None:
                self.processes[idx].start_time = current_time

            start = current_time

            current_time += self.processes[idx].burst_time

            self.processes[idx].completion_time = current_time

            gantt.append(
                {
                    "pid": self.processes[idx].pid,
                    "start": start,
                    "end": current_time,
                }
            )

            visited[idx] = True
            completed += 1

        return Metrics.calculate(
            self.processes,
            gantt
        )