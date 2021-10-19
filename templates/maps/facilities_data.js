const athleticFacilities = require("./athletic facilities.json");

const facilitiesArr = athleticFacilities.features;

const athleticObj = {};
facilitiesArr.map(
  (element) => (athleticObj[element.properties.objectid] = element.properties)
);

return athleticObj;