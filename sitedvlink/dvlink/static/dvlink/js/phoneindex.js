$(document).ready(function() {
  $('#id_field_number_phone').on('input', function(e) {
    var phone = $(this).val();
    phone = phone.replace(/[^0-9]/g, '');
    var formattedPhone = '+7 (' + phone.slice(1, 4) + ') ' + phone.slice(4, 7) + '-' + phone.slice(7, 9) + '-' + phone.slice(9, 11);
    $(this).val(formattedPhone);
  }).on('keydown', function(e) {
    if (e.keyCode === 8) {
    e.preventDefault();
      var phone = $(this).val();
      if (phone.length > 0) {
        phone = phone.slice(0, -1);
        $(this).val(phone);
      }
    }
  });
});