import React, {Component} from 'react';
import { Button } from 'react-bootstrap'
import './App.css';

export default class App extends Component {
  render(){
    return (
      <div className="App">
        <header className="App-header">
          <p>
            Choisissez le projet ci-dessous :
          </p>
        </header>
        <div className="App-body">
          <Button variant="primary" className="App-button">
            GeoData
          </Button>
          <Button variant="primary" className="App-button">
            Chatbot
          </Button>
        </div>
      </div>
    );
  }
}
