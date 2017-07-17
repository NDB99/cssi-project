function setupEverything()
{
	var circle = $('#circle');
	circle.on('click', Animate);
}

function Animate()
{
	var circle = $('#circle')
	circle.animate(
		{
			'marginTop': '200px'
		},
	200
	);
}

$(document).ready(setupEverything);