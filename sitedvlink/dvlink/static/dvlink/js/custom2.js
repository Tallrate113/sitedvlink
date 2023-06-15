$(document).ready(function() {
    $('.btnred').click(function() {
        var row = $(this).closest('tr');
        var textElement = row.find('.editable-field');
        var newText = textElement.text();

        var postId = row.find('.btndel').data('post-id');
        var token = '77ab9b784178cb8f64ababc80dcb1104349597f9'; // Замените 'your_token' на фактический токен аутентификации

        $.ajax({
            url: '/api/v1/application/' + postId + '/',
            type: 'PATCH',
            data: {
                field_text_appeal: newText
            },
            beforeSend: function(xhr) {
                xhr.setRequestHeader('Authorization', 'Token ' + token);
            },
            success: function(response) {
                // Обработка успешного обновления записи
                console.log('Изменения сохранены');
            },
            error: function(xhr, status, error) {
                // Обработка ошибки обновления записи
                console.log('Ошибка при сохранении изменений:', error);
            }
        });
    });
});