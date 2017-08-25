/**
 * Created by yangyang on 8/9/17.
 */
var express = require('express');
var router = express.Router();
var rpc_client = require('../rpc_client/rpc_client');

// GET news summary list
router.get('/userId/:userId/pageNum/:pageNum', function (req, res, next) {
    console.log('Fetching News');
    userId = req.params['userId'];
    pageNum = req.params['pageNum'];

    rpc_client.getNewsSummariesForUser(userId, pageNum, function (response) {
        res.json(response);
        console.log(response)
    });
});

router.post('/userId/:userId/newsId/:newsId', function (req, res, next) {
    console.log('Logging news click ...')
    user_id = req.params['userId']
    news_id = req.params['newsId']

    rpc_client.logNewsClickForUser(user_id, news_id);
    res.status(200)
});

module.exports = router;

