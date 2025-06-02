const express = require("express");

const appFlag = express();
const portFlag = 1337;

appFlag.use((req, res) => {
	res.send(process.env.FLAG);
});

module.exports = {
	appFlag,
	portFlag
};