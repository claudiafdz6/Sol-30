

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('addButton').addEventListener('click', function () {
        document.getElementById('addModal').style.display = 'none';
    });

    document.getElementById('addTicketButton').addEventListener('click', function () {
        document.getElementById('addModal').style.display = 'block';
    });
});