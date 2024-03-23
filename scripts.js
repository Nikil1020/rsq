const form = document.getElementById('studentForm');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('stname').value;
    const regno = document.getElementById('streg').value;
    
    axios.post('http://127.0.0.1:8000/rsquare/Student/', { student_name: name, student_regno: regno })
        .then(function (response) {
            // Handle success
            alert('Student added successfully');
        })
        .catch(function (error) {
            // Handle error
            console.error('Error adding student:', error);
        });
});




