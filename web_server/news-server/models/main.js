/**
 * Created by yangyang on 8/20/17.
 */
const mongoose = require('mongoose');

module.exports.connect = (uri) => {
    mongoose.connect(uri, { useMongoClient: true,});

    mongoose.connection.on('error', (err) => {
        console.error(`Mongoose connection error: ${err}`);
        process.exit(1);
    });

    // load models
    require('./user');
};