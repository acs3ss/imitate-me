// var mediaConstraints = {
//     audio: true,
//     video: true
// };
//
// navigator.getUserMedia(mediaConstraints, onMediaSuccess, onMediaError);
//
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
//
// function onMediaError(e) {
//     console.error('media error', e);
// }

export var array = [1, 2, 3, 4];

// const stitch = require("mongodb-stitch");
// clientPromise.then(client => {
//   const db = client.service('mongodb', 'mongodb-atlas').db('imitate');
//   client.login().then(() =>
//     db.collection('recordings').insertOne(array);
//   ).then(()=>
//     db.collection('recordings').find({owner_id: client.authedId()}).limit(100).execute()
//   ).then(docs => {
//     console.log("Found docs", docs)
//     console.log("[MongoDB Stitch] Connected to Stitch")
//   }).catch(err => {
//     console.error(err)
//   });
// });
