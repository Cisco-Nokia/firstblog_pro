$(document).ready(function () {
    $('#awesome').click(function () {
        var aid;
        aid = $(this).attr('arti_id');
        $.get('/awesome_click/', {article_id: aid}, function (data) {
            $('#awesome_count').html(data);
            $('#awesome').hide();
        })
    })
})