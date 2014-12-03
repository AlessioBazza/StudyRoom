var data = null;
var sezioni = null;

function prepareAula(aula, index) {
    if(aula.ultimo_aggiornamento != null){
        var formattedDate = new Date(aula.ultimo_aggiornamento);
        var h = formattedDate.getHours();
        var m = formattedDate.getMinutes();
        aula.ultimo_aggiornamento = ((h < 10 ? '0' + h : h) + ":" + (m < 10 ? '0' + m : m));
    } else aula.ultimo_aggiornamento = "More than 2h ago"
    
    aula.sezione = aula.locazione + ' - Piano ' + aula.piano.toString();
    aula.posti_liberi = parseInt(aula.stat ? aula.stat.posti_liberi : "0");
    aula.index = index;

    if(aula.stat == null) aula.immagine = "img/default.jpg";
    else {
        var posti_perc = aula.stat.posti_liberi / aula.dimensione;
        var ghetto = aula.stat.ghetto > 50 ? "ghetto" : "noghetto";
        var lesson = aula.stat.lesson ? "lesson" : "nolesson";
        var posti = aula.stat.posti_liberi < 40 ? "empty" : (
            aula.stat.posti_liberi < 75 ? "medium" : "full");

        aula.immagine = "img/" + ghetto + "_" + lesson + "_" + posti + ".jpg";
    }

    data[index] = aula;
}

function loaddata() {
    $.get("/api/aule?format=json", function(x) {
        data = x
        sezioni = { }

        for(var i = 0; i < data.length; i++) {
            prepareAula(data[i], i);
            if(!sezioni[data[i].sezione])
                sezioni[data[i].sezione] = []

            sezioni[data[i].sezione].push(data[i]);
        }

        var html = "";
        for(var sezione in sezioni) {
            html = html.concat(tmpl("template_piano", { data:sezioni[sezione] }));
        }

        $("#container").html(html);
    });
}

function renderAula(index, show) {
    var aula = data[index];

    $("#containerItem-" + index).html(tmpl("template_containerItem", { aula: aula, index: index }));

    if(show) {
        $(".statContainer").hide().html("");
        $("#statContainer-" + index).html(tmpl("template_statContainer", { aula: aula, index: index })).show();
        $( "#statSlider-" + index ).slider({
            value: 1,
            min: 0,
            max: 100,
            step: 1,
            slide: function( event, ui ) {
                $( "#amount-" + index ).val( ui.value + "%");
            }
        });
    }
}

function updateAula(index) {
    var aula = data[index];

    $.get("/api/aule/" + aula.id + "?format=json", function(update) {
        delete update.posti_set;
        prepareAula(update, index);
        renderAula(index, false);
    });
}

function submit_posti(index) {
    var aula = data[index];

    posti = parseInt($("#amount-" + index).val());
    lesson = $("#lesson-" + index).is(":checked");
    ghetto = $("#ghetto-" + index).is(":checked");

    $.post("/api/posti", {
        posti_liberi: posti,
        user: "io",
        aula: aula.id,
        chaos: ghetto,
        lesson: lesson,
    }, function(resp) {
        updateAula(index);
    });
}

$(document).ready(function() {
    loaddata();
});
