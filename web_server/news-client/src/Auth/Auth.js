/**
 * Created by yangyang on 8/19/17.
 */
class Auth{
    /**
     * authenticate a user
     */
    static authenticateUser (token, email) {
        localStorage.setItem('token', token);
        localStorage.setItem('email', email);
    }

    /**
     * if authenticated
     */

    static isUserAuthenticated () {
        return localStorage.getItem('token') !== null ;
    }
    /**
     * log out
     */
    static deauthenticate () {
        localStorage.removeItem('token');
        localStorage.removeItem('email');
    }

    static getToken () {
        return localStorage.getItem('token')
    }

    static getEmial () {
        return localStorage.getItem('email')
    }

};

export default Auth