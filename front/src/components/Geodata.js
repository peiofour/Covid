import React, { Component } from 'react';
import France from "../departements/index";

export default class Geodata extends Component {

  render(){
    return(
      <>
        <h1>Geodata</h1>

        <France departements={[92, 89, 21, 33, 47, 74, "2a", 976]} depOrange={[64, 75]}/>
      </>
    )
  }
}