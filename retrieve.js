//get student
const form = document.getElementById('getStudentForm');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Get registration number from user input using prompt
    const regno = document.getElementById('regno').value.trim();
    if (regno == "all") {
        // Make a GET request to retrieve all student data
        axios.get('http://127.0.0.1:8000/rsquare/Student/')
            .then(function(response) {
                // Handle success
                displayStudentData(response.data);
            })
            .catch(function(error) {
                // Handle error
                console.error('Error fetching student data:', error);
            });
    }
    
    // Make a GET request to retrieve student data for the provided registration number
    axios.get(`http://127.0.0.1:8000/rsquare/Student/${regno}`)
        .then(function(response) {
            // Handle success
            displayStudentData(response.data);
        })
        .catch(function(error) {
            // Handle error
            console.error('Error fetching student data:', error);
        });
});

function displayStudentData(data) {
    const outputDiv = document.getElementById('studentDataDiv');
    if (data.Status_msg) {
        // Display error message if student doesn't exist
        outputDiv.textContent = data.Status_msg;
    } else {
        // Display student data
        outputDiv.innerHTML = `Name: ${data.student_name}, Reg No: ${data.student_regno}`;
    }
}
