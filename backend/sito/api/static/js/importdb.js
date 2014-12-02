var data = null;
var piani = null;

function prepareAula(aula, index) {
    if(aula.ultimo_aggiornamento != null){
        var formattedDate = new Date(aula.ultimo_aggiornamento);
        var h = formattedDate.getHours();
        var m = formattedDate.getMinutes();
        aula.ultimo_aggiornamento = (h + ":" + m);
    } else {
        aula.ultimo_aggiornamento = "More than 2h ago"
    }
    
    aula.posti_liberi = parseInt(aula.stat ? aula.stat.posti_liberi : "0");
    aula.immagine = nomeImmagine(index);
    aula.index = index;

    data[index] = aula;
}

function loaddata() {
    $.get("/api/aule?format=json", function(x) {
        data = x
        piani = [ [], [], [], [], [] ]

        for(var i = 0; i < data.length; i++) {
            prepareAula(data[i], i);
            piani[data[i].piano + 1].push(data[i]);
        }

        var html = "";
        for(var piano = 0; piano < piani.length; piano++) {
            if(piani[piano].length > 0)
                html = html.concat(tmpl("template_piano", { data: piani[piano] }));
        }

        $("#container").html(html);
    });
}

function nomeImmagine(index) {
    var aula = data[index];

    if(aula.stat == null) return "img/default.jpg";
    else {
        var posti_perc = aula.stat.posti_liberi / aula.dimensione;
        var ghetto = aula.stat.ghetto > 50 ? "ghetto" : "noghetto";
        var lesson = aula.stat.lesson ? "lesson" : "nolesson";
        var posti = aula.stat.posti_liberi < 40 ? "empty" : aula.stat.posti_liberi < 75 ? "medium" : "full";
        return "img/" + ghetto + "_" + lesson + "_" + posti + ".jpg";
    }
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
