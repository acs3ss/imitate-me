var MongoClient = require('mongodb').MongoClient
  , co = require('co')
  , assert = require('assert');

// 1. Connect to MongoDB instance running on localhost

// Connection URL
var url = 'mongodb://localhost:27017/test';

co(function*() {
  const db = yield MongoClient.connect(url);
  console.log("Connected successfully to server");
  
  yield insertDocuments(db, null);
  yield findDocuments(db, null);
  yield indexCollection(db, null);
  yield aggregateDocuments(db, null);

  db.close();
}).catch(err => console.log(err));

// 2. Insert
var insertDocuments = function(db, callback) {
  return co(function*() {
    const results = yield db.collection('restaurants')
      .insertMany( [ 
          {"name":"Sun Bakery Trattoria", "stars":4, "categories":["Pizza","Pasta","Italian","Coffee","Sandwiches"]},
          {"name":"Blue Bagels Grill", "stars":3, "categories":["Bagels","Cookies","Sandwiches"]},
          {"name":"Hot Bakery Cafe","stars":4,"categories":["Bakery","Cafe","Coffee","Dessert"]},
          {"name":"XYZ Coffee Bar","stars":5,"categories":["Coffee","Cafe","Bakery","Chocolates"]},
          {"name":"456 Cookies Shop","stars":4,"categories":["Bakery","Cookies","Cake","Coffee"]}
]);
    console.log(results)
    return results;
  });
}

// 3. Query Collection
var findDocuments = function(db) {
  return co(function*() {
    // Get the documents collection
    const collection = db.collection('restaurants');
    const docs = yield collection.find({}).toArray();
    console.log("Found the following records");
    console.log(docs)
    return docs;
  });
}

// 4. Create Index
var indexCollection = function(db) {
  return co(function*() {
    const results = yield db.collection('restaurants').createIndex(
      { "name": 1 },
      null
    );

    console.log(results);
    return results;
  });
};

// 5. Perform Aggregation

var aggregateDocuments = function(db, callback) {
  return co(function*() {
    const results = yield db.collection('restaurants')
      .aggregate( 
        [ { '$match': { "categories": "Bakery" } },
          { '$group': { '_id': "$stars", 'count': { '$sum': 1 } } } ])
      .toArray();

    console.log(results)
    return results;
  });
}