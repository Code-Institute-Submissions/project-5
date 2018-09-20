/*
General
*/

$(document).ready(function () {
	$("#search-btn").on("click", function() {
		$(".search-overlay").slideToggle();
	});
});

/*
Alerts modal
*/

function alerts(message) {	
	$("#message").html(message)
	$("#alerts").slideDown(1500)
	setTimeout(() => {
		$("#alerts").slideUp(1500)		
	}, 4000);
}


/*
Print recipe
*/

function print_recipe(recipe) {
	$.post(`/recipe/${recipe}`, function (data) {
		print(data);
		return false;
	}).fail(function (xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
	return false;
}