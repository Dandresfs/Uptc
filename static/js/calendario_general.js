$(document).ready(function() {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        selectable: true,
        lang: 'es',
        editable: false,
        events: '/tipo/api/event/all/',
        eventLimit: true, // allow "more" link when too many events
        droppable: true,
        dragRevertDuration: 0,
        eventRender: function(event,element){
            element.find('.fc-title').before('<i class="icon-lg fa fa-'+event.icono+'"'+'></i> ');
        },
        eventClick: function(event){
            $("#titulo").html('<h2 id="titulo">'+event.title+'</h2>');

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            $.ajax({
                url: "/tipo/api/event/actividad/"+event.title+"/",
                type: 'GET',
                success: function(json){
                    if(json[0] != null){
                        $("#descripcion").html('<p id="descripcion">'+json[0].descripcion+'</p>');
                        $("#imagen").attr('src',json[0].imagen);
                    }
                    else{
                        $("#descripcion").html('<p id="descripcion">'+'No se encontro descripcion'+'</p>');
                        $("#imagen").attr('src','/');
                    }
                }
            });
        }

    });
        function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }


});