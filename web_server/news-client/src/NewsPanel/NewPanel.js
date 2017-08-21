/**
 * Created by yangyang on 8/9/17.
 */
import './NewPanel.css';
import React from 'react';
import NewsCard from '../NewsCard/NewsCard'
import _ from 'lodash';
import Auth from '../Auth/Auth';

class NewsPanel extends React.Component {
    constructor(){
        super();
        this.state = {news: null};
        this.handleScroll = this.handleScroll.bind(this);
    }

    componentDidMount() {
        this.loadMoreNews();
        this.loadMoreNews = _.debounce(this.loadMoreNews,1000);
        window.addEventListener('scroll', this.handleScroll)

    }

    handleScroll() {
        let scrollY =  window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
        if ((window.innerHeight + scrollY) >= (document.body.offsetHeight - 50)) {
            console.log('loading more news');
            this.loadMoreNews();
        }

    }

    loadMoreNews() {
        let request = new Request('http://localhost:3000/news',{
            method:'GET',
            headers: {
              'Authorization': 'bearer ' + Auth.getToken(),
            },
            cache: false
        });

        fetch(request).then( res => res.json()).then( news => {
            this.setState({
                news: this.state.news ? this.state.news.concat(news) : news,
            })
        })

    }

    renderNews() {
        const new_list = this.state.news.map( news => {
            return (
                <a className="list-group-item" href="#">
                    <NewsCard news={news}/>
                </a>
            )
        });

        return(
            <div className="container-fluid">
                <div className="list-group"> {new_list} </div>
            </div>
        )
    }

    render() {
        if (this.state.news) {
            return (
                <div>
                    {this.renderNews()}
                </div>
            )
        } else {
            return (
                <div>
                    <div id="msg-app-loading">
                        Loading...
                    </div>
                </div>
            )
        }
    }
}

export default NewsPanel;