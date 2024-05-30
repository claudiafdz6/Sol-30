
document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('addTicketButton').addEventListener('click', function () {
        document.getElementById('addModalButton').style.display = 'block';
    });

    document.getElementById('closeButton').addEventListener('click', function () {
        document.getElementById('addModalButton').style.display = 'none';
    });
});
