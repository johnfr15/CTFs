import axios from 'https://cdn.skypack.dev/axios';

import MyNotification from '../../notification.js';

axios.defaults.baseURL = window.ENV.BACKEND_URL;
axios.defaults.withCredentials = true;

document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const error = urlParams.get('error');


    if (error === '3') {
        const popup = MyNotification({
            position: 'bottom-right',
            duration: 7000
          });
        popup.error({
        title: 'Erreur',
        message: 'Utilisateur déja pris'
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

    var usernameInput = document.getElementsByName('user')[0]; 
    var passwordInput = document.getElementsByName('pass')[0]; 

    document.getElementById('mybutton').addEventListener('click', function() {
        if (validate(usernameInput) && validate(passwordInput)) {
            $(usernameInput).parent().removeClass('alert-validate');
            $(passwordInput).parent().removeClass('alert-validate');
            register(usernameInput.value, passwordInput.value);

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
                const value = input.value.trim();
                const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
                return regex.test(value);
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


window.register = async function (usernameInput, passwordInput) {
    let username = usernameInput;
    let password = passwordInput;
    try {
        console.log({
            username,
            password
        });
        const response = await axios.post('/register', {
            username,
            password
        });
        console.log(response.data);

        if (response.status === 201 && response.data.message === 'User created') {
            window.location.href = '/login/index.html?registered=true';
        }
    } catch (error) {
        console.error(error);
        if (error.response && error.response.status === 401 && error.response.data.message === 'username déjà existant') {
            window.location.href = '/register/index.html?error=3';
        }
    }
}
