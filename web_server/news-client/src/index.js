/**
 * Created by yangyang on 8/9/17.
 */
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import { browserHistory, Router } from 'react-router';
import routes from './routes';
import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';


ReactDOM.render(
    <Router history={browserHistory} routes={routes} />,
    document.getElementById('root')
)