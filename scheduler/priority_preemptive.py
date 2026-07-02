from scheduler.metrics import Metrics


class PriorityPreemptive:

    def __init__(self, processes):
        self.processes = sorted(
            processes,
            key=lambda x: x.arrival_time
        )

    def run(self):

        n = len(self.processes)

        remaining = [p.burst_time for p in self.processes]

        completed = 0
        current_time = 0

        gantt = []

        while completed < n:

            idx = -1
            best_priority = float("inf")

            for i in range(n):

                if (
                    self.processes[i].arrival_time <= current_time
                    and remaining[i] > 0
                ):

                    if self.processes[i].priority < best_priority:

                        best_priority = self.processes[i].priority
                        idx = i

            if idx == -1:
                current_time += 1
                continue

            if self.processes[idx].start_time is None:
                self.processes[idx].start_time = current_time

            if (
                gantt
                and gantt[-1]["pid"] == self.processes[idx].pid
            ):

                gantt[-1]["end"] += 1

            else:

                gantt.append({
                    "pid": self.processes[idx].pid,
                    "start": current_time,
                    "end": current_time + 1
                })

            remaining[idx] -= 1

            current_time += 1

            if remaining[idx] == 0:

                completed += 1

                self.processes[idx].completion_time = current_time

        return Metrics.calculate(
            self.processes,
            gantt
        )