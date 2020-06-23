import React, { Component } from 'react';
import France from "../departements/index";

export default class Geodata extends Component {

  render(){
    return(
      <>
        <h1>Geodata</h1>

        <France greenDepartements={[92, 89, 21, 33, 47, 74, "2a", 976]} orangeDepartements={[64, 34, "2b", 75]} redDepartements={[31]}/>
      </>
    )
  }
}