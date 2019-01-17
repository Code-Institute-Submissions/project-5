// Enable btns in search form for Safari as the evens will not trigger
(function () {
	let safari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
	if (safari) {
		$("#input_search_btn").removeAttr("disabled");
		$("#tags_search_btn").removeAttr("disabled");
	}
})();