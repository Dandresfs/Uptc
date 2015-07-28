$(document).ready(function(){

	var fecha = new Date();
	var year = fecha.getFullYear();
	var month = fecha.getMonth();
	var day = fecha.getDate();
	var meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


	if ($( window ).width() <= 500 ){
		$("#facebook").removeClass("fa-5x").addClass("fa-2x");
		$("#twitter").removeClass("fa-5x").addClass("fa-2x");
		$("#github").removeClass("fa-5x").addClass("fa-2x");
	}



	$("#fecha").html("13 de Enero del 2014 a "+day+" de "+meses[month]+" del "+year);

	$("#perfil").click(function(){
		$('html, body').animate({
        scrollTop: $(".separator--color-2").offset().top
    }, 1000);
	});	

	$("#educacion").click(function(){
		$('html, body').animate({
        scrollTop: $(".separator--color-1").offset().top
    }, 1000);
	});

	$("#cualidades").click(function(){
		$('html, body').animate({
        scrollTop: $(".separator--color-3").offset().top
    }, 1000);
	});

	$("#experiencia").click(function(){
		$('html, body').animate({
        scrollTop: $(".separator--color-4").offset().top
    }, 1000);
	});

	$("#contacto").click(function(){
		$('html, body').animate({
        scrollTop: $(".separator--color-5").offset().top
    }, 1000);
	});

	$(".html5").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 80,
		showText: true,
		lineWidth: 20
	});

	$(".css3").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 87,
		showText: true,
		lineWidth: 20
	});

	$(".javascript").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 75,
		showText: true,
		lineWidth: 20
	});

	$(".githubloader").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 94,
		showText: true,
		lineWidth: 20
	});

	$(".python").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 88,
		showText: true,
		lineWidth: 20
	});

	$(".c").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 67,
		showText: true,
		lineWidth: 20
	});

	$(".java").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 56,
		showText: true,
		lineWidth: 20
	});

	$(".sql").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 60,
		showText: true,
		lineWidth: 20
	});

	$(".ruby").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 35,
		showText: true,
		lineWidth: 20
	});

	$(".php").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 30,
		showText: true,
		lineWidth: 20
	});

	$(".django").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 91,
		showText: true,
		lineWidth: 20
	});

	$(".net").ClassyLoader({
		diameter:80,
		fontSize:'16px',
		fontColor: 'rgba(0,0,0,0.7)',
		lineColor: '#00A858',
		percentage: 27,
		showText: true,
		lineWidth: 20
	});
});