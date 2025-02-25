// Wait for the DOM to be ready
$(document).ready(function() {
    // Initialize the DataTable
    var activeTable = null;
    var startDate = null;
    var endDate = null;
    debugger

    // send mail button ID starts
    // Add click handler for the send mail button
    $('#sendMailBtn').on('click', function() {
        // Get all data from the DataTable
        const tableData = $('#pqVqViolationID').DataTable().data().toArray();
        
        // Filter for violated records only
        const violatedRecords = tableData
            .filter(record => record.isPqViolated || record.isVqViolated || record.isPqVqViolated)
            .map(record => record.generating_station);
            
        // Create the data object to send
        const dataToSend = {
            timestamp: new Date().toISOString(),
            violations: violatedRecords,
            summary: {
                totalRecords: tableData.length,
                violatedRecords: violatedRecords.length
            }
        };
        // Add loading state to the button
        $('#sendMailBtn').prop('disabled', true);
        $('#sendMailBtn .fas').addClass('fa-spin');
        $.ajax({
            url: '/sendPqVqViolationMail',
            method: 'POST',
            dataType: 'json',
            contentType: 'application/json',  // Specify content type
            data: JSON.stringify(dataToSend), // Convert data to JSON string
            success: function(response) {
                // Show success message
                alert('Mail sent successfully!');
                console.log('Mail sent at ' + new Date().toLocaleTimeString());
            },
            error: function(xhr, status, error) {
                // Show error message with more details
                const errorMessage = xhr.responseJSON?.message || error || 'Unknown error occurred';
                alert('Error sending mail: ' + errorMessage);
                console.error("Error sending mail:", {
                    status: status,
                    error: error,
                    details: xhr.responseText
                });
            },
            complete: function() {
                // Remove loading state from button
                $('#sendMailBtn').prop('disabled', false);
                $('#sendMailBtn .fas').removeClass('fa-spin');
            }
        });
    });
    // send mail button ID ends

    // Set default date values (last 6 hours)
    function setDefaultDates() {
        const now = new Date();
        const sixHoursAgo = new Date(now);
        sixHoursAgo.setHours(now.getHours() - 6);
        
        // Format for datetime-local input
        // const formatDate = (date) => {
        //     return date.toISOString().slice(0, 16);
        // };
        
        // $('#startDate').val(formatDate(sixHoursAgo));
        // $('#endDate').val(formatDate(now));

        // Format for datetime-local input (in local time zone)
        const formatDateForInput = (date) => {
            const year = date.getFullYear();
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const day = String(date.getDate()).padStart(2, '0');
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            
            // This format works with datetime-local inputs
            return `${year}-${month}-${day}T${hours}:${minutes}`;
        };
    
        $('#startDate').val(formatDateForInput(sixHoursAgo));
        $('#endDate').val(formatDateForInput(now));
        
        startDate = sixHoursAgo;
        endDate = now;
    }
    
    // Set default dates on page load
    setDefaultDates();

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
        },
        createdRow: function(row, data, dataIndex) {
            // Add hover classes based on violation conditions
            if (Boolean(data.isPqVqViolated)) {
                $(row).addClass('violation-pqvq-hover');
            } else if (Boolean(data.isVqViolated)) {
                $(row).addClass('violation-vq-hover');
            } else if (Boolean(data.isPqViolated)) {
                $(row).addClass('violation-pq-hover');
            } else {
                $(row).addClass('no-violation-hover');
            }
        }
    });

    // Function to refresh the DataTable
    function refreshDataTable() {
        // Add loading state to the button
        $('.btn-success').prop('disabled', true);
        $('.btn-success .fas').addClass('fa-spin');

        // Get current date filter values
        const startDateVal = $('#startDate').val() ? new Date($('#startDate').val()).toISOString() : null;
        const endDateVal = $('#endDate').val() ? new Date($('#endDate').val()).toISOString() : null;
        

        $.ajax({
            url: '/fetchPqVqViolation',
            method: 'GET',
            dataType: 'json',
            // start Date & end Date
            data: {
                startDate: startDateVal,
                endDate: endDateVal
            },
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
    
    // Add click handler for the apply filter button
    $('#applyDateFilter').on('click', function() {
        refreshDataTable();
    });
    
    // Add click handler for the reset filter button
    $('#resetDateFilter').on('click', function() {
        setDefaultDates();
        refreshDataTable();
    });

    // Start the periodic refresh
    startPeriodicRefresh();
});