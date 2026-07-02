from flask import Flask, render_template, request, jsonify

from scheduler.process import Process

from scheduler.fcfs import FCFS
from scheduler.sjf import SJF
from scheduler.srtf import SRTF
from scheduler.round_robin import RoundRobin
from scheduler.priority import Priority
from scheduler.priority_preemptive import PriorityPreemptive

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulator")
def simulator():
    return render_template("simulator.html")


@app.route("/simulate", methods=["POST"])
def simulate():

    data = request.get_json()

    algorithm = data.get("algorithm")
    quantum = int(data.get("quantum", 2))

    process_data = data.get("processes", [])

    processes = []

    for p in process_data:

        processes.append(
            Process(
                pid=p["pid"],
                arrival_time=int(p["arrival"]),
                burst_time=int(p["burst"]),
                priority=int(p.get("priority", 0))
            )
        )

    if algorithm == "FCFS":
        scheduler = FCFS(processes)

    elif algorithm == "SJF":
        scheduler = SJF(processes)

    elif algorithm == "SRTF":
        scheduler = SRTF(processes)

    elif algorithm == "RR":
        scheduler = RoundRobin(processes, quantum)

    elif algorithm == "Priority":
        scheduler = Priority(processes)

    elif algorithm == "Priority Preemptive":
        scheduler = PriorityPreemptive(processes)

    else:
        return jsonify({"error": "Invalid Algorithm"}), 400

    result = scheduler.run()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)