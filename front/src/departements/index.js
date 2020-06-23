import React from "react";
import PropTypes from "prop-types";
import { SvgLoader, SvgProxy } from "react-svgmt";

import Carte from "./Carte";
import { hasPetiteCouronne, normalizeDpt } from "./departements";

const France = ({ color, greenColor, orangeColor, redColor, greenDepartements, orangeDepartements, redDepartements }) => {
  const greenDep = [
    ...greenDepartements,
    ...(hasPetiteCouronne(greenDepartements) ? ["75-92-93-94"] : [])
  ];

  const orangeDep = [
    ...orangeDepartements,
    ...(hasPetiteCouronne(orangeDepartements) ? ["75-92-93-94"] : [])
  ]

  const redDep = [
    ...redDepartements,
    ...(hasPetiteCouronne(redDepartements) ? ["75-92-93-94"] : [])
  ]

  return (
    <SvgLoader svgXML={Carte}>
      <SvgProxy selector="#carte" fill={color} />
      {greenDep.map(dpt => (
        <SvgProxy
          key={dpt}
          selector={`#dpt-${normalizeDpt(dpt)}`}
          fill={greenColor}
        />
      ))}

      {orangeDep.map(dpt => (
        <SvgProxy
          key={dpt}
          selector={`#dpt-${normalizeDpt(dpt)}`}
          fill={orangeColor}
        />
      ))}

      {redDep.map(dpt => (
        <SvgProxy
          key={dpt}
          selector={`#dpt-${normalizeDpt(dpt)}`}
          fill={redColor}
        />
      ))}
    </SvgLoader>
  );
};

France.propTypes = {
  color: PropTypes.string,
  greenDepartements: PropTypes.array,
  orangeDepartements: PropTypes.array,
  redDepartements: PropTypes.array,
  greenColor: PropTypes.string,
  orangeColor: PropTypes.string,
  redColor: PropTypes.string
};

France.defaultProps = {
  color: "#74B4FF",
  greenColor: "#b3ff75",
  orangeColor: "#F09A3C",
  redColor: "#EB002A",
  greenDepartements: [],
  orangeDepartements: [],
  redDepartements: []
};

export default France;
