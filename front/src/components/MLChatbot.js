import React, { Component } from 'react';
import Chatbot, { Loading } from 'react-simple-chatbot';

export default class MLChatbot extends Component {

  constructor(props){
    super(props);
    this.state = {
      loading: true,
      result: "",
      trigger: false
    }
  }

  render(){
    return(
      <div style={{display: "inline-block"}}>
        <h1>Chatbot</h1>
        <Chatbot 
          steps={[
            {
              id:'1',
              message:'Hello world',
              end: true
            }
          ]}
        />
      </div>
    )
  }
}

