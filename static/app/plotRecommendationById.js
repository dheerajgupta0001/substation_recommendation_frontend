function loadPlotData(substationName) {
    // Sample data - replace with your own list of values
    // var dfData_g = dfData
    var dfData_g = dfData;
    var substationName = substationName;

    // Create x-axis values (indices of the data points)
    const xValues = Array.from({ length: dfData_g.length }, (_, i) => i);

    // Define the trace for the line chart
    const trace = {
    x: xValues,
    y: dfData_g,
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Values'
    };

    // Define the layout for the chart
    debugger;
    const layout = {
    title: substationName,
    yaxis: { title: 'Voltage' }
    };

    // Create the plot
    Plotly.newPlot(subStation, [trace], layout);

}

function loadPlotDetails(substationName, recommendation) {
    document.getElementById("recommendationField").innerHTML = recommendation;
    document.getElementById("subStationField").innerHTML = substationName;
}