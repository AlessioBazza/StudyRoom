function loaddata() {
    $.get('/api/aule?format=json', function(x) {
        data = x
        $('.list-group').html(tmpl('template_aula', data));
        
        $(".statSlider").ionRangeSlider({
            hide_min_max: true,
            keyboard: true,
            min: 0,
            max: 100,
            step: 1,
            prefix: "%",
            grid: true
        });
        
    });
}

function submit_posti(aula_id) {
    posti = parseInt($('#report-' + aula_id).val());

     
        $.post('/api/posti', {
            posti_liberi: posti,
            user: 'io',
            aula: aula_id,
            chaos: false,
            lesson: false
        }, function(resp) {
            loaddata();
        });
}

$(document).ready(function() {
    loaddata();
});