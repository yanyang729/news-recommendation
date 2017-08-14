/**
 * Created by yangyang on 8/9/17.
 */
/**
 * Created by yangyang on 8/9/17.
 */
import React from 'react';
import SignUpForm from './SignUpForm'

class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            errors: {},
            user: {
                email: '',
                password: '',
                confirm_password: '',
            }
        };

        this.processForm = this.processForm.bind(this);
        this.changeUser = this.changeUser.bind(this);

    }



    // pre-submission
    processForm(event) {
        event.preventDefault();

        const email = this.state.user.email;
        const password = this.state.user.password;
        const confirm_password = this.state.user.confirm_password;
    }

    changeUser(event) {
        const field = event.target.name;
        const user = this.state.user;
        if (field === 'password') {
            user[field] = event.target.value;
            user['confirm_password'] = event.target.value;
        } else {
            user[field] = event.target.value;
        }

        this.setState({user:user});

        if (this.state.user.password !== this.state.user.confirm_password) {
            const errors = this.state.errors;
            errors.password = "Password and Confirm Password don't match"
            this.setState({errors:errors})
        } else {
            const errors = this.state.errors;
            errors.password = '';
            this.setState({errors:errors});
        }
    }

    render() {
        return (
            < SignUpForm onSubmit={this.processForm} onChange={this.changeUser} errors={this.state.errors} user={this.state.user} />
        )
    }

}

export default LoginPage;