function showTime() {
	document.getElementById("currentTime").innerHTML = new Date().toLocaleString('id-ID', { timeZone: 'Asia/Jakarta' });
}
showTime();
setInterval(function () {
	showTime();
}, 1000);
