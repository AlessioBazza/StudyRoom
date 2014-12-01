function loaddata() {
    $.get('/api/aule?format=json', function(x) {
        data = x
        $('.list-group').html(tmpl('template_aula', data));
            /* SLIDER_SCRIPT || START */
        $(".statSlider").ionRangeSlider({
            min: 0,
            max: 100,
            from: 0,
            postfix: "%",
            grid: true,
            hide_min_max: true,
        });
            /* SLIDER_SCRIPT || END */
    });
}

function submit_posti(aula_id) {
    posti = parseInt($('#report-' + aula_id).val());
    lesson = $('#lesson-' + aula_id).is(':checked');
    ghetto = $('#ghetto-' + aula_id).is(':checked');
     
        $.post('/api/posti', {
            posti_liberi: posti,
            user: 'io',
            aula: aula_id,
            chaos: ghetto,
            lesson: lesson,
        }, function(resp) {
            loaddata();
        });    
}

$(document).ready(function() {
    loaddata();
});