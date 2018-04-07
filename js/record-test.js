var Myo = require('myo');

Myo.connect('com.stolksdorf.myAwesomeApp', require('ws'));

var array = [];
var recording = false;

function startRecord(elmnt,clr) {
		this.vibrate();
		recording = true;
		console.log("Started recording");
		while(recording) {
			Myo.on('imu', function(data) {
				array.push(data);
			});
		}
}

function stopRecord(elmnt,clr) {
		recording = false;
		console.log(array);
}
