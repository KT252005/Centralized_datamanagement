// login.js

const loginForm = document.getElementById('login-form');
const loginMessage = document.getElementById('login-message');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const role = document.getElementById('role').value;

    if (!username || !password || !role) {
        loginMessage.textContent = 'All fields are required';
        loginMessage.style.color = 'red';
        return;
    }

    // CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ username, password, role })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'access.html';
        } else {
            loginMessage.textContent = 'Invalid username, password, or role';
            loginMessage.style.color = 'red';
        }
    })
    .catch(error => {
        loginMessage.textContent = 'An error occurred. Please try again.';
        loginMessage.style.color = 'red';
    });
});
