/**
 * Created by yangyang on 8/14/17.
 */
// invoke 'add'
client.add(1, 2, function(response) {
    console.assert(response == 3)
});

// invoke "getNewsSummariesForUser"
client.getNewsSummariesForUser('test_user', 1, function(response) {
    console.assert(response != null);
});

// invoke "logNewsClickForUser"
client.logNewsClickForUser('test_user', 'test_news');
