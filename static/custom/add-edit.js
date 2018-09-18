

/*
Add elements
*/

function add_indegrient() {
	let len = parseInt($("#ingredients input").length);
	$("#ingredients").append(`
					<li class="list-group">
						<div class="add-remove-element">
							<button onclick="add_indegrient()" class="add-element btn btn-success" type="button"><i class="fas fa-plus"></i></button>
							<button onclick="remove_indegrient(this)" class="add-element btn btn-danger" type="button"><i class="fas fa-trash-alt"></i></button>
						</div>						
						<input name="ingredient-${len + 1}" value="" type="text" class="col-8 form-control"
						 placeholder="2 cups all purpose flour" minlength="5" maxlength="30" required>						
					</li>
		`);
}
function add_dishType() {
	let name = $("input[name='new_dish_type']").val();
	if (name != "") {
		let check_box = $(".dish-type input");
		let len = parseInt($(".dish-type input").length);

		for (let i = 0; i < check_box.length; i++) {
			if (check_box[i].value.toLowerCase() == name.toLowerCase()) {
				$(check_box[i]).prop("checked", true);
				return;
			}
		}
		$("#dish-type-append").append(`
				<div class="form-check">
					<input class="form-check-input" name="dishTypes-0${len + 1}" type="checkbox" value="${name}">
					<label class="form-check-label" for="dishTypes-0${len + 1}" checked>
						${name}
					</label>
				</div>
		`);
	}
	
}

function add_cuisine() {
	let name = $("input[name='new_cusine_type']").val();
	if (name != "") {
		let check_box = $("#cuisine input");
		let len = parseInt($("#cuisine input").length);
		for (let i = 0; i < check_box.length; i++) {
			if (check_box[i].value.toLowerCase() == name.toLowerCase()) {
				$(check_box[i]).prop("checked", true);
				return;
			}
		}
		$("#cuisine").append(`
				<div class="form-check">
					<input class="form-check-input" name="dishTypes-0${len + 1}" type="checkbox" value="${name}">
					<label class="form-check-label" for="dishTypes-0${len + 1}" checked>
						${name}
					</label>
				</div>
		`);
	}
}

function add_diet() {
	let name = $("input[name='new_diet_type']").val();
	if (name != "") {
		let check_box = $("#diet input");
		let len = parseInt($("#diet input").length);
		for (let i = 0; i < check_box.length; i++) {
			if (check_box[i].value.toLowerCase() == name.toLowerCase()) {
				$(check_box[i]).prop("checked", true);
				return;
			}
		}
		$("#diet").append(`
				<div class="form-check">
					<input class="form-check-input" name="dishTypes-0${len +
						1}" type="checkbox" value="${name}">
					<label class="form-check-label" for="dishTypes-0${len + 1}" checked>
						${name}
					</label>
				</div>
		`);
	}
}


function add_step() {
	let len = parseInt($("#steps input").length);
	if (len == 10) {
		let message = "How many Ingredients do you need?";
		console.log(message)
	}
	if (len == 10) {
		let message = "Sometimes less is more";
		console.log(message);
	}
	$("#steps").append(`
					<li class="list-group">
						<div class="add-remove-element">
							<button onclick="add_step()" class="add-element btn btn-success" type="button"><i class="fas fa-plus"></i></button>
							<button onclick="remove_step(this)" class="add-element btn btn-danger" type="button"><i class="fas fa-trash-alt"></i></button>
						</div>
						<input name="step-${len + 1}" type="text" class="col-8 form-control" placeholder="In a medium bowl mix the sugar, yeast, and water" minlength="10" maxlength="60" required>
					</li>
	`);
}

/*
Remove elements
*/

function remove_indegrient(input) {
	let len = parseInt($("#ingredients input").length);
	if (len == 1) {
		console.log("YEs");
	} else {
		$(input)
			.parent()
			.parent()
			.remove();
	}
}

function remove_step(input) {
	let len = parseInt($("#steps input").length);
	if (len == 1) {
		console.log("YEs");
	} else {
		$(input)
			.parent()
			.parent()
			.remove();
	}
}

