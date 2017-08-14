/**
 * Created by yangyang on 8/14/17.
 */
var client = require('./rpc_client');

client.add(1,2, function (response) {
    console.assert(response == 3)
})