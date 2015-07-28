$(document).ready(function() {
    var mantenimiento= document.getElementById("mantenimiento").value;
    var maquina=document.getElementById("maquina").value;
    var color=document.getElementById("color").value;
    $('#external-events .fc-event').each(function() {

			// store data so the calendar knows to render an event upon drop
			$(this).data('event', {
				title: $.trim($(this).text()), // use the element's text as the event title
				stick: true // maintain when user navigates (see docs on the renderEvent method)
			});

			// make the event draggable using jQuery UI
			$(this).draggable({
				zIndex: 999,
				revert: true,      // will cause the event to go back to its
				revertDuration: 0  //  original position after the drag
			});
		});

    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,basicWeek,basicDay'
        },
        eventColor:color,
        selectable: true,
        lang: 'es',
        editable: true,
        events: '/tipo/api/event/'+mantenimiento+"/"+maquina,
        eventLimit: true, // allow "more" link when too many events
        droppable: true,
        dragRevertDuration: 0,
        eventDragStop: function( event, jsEvent, ui, view ) {
                if(isEventOverDiv(jsEvent.clientX, jsEvent.clientY)) {
                    $('#calendar').fullCalendar('removeEvents', event._id);
                    var el = $( "<div class='fc-event'>" ).appendTo( '#external-events-listing' ).text( event.title );
                    el.draggable({
                      zIndex: 999,
                      revert: true,
                      revertDuration: 0
                    });
                    el.data('event', { title: event.title, id :event.id, stick: true });
                    deleteData(event);
                }
        },
        eventDrop: function (event, dayDelta, minuteDelta) {
            if(event.end == null){
                event.end = event.start;
            }
            updateData(event);
        },
        eventResize: function (event, dayDelta, minuteDelta) {
            updateData(event);
        },
        eventReceive: function(event) {
            postData(event);
        },
        eventRender: function(event,element){
            element.find('.fc-title').before('<i class="icon-lg fa fa-'+event.icono+'"'+'></i> ');
        }
    });

    function postData(event,element) {
        var csrftoken = getCookie('csrftoken');
        if(mantenimiento==1){
            var icono = "calendar-o";
        }
        if(mantenimiento==2){
            var icono = "fire";
        }
        if(mantenimiento==3){
            var icono = "magic";
        }
        if(mantenimiento==4){
            var icono = "bar-chart";
        }
        if(mantenimiento==5){
            var icono = "wrench";
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/tipo/api/event/"+mantenimiento+"/"+maquina+"/",
            data: {"title":event.title,"start":event.start.format(),"end":event.end,"color":color,"icono":icono,"mantenimiento":mantenimiento,"maquina":maquina},
            type: 'POST',
            success: function(json){
                event.id = json.id;
                $("#calendar").fullCalendar('renderEvent',event);
            }
        });
    }

    function updateData(event) {
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/tipo/api/event/"+ event.id +"/"+mantenimiento+"/"+maquina+"/",
            data: {"title":event.title,"start":event.start.format(),"end":event.end.format(),"mantenimiento":mantenimiento,"maquina":maquina},
            type: 'PUT',
        });
    }


    function deleteData(event) {
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            url: "/tipo/api/event/"+event.id+"/"+mantenimiento+"/"+maquina+"/",
            type: 'DELETE',
        });
    }

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



    var isEventOverDiv = function(x, y) {

            var external_events = $( '#external-events' );
            var offset = external_events.offset();
            offset.right = external_events.width() + offset.left;
            offset.bottom = external_events.height() + offset.top;

            // Compare
            if (x >= offset.left
                && y >= offset.top
                && x <= offset.right
                && y <= offset .bottom) { return true; }
            return false;

        }

});