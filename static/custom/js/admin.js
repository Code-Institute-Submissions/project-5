$(document).ready(function () {
	$("#update-db").removeAttr("disabled")

	$("#update-db").on("click", function () {
		$("#update-db").attr("disabled", true).html("Updating");
		$.post(`/update-db`, function (data, status) {
			console.log(status);
			if (status == "success") {

				window.location.replace("/admin_dashboard");
			}

		}).fail(function (xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});

	});
});