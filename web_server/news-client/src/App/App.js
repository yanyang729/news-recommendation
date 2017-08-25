/**
 * Created by yangyang on 8/9/17.
 */
import React from 'react';
import logo from './logo.png';
import './App.css';
import NewsPanel from '../NewsPanel/NewPanel';

class App extends React.Component {
    render() {
        return (
            <div>
                {/*<img className='logo' src={logo} alt='logo'/>*/}
                <div className='container'>
                    <NewsPanel />
                </div>
            </div>
        );
    }
}

export default App;