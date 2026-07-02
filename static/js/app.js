// ================================
// SchedScope JavaScript
// ================================

let processCount = 1;

// DOM Elements
const algorithmSelect = document.getElementById("algorithm");
const quantumBox = document.getElementById("quantumBox");
const processTable = document.querySelector("#processTable tbody");
const resultTable = document.querySelector("#resultTable tbody");
const ganttChart = document.getElementById("ganttChart");

const priorityHeader = document.getElementById("priorityHeader");

// ================================
// Toggle Inputs
// ================================

algorithmSelect.addEventListener("change", toggleInputs);

toggleInputs();

function toggleInputs() {

    quantumBox.style.display =
        algorithmSelect.value === "RR"
            ? "block"
            : "none";

    const showPriority =
        algorithmSelect.value === "Priority" ||
        algorithmSelect.value === "Priority Preemptive";

    priorityHeader.style.display =
        showPriority ? "" : "none";

    document.querySelectorAll(".priorityCell")
        .forEach(cell => {
            cell.style.display =
                showPriority ? "" : "none";
        });

}

// ================================
// Add Process
// ================================

document.getElementById("addProcess").addEventListener("click", () => {

    processCount++;

    const showPriority =
        algorithmSelect.value === "Priority" ||
        algorithmSelect.value === "Priority Preemptive";

    const row = document.createElement("tr");

    row.innerHTML = `

        <td>P${processCount}</td>

        <td>
            <input
                type="number"
                class="arrival"
                value="0"
                min="0">
        </td>

        <td>
            <input
                type="number"
                class="burst"
                value="1"
                min="1">
        </td>

        <td class="priorityCell"
            style="display:${showPriority ? "" : "none"};">

            <input
                type="number"
                class="priority"
                value="1"
                min="1">

        </td>

        <td>

            <button class="deleteBtn">
                ❌
            </button>

        </td>

    `;

    processTable.appendChild(row);

});

// ================================
// Delete Process
// ================================

processTable.addEventListener("click", function (e) {

    if (!e.target.classList.contains("deleteBtn"))
        return;

    if (processTable.rows.length === 1) {

        alert("At least one process is required.");

        return;

    }

    e.target.closest("tr").remove();

    renumberProcesses();

});

// ================================
// Renumber PIDs
// ================================

function renumberProcesses() {

    processCount = 0;

    [...processTable.rows].forEach(row => {

        processCount++;

        row.cells[0].textContent = `P${processCount}`;

    });

}

// ================================
// Run Simulation
// ================================

document.getElementById("simulate")
    .addEventListener("click", runSimulation);

async function runSimulation() {

    const processes = [];

    const rows = [...processTable.rows];

    for (let i = 0; i < rows.length; i++) {

        const pid = rows[i].cells[0].textContent;

        const arrival = parseInt(
            rows[i].querySelector(".arrival").value
        );

        const burst = parseInt(
            rows[i].querySelector(".burst").value
        );

        const priorityInput =
            rows[i].querySelector(".priority");

        const priority =
            priorityInput
                ? parseInt(priorityInput.value)
                : 0;

        if (isNaN(arrival) || arrival < 0) {

            alert("Arrival time must be 0 or greater.");

            return;

        }

        if (isNaN(burst) || burst <= 0) {

            alert("Burst time must be greater than 0.");

            return;

        }

        if (
            (algorithmSelect.value === "Priority" ||
                algorithmSelect.value === "Priority Preemptive")
            &&
            (isNaN(priority) || priority < 1)
        ) {

            alert("Priority must be at least 1.");

            return;

        }

        processes.push({

            pid,

            arrival,

            burst,

            priority

        });

    }

    const payload = {

        algorithm: algorithmSelect.value,

        quantum: document.getElementById("quantum").value,

        processes

    };

    const response = await fetch("/simulate", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(payload)

    });

    const data = await response.json();

    renderResults(data);

}

// ================================
// Render Results
// ================================

function renderResults(data) {

    renderMetrics(data);

    renderTable(data.processes);

    renderGantt(data.gantt);

}

// ================================
// Metrics
// ================================

function renderMetrics(data) {

    document.getElementById("avgWaiting").textContent =
        data.average_waiting;

    document.getElementById("avgTurnaround").textContent =
        data.average_turnaround;

    document.getElementById("avgResponse").textContent =
        data.average_response;

    document.getElementById("cpuUtil").textContent =
        data.cpu_utilization + "%";

    document.getElementById("throughput").textContent =
        data.throughput;

}

// ================================
// Results Table
// ================================

function renderTable(processes) {

    resultTable.innerHTML = "";

    processes.forEach(p => {

        const row = document.createElement("tr");

        row.innerHTML = `

        <td>${p.pid}</td>

        <td>${p.arrival}</td>

        <td>${p.burst}</td>

        <td>${p.priority ?? "-"}</td>

        <td>${p.completion}</td>

        <td>${p.waiting}</td>

        <td>${p.turnaround}</td>

        <td>${p.response}</td>

        `;

        resultTable.appendChild(row);

    });

}

// ================================
// Animated Gantt Chart
// ================================

function renderGantt(gantt) {

    ganttChart.innerHTML = "";

    gantt.forEach((block, index) => {

        setTimeout(() => {

            const wrapper = document.createElement("div");

            wrapper.style.display = "flex";

            wrapper.style.flexDirection = "column";

            wrapper.style.alignItems = "center";

            const div = document.createElement("div");

            div.className = "gantt-block " + block.pid;

            div.textContent = block.pid;

            div.style.width =
                ((block.end - block.start) * 50) + "px";

            const time = document.createElement("div");

            time.className = "gantt-time";

            time.innerHTML = `
                ${block.start}
                &nbsp;&nbsp;&nbsp;
                ${block.end}
            `;

            wrapper.appendChild(div);

            wrapper.appendChild(time);

            ganttChart.appendChild(wrapper);

        }, index * 250);

    });

}