/**
 * Created by yangyang on 8/9/17.
 */
import React from 'react';
import LoginForm from './LoginForm'


class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            errors: {},
            user: {
                email: '',
                password: '',
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
    }

    changeUser(event) {
        console.log(event.target.name)
        const field = event.target.name;
        const user = this.state.user;
        user[field] = event.target.value;

        this.setState({user:user});
    }

    render() {
        return (
            < LoginForm onSubmit={this.processForm} onChange={this.changeUser}
                        errors={this.state.errors} user={this.state.user} />
        )
    }

}

export default LoginPage;