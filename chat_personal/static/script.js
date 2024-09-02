document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log("Form submitted");  
    let formData = {
            gst_no: document.getElementById('gst').value,
            company_name: document.getElementById('company-name').value,
            domain: document.getElementById('domain').value,
            address: document.getElementById('address').value,
            city: document.getElementById('city').value,
            state: document.getElementById('state').value,
            pincode: document.getElementById('pincode').value,
            contact_info: document.getElementById('contact').value
        };
   
    console.log("Data to send:", formData); 
    fetch('/Registration.html/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Ensure JSON content type is set
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  // Correct way to include CSRF token
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.success) {
            alert(data.message); 
            console.log('Redirecting to:', data.redirect_url);
            window.location.href = data.redirect_url;  // Redirect to the URL provided in the response
        } else {
            alert(data.error);  // Show error message
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});