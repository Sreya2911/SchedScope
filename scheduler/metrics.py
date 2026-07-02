class Metrics:
    """
    Calculates scheduling statistics and prepares
    the final JSON response.
    """

    @staticmethod
    def calculate(processes, gantt):
        n = len(processes)

        if n == 0:
            return {
                "processes": [],
                "gantt": [],
                "average_waiting": 0,
                "average_turnaround": 0,
                "average_response": 0,
                "cpu_utilization": 0,
                "throughput": 0
            }

        total_waiting = 0
        total_turnaround = 0
        total_response = 0

        # Calculate metrics for each process
        for process in processes:
            process.calculate_metrics()

            total_waiting += process.waiting_time
            total_turnaround += process.turnaround_time
            total_response += process.response_time

        average_waiting = round(total_waiting / n, 2)
        average_turnaround = round(total_turnaround / n, 2)
        average_response = round(total_response / n, 2)

        finish_time = max(
            (p.completion_time for p in processes),
            default=0
        )

        # Total CPU busy time from Gantt Chart
        busy_time = sum(
            segment["end"] - segment["start"]
            for segment in gantt
        )

        cpu_utilization = (
            round((busy_time / finish_time) * 100, 2)
            if finish_time > 0 else 0
        )

        throughput = (
            round(n / finish_time, 2)
            if finish_time > 0 else 0
        )

        return {
            "processes": [
                p.to_dict()
                for p in sorted(processes, key=lambda x: x.pid)
            ],

            "gantt": gantt,

            "average_waiting": average_waiting,

            "average_turnaround": average_turnaround,

            "average_response": average_response,

            "cpu_utilization": cpu_utilization,

            "throughput": throughput,

            # Extra values useful for charts/statistics
            "finish_time": finish_time,
            "busy_time": busy_time,
            "process_count": n
        }