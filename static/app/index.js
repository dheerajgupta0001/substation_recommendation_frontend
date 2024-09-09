var table = $('#recommendationID').DataTable();

// Function to refresh the DataTable
function refreshDataTable() {
    // Clear the existing data
    table.clear();
    
    // Ajax call to fetch new data
    $.ajax({
        url: 'http://10.2.100.182:8094/fetchLatestRecommendation',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // Add new data to the table
            table.rows.add(data);
            // Redraw the table to reflect the new data
            table.draw();
            console.log('DataTable refreshed at ' + new Date().toLocaleTimeString());
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data: " + error);
            console.log(jqXHR);
            console.log(exception);
        }
    });
}

// Function to start periodic refresh
function startPeriodicRefresh() {
    // Refresh immediately on start
    refreshDataTable();
    
    // Set up interval to refresh every 30 seconds
    setInterval(refreshDataTable, 5000);
}