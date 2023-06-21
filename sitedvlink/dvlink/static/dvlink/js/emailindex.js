$(document).ready(function() {
  $('#id_field_email').on('input', function(e) {
    var email = $(this).val();
    var emailRegex = /^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+(?:ru|com|net|org)$/;

    if (!emailRegex.test(email)) {
    }
  });
});