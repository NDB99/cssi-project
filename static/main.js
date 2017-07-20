function setupEverything()
{
	var dino = $('#dino');
	dino.on('click', Animate);                             
                             
	var dino = $('#dino');                             
	dino.on('click', Background);                             
                             
	var dino = $('#dino');                             
	dino.on('dblclick', Calm);                             
                             
}                             
                             
function Animate()                             
{                             
	var dino = $('#dino')                             
	dino.animate(                             
		{                             
			'width': '200px'                             
		},                             
	1200                             
	);                             
	dino.animate(                             
		{                             
			'width': '50px'                             
		},                             
	1200                             
	);                             
}                             
                             
function Background()                             
{                             
	var dino = $('#dino')                             
	$('#html').css('background-image','url(/resources/color.png)');                             
                             
}                             
                             
function Calm()                             
{                             
	var dino = $('#dino')                             
	$('#html').css('background-image','url(/resources/calm.jpg)');
}


$(document).ready(setupEverything);