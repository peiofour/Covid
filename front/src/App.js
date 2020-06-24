import React, {Component} from 'react';
import { Button } from 'react-bootstrap'
import './App.css';
import Geodata from './components/Geodata'
import MLChatbot from './components/MLChatbot'


export default class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      display: 0
    };
  }

  ShowProject(props){
    if(props.disp === 1){
      return <Geodata/>
    }
    else if(props.disp === 2){
      return <MLChatbot />
    }
    else{
      return <div></div>
    }
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <p>
            Choisissez le projet ci-dessous :
          </p>
        </header>
        <div className="App-body">
          <Button onClick={() => this.setState({display: 1})} 
          variant="primary" className="App-button">
            GeoData
          </Button>
          <Button onClick={() => this.setState({display: 2})} 
          variant="primary" className="App-button">
            Chatbot
          </Button>
        </div>
        <this.ShowProject disp={this.state.display} />
      </div>
    );
  }
}
