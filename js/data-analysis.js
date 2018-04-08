function processData(data) {
  console.log('linking successful ' + typeof(data));
  d3.json('../data/data.json', function(data) {
  console.log(data[0]);
  });
}
