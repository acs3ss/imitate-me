// var mediaConstraints = {
//     audio: !!navigator.mozGetUserMedia, // don't forget audio!
//     video: true                         // don't forget video!
// };

// navigator.getUserMedia(mediaConstraints, onMediaSuccess, onMediaError);

// function onMediaSuccess(stream) {
//     var mediaRecorder = new MediaStreamRecorder(stream);
//     mediaRecorder.mimeType = 'video/webm';
//     mediaRecorder.ondataavailable = function (blob) {
//         // POST/PUT "Blob" using FormData/XHR2
//         var blobURL = URL.createObjectURL(blob);
//         document.write('<a href="' + blobURL + '">' + blobURL + '</a>');
//     };
//     mediaRecorder.start(3000);
// }

// function onMediaError(e) {
//     console.error('media error', e);
// }
