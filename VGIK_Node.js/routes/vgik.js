const {Router} = require('express')
const router = Router()


router.get('/', (req, res) => {
    res.render('index', {
        title: 'ВГИК'
    })
})
router.get('/learning', (req, res) => {
    res.render('learning', {
        title: 'Обучение'
    })
})
router.get('/eios', (req, res) => {
    res.render('eios', {
        title: 'ЕИОС'
    })
})
router.get('/contacts', (req, res) => {
    res.render('contacts', {
        title: 'Контакты'
    })
})
router.get('/news', (req, res) => {
    res.render('news', {
        title: 'Новости'
    })
})
router.get('/about', (req, res) => {
    res.render('about', {
        title: 'Основные сведения'
    })
})

module.exports = router