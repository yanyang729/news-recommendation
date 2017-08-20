/**
 * Created by yangyang on 8/19/17.
 */
import React from 'react';
import Auth from '../Auth/Auth';
import Login from '../Login/LoginPage';
import Signup from '../SignUpPage/SignUpPage';
import {
    BrowserRouter as Router,
    Route,
    Link
} from 'react-router-dom'
import './Base.css';
import App from '../App/App';


const Base = () => (
    <Router>
        <div>
        <nav>
            <div className="nav-wrapper">
                <a href="/" className="brand-logo">News</a>
                <ul id="nav-mobile" className="right hide-on-med-and-down">
                    {
                        Auth.isAuthenticated() ?
                            (
                                <div>
                                    <li>{Auth.getEmial()}</li>
                                    <li><Link to="/logout">Log out</Link></li>
                                </div>
                            ) : (
                                <div>
                                    <li><Link to="/login">Log in</Link></li>
                                    <li><Link to="/signup">Sign up</Link></li>
                                </div>
                            )
                    }
                </ul>
            </div>
        </nav>
        <br/>


        <Route exact path="/" component={App} />
        <Route path="/login" component={Login} />
        <Route path="/signup" component={Signup} />
        </div>
    </Router>
);


export default Base;