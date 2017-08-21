var bodyParser = require('body-parser');
var express = require('express');
var path = require('path');
var cors = require('cors');
var config = require('./config/config.json');
var passport = require('passport');

var index = require('./routes/index');
var news = require('./routes/news');
var auth = require('./routes/auth');

var app = express();


require('./models/main').connect(config.mongoDbUri);

// var main = require('./models/main');
// main.connect(config.mongoDbUril);

// view engine
app.set('views', path.join(__dirname, '../news-client/build'));
app.set('view engine', 'jade');
app.use('/static', express.static(path.join(__dirname, '../news-client/build/static')));


// Load passport strategies
app.use(passport.initialize());
var localSignupStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignupStrategy);
passport.use('local-login', localLoginStrategy);



// TODO: remove this after development is done.
app.use(cors());

app.use(bodyParser.json());

app.use('/', index);
const authCheckMiddleware = require('./middleware/auth_checker');
app.use('/news', authCheckMiddleware);
app.use('/news', news);
app.use('/auth', auth);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  res.send('404 Not Found')
});


module.exports = app;
