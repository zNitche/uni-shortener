async function getData(url) {
    const options = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        }

    const response = await fetch(url, options);

    return response.json();
}


async function getHoursData(day) {
    let data = await getData("/api/redirects_per_hour/" + day)

    let xValues = Object.keys(data);
    let yValues = [];

    xValues.forEach((hour) => {
        yValues.push(data[hour])
    });

    return {
        "x": xValues,
        "y": yValues
    }
}


async function initHoursGraph() {
    const date = new Date();
    let data = await getHoursData(date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate());

    createLinearChart("hoursGraph", data.x, data.y);
}


async function updateHoursGraph(dateInput) {
    let data = await getHoursData(dateInput.value);
    updateChartData("hoursGraph", data.x, data.y);
}


async function getDaysData(month) {
    let data = await getData("/api/redirects_per_day/" + month)

    let xValues = Object.keys(data);
    let yValues = [];

    xValues.forEach((hour) => {
        yValues.push(data[hour])
    });

    return {
        "x": xValues,
        "y": yValues
    }
}


async function initDaysGraph() {
    const date = new Date();
    let data = await getDaysData(date.getFullYear() + "-" + (date.getMonth() + 1));

    createLinearChart("daysGraph", data.x, data.y);
}


async function updateDaysGraph(dateInput) {
    let data = await getDaysData(dateInput.value);
    updateChartData("daysGraph", data.x, data.y);
}


function createLinearChart(chartID, xValues, yValues) {
    new Chart(chartID, {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor:"#fff",
          borderColor: "#8DB580",
          data: yValues
        }]
      },
      options: {
        plugins: {
            legend: {
                display: false
            },
        },
        scales: {
            yAxes: {
                display: true,
                ticks: {
                    suggestedMin: 0,
                }
            }
        }
      }
    });

    Chart.defaults.color = "#fff";
}

function updateChartData(chartID, xValues, yValues) {
    const chart = Chart.getChart(chartID);

    if (chart) {
        chart.data.labels = xValues;
        chart.data.datasets[0].data = yValues;

        chart.update();
    }
}
