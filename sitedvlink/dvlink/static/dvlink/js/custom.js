$(document).ready(function() {
    $('.btndel').click(function() {
        var postId = $(this).data('post-id');
        var token = '77ab9b784178cb8f64ababc80dcb1104349597f9';  // Замените 'your_token' на фактический токен аутентификации

        var $row = $(this).closest('tr');  // Сохраняем ссылку на текущую строку

        $.ajax({
            url: '/api/v1/application/' + postId + '/',
            type: 'DELETE',
            beforeSend: function(xhr) {
                xhr.setRequestHeader('Authorization', 'Token ' + token);
            },
            success: function(response) {
                // Обработка успешного удаления записи
                // Например, обновление списка заявок или других действий

                $row.remove();  // Удалить строку из таблицы после успешного удаления
                updateApplications();  // Обновить список заявок
            },
            error: function(xhr, status, error) {
                // Обработка ошибки удаления записи
                // Например, вывод сообщения об ошибке или других действий
            }
        });
    });

    function updateApplications() {
        // Код для обновления списка заявок
        // Например, выполнение нового AJAX-запроса для получения актуальных данных и их отображение на странице
    }
});