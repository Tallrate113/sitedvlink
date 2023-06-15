$('#account-icon').on('click', function(event) {
    if (!checkAuthenticated()) {
        event.preventDefault();
        window.location.href = '/signin/';
    }
});