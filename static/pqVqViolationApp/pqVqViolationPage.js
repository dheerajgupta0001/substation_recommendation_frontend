// Wait for the DOM to be ready
$(document).ready(function() {
    // Initialize the DataTable
    var activeTable = null;
    debugger
    var table1 = $('#pqVqViolationID').DataTable({
        columns: [
            { title: "Timestamp", data: "time_stamp" },
            { title: "Generating Substation", data: "generating_station" },
            { title: "Voltage", data: "voltage" },
            { title: "Substaion MVAr", data: "substation_mvar" },
            { title: "Farm P", data: "farm_p" },
            { title: "Farm Q", data: "farm_q" },
            { 
                title: "isVqViolated", 
                data: "isVqViolated",
                render: function(data) {
                    // Convert any truthy/falsy value to true/false
                    const boolValue = Boolean(data);
                    return `<span class="badge ${boolValue ? 'bg-danger' : 'bg-success'}">${boolValue ? 'Yes' : 'No'}</span>`;
                }
            },
            { 
                title: "isPqViolated", 
                data: "isPqViolated",
                render: function(data) {
                    const boolValue = Boolean(data);
                    return `<span class="badge ${boolValue ? 'bg-danger' : 'bg-success'}">${boolValue ? 'Yes' : 'No'}</span>`;
                }
            },
            { 
                title: "isPqVqViolated", 
                data: "isPqVqViolated",
                render: function(data) {
                    const boolValue = Boolean(data);
                    return `<span class="badge ${boolValue ? 'bg-danger' : 'bg-success'}">${boolValue ? 'Yes' : 'No'}</span>`;
                }
            }
        ],
        fixedHeader: true,
        "lengthMenu": [[10, 20, 50, 100, -1], [10, 20, 50, 100, "All"]],
        "pageLength": 50,
        dom: 'Bfrtip',
        "order": [[0, "desc"]],
        buttons: ['pageLength', 'csv', 'excel', 'pdf', 'print'],
        pageLength: 10,
        responsive: true,
        // select: true
        select: {
            style: 'single'
        }
    });

    // Function to refresh the DataTable
    function refreshDataTable() {
        // Add loading state to the button
        $('.btn-success').prop('disabled', true);
        $('.btn-success .fas').addClass('fa-spin');
        $.ajax({
            url: '/fetchPqVqViolation',
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                // Clear existing data and add new data
                table1.clear().rows.add(data['data']['data1']).draw();
                
                console.log('DataTable refreshed at ' + new Date().toLocaleTimeString());
            },
            error: function(xhr, status, error) {
                console.error("Error fetching data: " + error);
            },
            complete: function() {
                // Remove loading state from button
                $('.btn-success').prop('disabled', false);
                $('.btn-success .fas').removeClass('fa-spin');
            }
        });
    }

    // Function to start periodic refresh
    function startPeriodicRefresh() {
        // Refresh immediately on start
        refreshDataTable();
        
        // Set up interval to refresh every 30 seconds
        setInterval(refreshDataTable, 90000);
    }

    // Add click handler for the refresh button
    $('.btn-success').on('click', function() {
        refreshDataTable();
    });

    // Start the periodic refresh
    startPeriodicRefresh();
});