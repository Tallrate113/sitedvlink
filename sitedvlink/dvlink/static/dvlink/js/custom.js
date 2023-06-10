$(document).ready(function() {
        $(".btndel").click(function(){
            var el = $(this), image_id =  $(this).data('image-id');
            $.ajax({
                type: "PATCH",
                dataType: "json",
                data: { "approved": "True"},
                url: "/ml/api/image/" + image_id + "/?format=json",
                success: function(data){
                    el.remove();
                }
            });
        });
    });
