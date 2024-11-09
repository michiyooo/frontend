function changeOrder(button) {
    // Logic to change the order status
    const row = button.parentElement.parentElement; // Get the row
    const statusSelect = row.querySelector('select'); // Get the status dropdown
    const selectedStatus = statusSelect.value; // Get the selected value
    alert('Order status changed to: ' + selectedStatus);
    // Add your logic to update the order status in the database
}

function deleteOrder(button) {
    // Logic to delete the order
    const row = button.parentElement.parentElement; // Get the row
    row.remove(); // Remove the row from the table
    alert('Order deleted.');
    // Add your logic to delete the order from the database
}