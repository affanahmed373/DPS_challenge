const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const jsonBody = {
  github: 'https://github.com/affanahmed373/DPS_challenge',
  email: 'affan.ahmed.93@gmail.com',
  url: 'https://dpschallenge22.herokuapp.com/',
  notes:
    'I have used Heroku and flash. I have used different models but Naive Bayes output was similar to Decision Trees and KNN . Hence I choose Naive Bayes. I include 4 inputs to the prediction values. Hence I also used a library to map categorical data into numerics'
};

const password = hotpTotpGenerator.totp({
  key: 'affan.ahmed.93@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, jsonBody, { headers })
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));