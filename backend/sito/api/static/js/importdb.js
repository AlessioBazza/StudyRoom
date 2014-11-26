function loaddata() {
    $.get('/api/aule?format=json',
          function(x) {
        data = x
        $('.list-group').html(tmpl('template_aula', data));
    });
}

function submit_posti(aula_id) {
    posti = parseInt($('#report-' + aula_id).val());

    if(isNaN(posti)) {
        alert('Inserisci un numero intero!');
    }
    else {
        $.post('/api/posti', {
            posti_liberi: posti,
            user: 'io',
            aula: aula_id,
            chaos: posti > 50,
            lesson: false
        }, function(resp) {
            alert('posted');
            loaddata();
        });
    }
}

$(document).ready(function() {
    loaddata();
});