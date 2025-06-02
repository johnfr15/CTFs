const express = require("express");
const session = require("express-session");
const path = require("path");

const { appFlag, portFlag } = require("./flag-server");

const app = express();
const PORT = 3000;

const users = {};
const userNotes = {};

app.use((req, res, next) => {
	const adminKey = req.headers["x-admin-key"];
	
	if (!adminKey || adminKey !== process.env.ADMIN_KEY) {
		return res.status(403).json({ error: "Unauthorized access" });
	}
	next();
});

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));
app.use(session({
	secret: "super_simple_key",
	resave: false,
	saveUninitialized: true
}));

const requireAuth = (req, res, next) => {
	if (!req.session.username) {
		return res.redirect("/");
	}
	next();
};

app.get("/", (req, res) => {
	if (req.session.username) {
		return res.redirect("/backlog");
	}
	res.render("login", { error: null });
});

app.post("/", (req, res) => {
	const { username, password } = req.body;
	
	if (users[username] && users[username] === password) {
		req.session.username = username;
		return res.redirect("/backlog");
	}
	
	res.render("login", { error: "Invalid credentials" });
});

app.get("/register", (req, res) => {
	res.render("register", { error: null });
});

app.post("/register", (req, res) => {
	const { username, password } = req.body;
	
	if (users[username]) {
		return res.render("register", { error: "Username taken" });
	}
	
	users[username] = password;
	userNotes[username] = [];
	req.session.username = username;
	res.redirect("/backlog");
});

app.get("/backlog", requireAuth, (req, res) => {
	res.render("backlog", { notes: userNotes[req.session.username] || [], username: req.session.username });
});

app.post("/backlog", requireAuth, (req, res) => {
	var { title, content } = req.body;
	title = title.replace(/[^ &-z]/g, "");

	userNotes[req.session.username].push({ title, content });
	res.redirect("/backlog");
});

app.post("/backlog/:id/update", requireAuth, (req, res) => {
	var { title, content } = req.body;
	title = title.replace(/[^ &-z]/g, "");

	const id = parseInt(req.params.id);
	userNotes[req.session.username][id] = {
		title: title,
		content: content
	};
	res.redirect("/backlog");
});

app.post("/backlog/:id/delete", requireAuth, (req, res) => {
	const id = parseInt(req.params.id);
	userNotes[req.session.username].splice(id, 1);
	res.redirect("/backlog");
});

app.get("/logout", (req, res) => {
	req.session.destroy();
	res.redirect("/");
});

app.listen(PORT, () => {
	console.log(`App server running on port ${PORT}`);
});

appFlag.listen(portFlag, () => {
	console.log(`Flag server running on port ${portFlag}`);
});
