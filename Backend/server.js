const express = require("express");
const app = express();

app.get("/", (req, res) => {
  return res.status(200).send("<h1>Hello M8 </>");
});

app.listen(9999, (err, result) => {
  console.log("Server is running on port 9999");
});
