const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => res.send('Hello From Express'))
app.get('/prueba',(req, res) => res.sendFile('prueba.html'))
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
