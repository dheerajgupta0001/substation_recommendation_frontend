// Wait for the DOM to be ready
$(document).ready(function() {
    // Initialize the DataTable
    var table = $('#recommendationID').DataTable({
        columns: [
            { title: "Timestamp", data: "time_stamp" },
            { title: "Substation Name", data: "substation_name" },
            { title: "Recommendation", data: "recommendation" },
            { title: "Voltage", data: "voltage_str" }
        ],
        fixedHeader: true,
        "lengthMenu": [[10, 20, 50, 100, -1], [10, 20, 50, 100, "All"]],
        "pageLength": 50,
        dom: 'Bfrtip',
        "order": [[0, "desc"]],
        buttons: ['pageLength', 'csv', 'excel', 'pdf', 'print'],
        pageLength: 10,
        responsive: true
    });

    // Function to refresh the DataTable
    function refreshDataTable() {
        $.ajax({
            url: 'http://localhost:8093/fetchLatestRecommendation',
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                // Clear existing data and add new data
                table.clear().rows.add(data['data']).draw();
                // debugger;
                console.log('DataTable refreshed at ' + new Date().toLocaleTimeString());
            },
            error: function(xhr, status, error) {
                console.error("Error fetching data: " + error);
            }
        });
    }

    // Function to start periodic refresh
    function startPeriodicRefresh() {
        // Refresh immediately on start
        refreshDataTable();
        
        // Set up interval to refresh every 30 seconds
        setInterval(refreshDataTable, 30000);
    }

    // Start the periodic refresh
    startPeriodicRefresh();
});