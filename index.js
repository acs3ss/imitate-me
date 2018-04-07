var Myo = require('myo');

Myo.connect('com.stolksdorf.myAwesomeApp', require('ws'));


Myo.on('imu', function(data) {
	var array = [];
	console.log(data);
});