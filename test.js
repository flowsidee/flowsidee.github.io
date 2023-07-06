let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = "#FFFFF";
tg.MainButton.color = "#2cab37";

let item = "";

let btn_nigger = document.getElementByID("btn_nigger");

btn_nigger.addEventListener("click", function() {
	if (tg.MainButton.isVisible) {
		tg.MainButton.hide();
	}
	else {
		tg.MainButton.setText("Негр пашет круче всех");
		item = "nigger";
		tg.MainButton.show();
	}
})