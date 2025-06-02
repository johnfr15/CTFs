import axios from 'https://cdn.skypack.dev/axios';

import MyNotification from '../../notification.js';

axios.defaults.baseURL = window.ENV.BACKEND_URL;
axios.defaults.withCredentials = true;

document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const registered = urlParams.get('registered');
    const error = urlParams.get('error');


    if (registered === 'true') {
        const popup = MyNotification({
            position: 'bottom-right',
            duration: 7000
          });
        popup.info({
        title: 'Félicitations',
        message: 'Utilisateur créé avec succès'
        });
    }
    else if (error === '1') {
        const popup = MyNotification({
            position: 'bottom-right',
            duration: 7000
          });
        popup.error({
        title: 'Erreur',
        message: 'Utilisateur inconnu'
        });
    }
    else if (error === '2') {
        const popup = MyNotification({
            position: 'bottom-right',
            duration: 7000
          });
        popup.error({
        title: 'Erreur',
        message: 'Mot de passe incorrect'
        });
    }

    var inputs = document.querySelectorAll('.input100');
    inputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            if (input.value.trim() !== "") {
                input.classList.add('has-val');
            } else {
                input.classList.remove('has-val');
            }
        });
    });

    var usernameInput = document.getElementsByName('user')[0]; // Select the first element with name 'user'
    var passwordInput = document.getElementsByName('pass')[0]; // Select the first element with name 'pass'

    document.getElementById('mybutton').addEventListener('click', function() {
        if (validate(usernameInput) && validate(passwordInput)) {
            $(usernameInput).parent().removeClass('alert-validate');
            $(passwordInput).parent().removeClass('alert-validate');
            login(usernameInput.value, passwordInput.value);

        } else {
            if(validate(usernameInput)){
                $(passwordInput).parent().addClass('alert-validate');
                $(usernameInput).parent().removeClass('alert-validate');
            } else if(validate(passwordInput)){
                $(usernameInput).parent().addClass('alert-validate');
                $(passwordInput).parent().removeClass('alert-validate');  
            } else {
                $(usernameInput).parent().addClass('alert-validate');
                $(passwordInput).parent().addClass('alert-validate');
            }}
        


    function validate(input) {
        return input.value.trim() !== '';
    }

});
var showPass = 0;
var btnShowPass = document.querySelectorAll('.btn-show-pass');

btnShowPass.forEach(function(button) {
    button.addEventListener('click', function() {
        var input = this.parentElement.querySelector('input');

        if (showPass == 0) {
            input.type = 'text';
            this.querySelector('i').classList.remove('zmdi-eye');
            this.querySelector('i').classList.add('zmdi-eye-off');
            showPass = 1;
        } else {
            input.type = 'password';
            this.querySelector('i').classList.add('zmdi-eye');
            this.querySelector('i').classList.remove('zmdi-eye-off');
            showPass = 0;
        }
    });
});
});

window.login = async function (usernameInput, passwordInput) {
    let username= usernameInput;
    let password= passwordInput;
    try {
        console.log({
            username,
            password
        });
        const response = await axios.post('/login', {
            username,
            password
        });
        console.log(response.data);
        if (response.status === 200) {
            window.location.href = '/'; // replace '/main' with the actual URL of your main page
        }
        // Successful login, redirect to main page or handle it as per your application flow
    } catch (error) {
        console.error(error);
        if (error.response && error.response.status === 401) {
            if (error.response.data.message === 'Utilisateur inexistant') {
                window.location.href = '/login/index.html?error=1';
            }
            if (error.response.data.message === 'Mot de passe incorrect') {
                window.location.href = '/login/index.html?error=2';
            }
        }
    }
}
