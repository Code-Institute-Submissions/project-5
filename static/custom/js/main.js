/*
Event handlers and ducument ready functions
*/

$(document).ready(function () {
	if ($(window).width() >= 1400) {
		$("#search-form-toggle").html(`
			<button type="button" id="search-btn" class="btn btn-outline-info">
				<i class="fas fa-search"></i>
			</button>
		`);
		
	}
	$("#search-btn").on("click", function () {
		$(".search-overlay").slideToggle();
	});
	flashed_messages();
});


/*
Alerts modal
*/

function alerts(message) {
	$("#messages").html(`<p>${message}</p>`);
	$("#alerts").slideDown(1500);
	setTimeout(() => {
		$("#alerts").slideUp(1500);
	}, 4000);
}

function flashed_messages() {
	let messages = parseInt($("#messages p").length);
	if (messages) {
		$("#alerts").slideDown(1500);
		setTimeout(() => {
			$("#alerts").slideUp(1500);
		}, 7000);
	}
}

/*
Print recipe
*/

function print_recipe(recipe) {
	$.post(`/recipe/${recipe}`, function(data) {
		print(data);
		return false;
	}).fail(function(xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
	return false;
}

/* 
Search form recipes count on filter selection
*/

$(".search-overlay input[type=checkbox]").change(function() {
	return checked_checkboxes();
});

function tags_search() {
	$("#tags_search_btn")
		.attr("disabled", "disabled")
		.html("Working ...");
	$("#input_search_btn")
		.attr("disabled", "disabled")
		.html("Working ...");
	$("#search-form").attr("action", "/tags_form_search?limit=12&offset=0");
	$("#search-form").submit();
}

function input_search() {
	$("#input_search_btn")
		.attr("disabled", "disabled")
		.html("Working ...");
	$("#tags_search_btn")
		.attr("disabled", "disabled")
		.html("Working ...");
	let input = $(".search-overlay input[name=search_input]").val();
	$("#search-form").attr("action", `/input_form_search?input=${input}&limit=12&offset=0`);
	$("#search-form").submit();
}

function checked_checkboxes() {
	let checked = $(".form-check-input:checkbox:checked");
	if (checked.length == 0) {	
		$("#num_of_results").html("");	
		$("#tags_search_btn")
			.attr("disabled", "disabled")
			.html("Select a tag!");
		return false;
	}
	let checkboxes = {};
	for (let i = 0; i < checked.length; i++) {
		checkboxes[checked[i].name] = checked[i].value;
	}
	checkboxes.limit = $(".search-overlay input[name=limit]").val();
	checkboxes.search_input = $(
		".search-overlay input[name=search_input]"
	).val();
	checkboxes.search_by = $(".search-overlay input[name=search_by]").val();
	$.post("/num_of_tags_results", checkboxes, function(data, status) {
		if (data != 0) {
			$("#num_of_results").html(`
					Found <span class="text-success">${data}</span> recipe/s`);
			$("#tags_search_btn")
				.removeAttr("disabled")
				.html("Search tags!");
		} else {
			$("#num_of_results").html(`
					Found <span class="text-danger">${data}</span> recipes <br>
					Please consider to remove some of the filters!`);
			$("#tags_search_btn")
				.attr("disabled", "disabled")
				.html("No recipes");
		}
	}).fail(function(xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
	return false;
}

/* 
Search Form
*/

$(".search-overlay input[name=search_input]").on("input", function() {
	let input = $(".search-overlay input[name=search_input]").val();
	if (input.length >= 3 && input.trim() != "") {
		$("#input_search_btn")
			.prop("disabled", false)
			.html("Search!");

		let form = {
			search_input: $(".search-overlay input[name=search_input]").val(),
			limit: $(".search-overlay input[name=limit]").val()
		};
		$.post("/num_of_input_results", form, function(data, status) {
			if (data == 0) {
				$("#input-search-messages").html("Sorry did not find any recipes!");
				$("#input_search_btn")
					.prop("disabled", true)
					.html("By?");
				$("#tags_search_btn")
					.prop("disabled", false)
					.html("Search tags!");
			} else {
				$("#input-search-messages").html(`
						Found ${data} recipes ...`);
			}
		}).fail(function(xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
		return false;
	} else {
		$("#input_search_btn")
			.prop("disabled", true)
			.html("By?");
	}
});

