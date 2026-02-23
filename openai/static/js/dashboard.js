const ctx = document.getElementById('movementChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Right Arm', 'Left Arm', 'Right Leg', 'Left Leg'],
        datasets: [{
            label: 'Limb Angles',
            data: [90, 110, 70, 85],
        }]
    }
});