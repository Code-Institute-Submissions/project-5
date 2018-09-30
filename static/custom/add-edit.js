

/*
Add elements
*/

function add_indegrient(btn) {
	let btn_parent = $(btn).parent().parent()
	let len = parseInt($("#ingredients input").length);
	if (len == 10) {
		let message = "How many Ingredients do you need?";
		alerts(message);
	}
	if (len == 15) {
		let message = "Sometimes less is more";
		alerts(message);
	}
	$(`
		<li class="list-group">
			<div class="add-remove-element">
				<button onclick="add_indegrient(this)" class="add-element btn btn-success" type="button"><i class="fas fa-plus"></i></button>
				<button onclick="remove_indegrient(this)" class="add-element btn btn-danger" type="button"><i class="fas fa-trash-alt"></i></button>
			</div>
			<input name="ingredient-${len + 1}" value="" type="text" class="col-8 form-control"
			placeholder="2 cups all purpose flour" minlength="5" maxlength="30" required>	
		</li>
	`).insertAfter(btn_parent);
}


function add_type(input, type) {
	let name = $(`input[name=${input}]`).val();
	if (name.length < 5 || name.length > 15) {
		let message = "Please enter name between 5 and 15 characters"
		alerts(message)
		return
	} 
	if (name != "") {
		let check_box = $(`#${type} input`);
		let len = parseInt($(`#${type} input`).length);
		for (let i = 0; i < check_box.length; i++) {
			if (check_box[i].value.toLowerCase() == name.toLowerCase()) {
				$(check_box[i]).prop("checked", true);
				let message = "Type already exist and has been checked for you.";
				alerts(message);
				return;
			}
		}
		$(`#${type}`).append(`
				<div class="form-check">
					<input class="form-check-input" name="${type}-0${len + 1}" type="checkbox" value="${name}" checked>
					<label class="form-check-label" for="${type}-0${len + 1}" checked>
						${name}
					</label>
				</div>
		`);
		let message = "New type created and checked for you.";
		alerts(message);
	} 
}

function add_dishType() {
	let name = $("input[name='new_dish_type']").val();
	if (name.length < 5 || name.length > 15) {
		let message = "Please enter name between 5 and 15 characters"
		alerts(message)
		return
	}
	if (name != "") {
		let check_box = $(".dish-type input");
		for (let i = 0; i < check_box.length; i++) {
			if (check_box[i].value.toLowerCase() == name.toLowerCase()) {
				$(check_box[i]).prop("checked", true);
				let message = "Type already exist and has been checked for you.";
				alerts(message);
				return;
			}
		}

		let len = parseInt($(".dish-type input").length);
		$("#dishType").append(`
				<div class="form-check">
					<input class="form-check-input" name="dishTypes-0${len + 1}" type="checkbox" value="${name}" checked>
					<label class="form-check-label" for="dishTypes-0${len + 1}" checked>
						${name}
					</label>
				</div>
		`);	
		let message = "New type created and checked for you.";
		name.value = ""
		alerts(message);	
	}

}

function add_step(btn) {
	let btn_parent = $(btn).parent().parent()
	let len = parseInt($("#steps input").length);
	$(`
	<li class="list-group">
		<div class="add-remove-element">
			<button onclick="add_step(this)" class="add-element btn btn-success" type="button"><i class="fas fa-plus"></i></button>
			<button onclick="remove_step(this)" class="add-element btn btn-danger" type="button"><i class="fas fa-trash-alt"></i></button>
		</div>
		<input name="step-${len + 1}" type="text" class="col-8 col-lg-10 form-control" placeholder="In a medium bowl mix the sugar, yeast, and water" minlength="10" maxlength="150" required>
	</li>
	`).insertAfter(btn_parent);
	
}

/*
Remove elements
*/

function remove_indegrient(input) {
	let len = parseInt($("#ingredients input").length);
	if (len == 1) {
		let message = "Please include at least one recipe indegrient";
		alerts(message);
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
		let message = "Please include at least one cooking step"
		alerts(message);
	} else {
		$(input)
			.parent()
			.parent()
			.remove();
	}
}


/*
Others
*/

// Characters left counter

function characters_counter(textarea, counter, maxlimit) {
	let countfield = document.getElementById(counter);
	if (textarea.value.length > maxlimit) {		
		textarea.value = textarea.value.substring(0, maxlimit);
		return false;
	} else {
		countfield.style.color = "#000000";
		countfield.value = `Remaining: ${maxlimit - textarea.value.length}`;
	}
}