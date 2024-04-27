const nodemailer = require('nodemailer');

// Dados do formulário
const nome = prompt('Nome: ');
const email = prompt('E-mail: ');
const telefone = prompt('Telefone: ');
const data = prompt('Data: ');
const hora = prompt('Hora: ');

// Mensagem de e-mail
const mensagem = `
Nome: ${nome}
E-mail: ${email}
Telefone: ${telefone}
Data: ${data}
Hora: ${hora}
`;

// Configurações do servidor de e-mail
const smtpTransport = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: true,
  auth: {
    user: 'SEU_EMAIL_GMAIL@gmail.com',  // Substitua por seu e-mail
    pass: 'SUA_SENHA_GMAIL'  // Substitua por sua senha
  }
});

// Cria o objeto de mensagem
const mailOptions = {
  from: 'SEU_EMAIL_GMAIL@gmail.com',  // Substitua por seu e-mail
  to: 'contato@brechossim.com.br',
  subject: 'Agendamento BrechóSim',
  text: mensagem
};

// Envia o e-mail
smtpTransport.sendMail(mailOptions, (err, info) => {
  if (err) {
    console.error('Erro ao enviar e-mail:', err);
  } else {
    console.log('E-mail enviado com sucesso!');
  }
});
