const express = require('express');
const cors = require('cors');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json());

const cards = [
    { number: '4444 4444 4444 4441', status: 'APPROVED' },
    { number: '4444 4444 4444 4442', status: 'DECLINED' }
];

app.post('/payment', (req, res) => {
    const card = cards.find(c => c.number === req.body.number);
    if (card) {
        res.json({ status: card.status });
    } else {
        res.status(400).json({ error: 'Invalid card' });
    }
});

app.post('/credit', (req, res) => {
    const card = cards.find(c => c.number === req.body.number);
    if (card) {
        res.json({ status: card.status });
    } else {
        res.status(400).json({ error: 'Invalid card' });
    }
});

app.get('/', (req, res) => {
    res.json({ status: 'ok' });
});

app.listen(9999, '0.0.0.0', () => {
    console.log('Gate simulator running on port 9999');
});
