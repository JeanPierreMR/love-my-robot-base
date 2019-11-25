const express = require("express")
const path = require ("path")

<<<<<<< HEAD
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
    res.render("user", {title: "Profile", userProfile: {nickname: "Auth0"}})
});


app.listen(port,  ()=> {
console.log('Listening to requests on http://localhost:${port}');
});

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(express.static(path.join(__dirname, "public")));

=======
app.get('/', (req, res) => res.send('Hello From Express'))
app.get('/prueba',(req, res) => res.sendFile('prueba.html'))
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
>>>>>>> cb56948156b50f18ebd94978fbd2c63892173591
