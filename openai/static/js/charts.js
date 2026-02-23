/* ==========================================
   FALLVISION – Premium Chart System
   ========================================== */

Chart.defaults.font.family = "'Segoe UI', 'Inter', sans-serif";
Chart.defaults.color = "#6c757d";
Chart.defaults.plugins.legend.display = false;
Chart.defaults.elements.point.radius = 0;
Chart.defaults.elements.line.borderWidth = 3;
Chart.defaults.elements.line.tension = 0.4;

/* ==========================================
   Utility: Gradient Creator
========================================== */

function createGradient(ctx, colorStart, colorEnd) {
    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, colorStart);
    gradient.addColorStop(1, colorEnd);
    return gradient;
}

/* ==========================================
   Mobility Trend Chart
========================================== */

function renderMobilityChart(canvasId, data) {

    const ctx = document.getElementById(canvasId).getContext("2d");

    const gradient = createGradient(
        ctx,
        "rgba(244,180,0,0.4)",
        "rgba(244,180,0,0.02)"
    );

    new Chart(ctx, {
        type: "line",
        data: {
            labels: data.map((_, i) => "Day " + (i + 1)),
            datasets: [{
                data: data,
                borderColor: "#f4b400",
                backgroundColor: gradient,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 1200,
                easing: "easeOutQuart"
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: { color: "#999" }
                },
                y: {
                    grid: {
                        color: "rgba(0,0,0,0.05)"
                    },
                    ticks: {
                        color: "#999"
                    }
                }
            }
        }
    });
}

/* ==========================================
   Fall Risk Bar Chart
========================================== */

function renderRiskChart(canvasId, low, moderate, elevated) {

    const ctx = document.getElementById(canvasId).getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Low", "Moderate", "Elevated"],
            datasets: [{
                data: [low, moderate, elevated],
                backgroundColor: [
                    "#4caf50",
                    "#ff9800",
                    "#f44336"
                ],
                borderRadius: 12
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { display: false } },
                y: {
                    grid: { color: "rgba(0,0,0,0.05)" }
                }
            }
        }
    });
}

/* ==========================================
   Circular Progress (Brain Correlation)
========================================== */

function renderCircularScore(canvasId, score) {

    const ctx = document.getElementById(canvasId).getContext("2d");

    new Chart(ctx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [score * 100, 100 - score * 100],
                backgroundColor: ["#f4b400", "#f1f1f1"],
                borderWidth: 0
            }]
        },
        options: {
            cutout: "75%",
            plugins: { tooltip: { enabled: false } }
        }
    });
}