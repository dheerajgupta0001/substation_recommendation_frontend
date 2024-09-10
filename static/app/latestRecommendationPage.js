// Wait for the DOM to be ready
$(document).ready(function() {
    // Initialize the DataTable
    var activeTable = null;

    // send selected data
    function sendSelectedData(data) {
        // $('#selectedTableId').val(tableId);
        $('#selectedData').val(JSON.stringify(data));
        $('#selectedDataForm').submit();
    }


    var table1 = $('#recommendationID').DataTable({
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
        responsive: true,
        // select: true
        select: {
            style: 'single'
        }
    });

    var table2 = $('#informationalRecommendation').DataTable({
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
        responsive: true,
        select: {
            style: 'single'
        }
    });

    // Function to handle table activation
    function activateTable(table) {
        if (activeTable && activeTable !== table) {
            activeTable.rows().deselect();
        }
        activeTable = table;
    }

    // Event listener for row selection on table1
    table1.on('select', function (e, dt, type, indexes) {
        if (type === 'row') {
            activateTable(table1);
            var data = table1.rows(indexes).data().toArray();
            id = data[0];
            // debugger;
            console.log('Selected data from table1:', data);
            // sendSelectedData('table1', id);
            sendSelectedData(id);
            // Do something with the selected data
        }
    });

    // Event listener for row selection on table2
    table2.on('select', function (e, dt, type, indexes) {
        if (type === 'row') {
            activateTable(table2);
            var data = table2.rows(indexes).data().toArray();
            id = data[0];
            console.log('Selected data from table2:', data);
            sendSelectedData(id);
            // Do something with the selected data
        }
    });

    // Event listeners for table focus
    $('#table1').on('click', function() {
        activateTable(table1);
    });

    $('#table2').on('click', function() {
        activateTable(table2);
    });

    // Function to refresh the DataTable
    function refreshDataTable() {
        $.ajax({
            url: 'http://localhost:8093/fetchLatestRecommendation',
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                // Clear existing data and add new data
                table1.clear().rows.add(data['data']['data1']).draw();
                // debugger;
                table2.clear().rows.add(data['data']['data2']).draw();
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
        setInterval(refreshDataTable, 90000);
    }

    // Start the periodic refresh
    startPeriodicRefresh();
});