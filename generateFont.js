var EXPORT_DATA_FOLDER = "jitendex/data/HanaMinA";
var fs = require("fs");
var output = Object.create(null);
let files = fs.readdirSync(EXPORT_DATA_FOLDER);
files.forEach((file) => {
  if (file === "LICENSE") {
    output[file] = fs.readFileSync(`${EXPORT_DATA_FOLDER}/${file}`, "utf8");
    //.toString('base64')
  } else {
    output[file] =
      `data:image/svg+xml;base64,${Buffer.from(fs.readFileSync(`${EXPORT_DATA_FOLDER}/${file}`, "utf8")).toString("base64")}`;
  }
});
console.log(JSON.stringify(output));
