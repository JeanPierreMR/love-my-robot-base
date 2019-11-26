const express = require("express")
const path = require ("path")
const axios = require('axios')
const app = express();
const port = process.env.PORT || "8000";
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

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



app.post('/load_code', function (req, res) { 
    console.log(req.body.code)
    axios.post('http://0.0.0.0:5000/', {
        code: req.body.code
    })
    .then((res) => {
        //console.log(`statusCode: ${res.statusCode}`)
        //console.log(res)
    })
    .catch((error) => {
        console.error(error)
    })  
})

