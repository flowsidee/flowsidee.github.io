let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = "#FFFFF";
tg.MainButton.color = "#2cab37";

let item = "";

let btn1 = document.getElementByID("btn_nigger");

btn1.addEventListener("click", function() {
	if (tg.MainButton.isVisible) {
		tg.MainButton.hide();
	}
	else {
		tg.MainButton.setText("Негр пашет круче всех");
		item = "nigger";
		tg.MainButton.show();
	}
});

tg.onEvent("mainButtonClicked", function(){
	tg.sendData(item);
});