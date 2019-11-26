const express = require("express")
const path = require ("path")

const app = express();
const port = process.env.PORT || "8000";

/**
 * Routes Definitions
 */
app.get("/", (req,res) => {
    //res.status(200).send("Whatabyte: Food for devs")
    res.render("index", {title: "Home"})
});
app.get("/user", (req, res) => {
    res.render("user", {title: "Profile", })
    
});

app.get("/about", (req,res) => {
    res.render("about", {title: "About"})
});


app.listen(port,  ()=> {
console.log('Listening to requests on http://localhost:${port}');
});

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(express.static(path.join(__dirname, "public")));
