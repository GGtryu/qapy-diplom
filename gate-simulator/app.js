// gate-simulator/app.js
const express = require('express');
const app = express();
const port = 9999;

app.use(express.json());

// Карта, по которой платеж/кредит будет APPROVED
const APPROVED_CARD = '4444444444444441';
// Карта, по которой платеж/кредит будет DECLINED
const DECLINED_CARD = '4444444444444442';

// Обработчик для /api/v1/process-payment
app.post('/api/v1/process-payment', (req, res) => {
  console.log('Received payment request:', req.body);
  const cardNumber = req.body.number?.replace(/\s/g, ''); // Убираем пробелы

  if (cardNumber === APPROVED_CARD) {
    console.log('Payment APPROVED');
    res.json({ status: 'APPROVED' });
  } else if (cardNumber === DECLINED_CARD) {
    console.log('Payment DECLINED');
    res.json({ status: 'DECLINED' });
  } else {
    console.log('Payment DECLINED (unknown card)');
    res.json({ status: 'DECLINED' }); // Для любой другой карты
  }
});

// Обработчик для /api/v1/process-credit
app.post('/api/v1/process-credit', (req, res) => {
  console.log('Received credit request:', req.body);
  const cardNumber = req.body.number?.replace(/\s/g, ''); // Убираем пробелы

  if (cardNumber === APPROVED_CARD) {
    console.log('Credit APPROVED');
    res.json({ status: 'APPROVED' });
  } else if (cardNumber === DECLINED_CARD) {
    console.log('Credit DECLINED');
    res.json({ status: 'DECLINED' });
  } else {
    console.log('Credit DECLINED (unknown card)');
    res.json({ status: 'DECLINED' }); // Для любой другой карты
  }
});

app.listen(port, () => {
  console.log(`Gate Simulator listening at http://localhost:${port}`);
});