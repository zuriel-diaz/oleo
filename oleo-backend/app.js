var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
//var users = require('./routes/users');

var challenges = require('./modules/challenges');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
//app.use('/users', users);
app.get('/v1/challenges',function(req,res){
  res.setHeader('content-type','application/json');
  /*
  var data = {
    "challenge_identifier":2,
    "description":"Can you tell us more about X and Y?",
    "solution":"b"
  };
  */
  //res.end(JSON.stringify(data));
  res.end(JSON.stringify(challenges.list()));
});
app.post('/v1/challenges',function(req,res){
  //console.log('challenge_identifier->'+JSON.stringify(req.body));
  res.setHeader('content-type','application/json');
  if(req.body.id & req.body.content){
    var challenges = challenges.list();
    console.log(typeof challenges);
  }
  var data = {'test':'test'};
  res.end(JSON.stringify(data));
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});


module.exports = app;
