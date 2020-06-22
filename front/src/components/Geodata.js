import React, { Component } from 'react';
import France from '@socialgouv/react-departements';


export default class Geodata extends Component {

  render(){
    return(
      <>
        <h1>Geodata</h1>

        <France/>
      </>
    )
  }
}