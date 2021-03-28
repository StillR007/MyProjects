const express = require('express')
const mongoose = require('mongoose')
const exphbs = require('express-handlebars')
const vgikRoutes = require('./routes/vgik')
const path = require('path')

const PORT = process.env.PORT || 3000

const app = express()
const hbs = exphbs.create({
    defaultLayout: "main",
    extname: 'hbs'
})

app.engine("hbs", hbs.engine)
app.set('view engine', 'hbs')
app.set('views', 'views')

app.use(vgikRoutes)
app.use(express.static(path.join(__dirname, 'css')))
app.use(express.static(path.join(__dirname, 'images')))


async function start() {
    try{
        await mongoose.connect('mongodb+srv://Roman:KG7BxfDBvb69VHi@cluster.kgutd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {
            useNewUrlParser: true,
            useFindAndModify: false
        })
        app.listen(PORT, () => {
            console.log('Server has been started')
        })
    } catch (e) {
        console.log(e)
    }
}

start()
