<div align="center">

# SchedScope

### Interactive CPU Scheduling Algorithm Simulator

Visualize, compare, and analyze CPU scheduling algorithms through an intuitive web interface featuring animated Gantt charts and performance analytics.

[Features](#features) •
[Algorithms](#implemented-algorithms) •
[Installation](#installation) •
[Project Structure](#project-structure)

</div>

---

## Overview

SchedScope is a web-based CPU Scheduling Algorithm Simulator designed to simplify the understanding of process scheduling concepts in Operating Systems.

The application provides an interactive environment where users can create processes, execute different scheduling algorithms, visualize execution through animated Gantt charts, and analyze scheduling performance using standard metrics.

Built with Flask and vanilla JavaScript, SchedScope focuses on combining educational value with a clean and modern user experience.

---

## Features

- Interactive CPU scheduling simulator
- Animated Gantt Chart visualization
- Real-time scheduling execution
- Process-wise execution table
- Performance metrics dashboard
- Responsive modern interface
- Glassmorphism-inspired UI
- Dynamic process creation and deletion
- Input validation for process parameters

---

## Implemented Algorithms

| Algorithm | Type |
|-----------|------|
| First Come First Serve (FCFS) | Non-Preemptive |
| Shortest Job First (SJF) | Non-Preemptive |
| Shortest Remaining Time First (SRTF) | Preemptive |
| Round Robin (RR) | Preemptive |
| Priority Scheduling | Non-Preemptive |
| Priority Scheduling | Preemptive |

---

## Performance Metrics

The simulator computes the following scheduling metrics:

- Average Waiting Time
- Average Turnaround Time
- Average Response Time
- CPU Utilization
- Throughput

These metrics allow users to compare the efficiency of different scheduling algorithms under identical workloads.

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```text
SchedScope/
│
├── scheduler/
│   ├── process.py
│   ├── metrics.py
│   ├── fcfs.py
│   ├── sjf.py
│   ├── srtf.py
│   ├── round_robin.py
│   ├── priority.py
│   └── priority_preemptive.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── simulator.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Sreya2911/SchedScope.git
```

### Navigate to the project

```bash
cd SchedScope
```

### Create a virtual environment (optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Usage

1. Select a scheduling algorithm.
2. Add one or more processes.
3. Enter arrival time, burst time, and priority (where applicable).
4. Specify the time quantum for Round Robin.
5. Run the simulation.
6. Analyze the generated Gantt chart and scheduling metrics.

---

## Screenshots

> Screenshots will be added after deployment.

Suggested screenshots:

- Landing Page
- Simulator Interface
- Animated Gantt Chart
- Performance Metrics Dashboard

---

## Future Enhancements

- Additional scheduling algorithms
- Algorithm comparison mode
- Export simulation results (CSV/PDF)
- Dark and Light theme support
- Learning module for scheduling concepts
- Interactive ready queue visualization
- Timeline playback controls

---

## Learning Outcomes

This project demonstrates practical implementation of:

- CPU Scheduling Algorithms
- Operating System Concepts
- Flask Web Development
- Client-Server Communication
- RESTful Request Handling
- JavaScript DOM Manipulation
- Responsive Web Design
- Data Visualization

---

## Contributing

Contributions, feature requests, and suggestions are welcome.

If you would like to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## Author

**Sreya S**

- GitHub: https://github.com/Sreya2911
- LinkedIn: *(Add your LinkedIn profile here)*

---

## License

This project is released for educational and learning purposes.
