var main = function(){
    $('.stat').hide();
    $('.containerItem').click(function(){
        $('.stat').hide();
        $(this).children('.stat').show();
    }); 
};

$(document).ready(main);