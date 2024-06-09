console.log("first")


const paragraphs = document.querySelectorAll('p');

// const data  = paragraphs.
paragraphs.forEach(paragraph => {


    paragraph.style.backgroundColor = 'blue';
    //   paragraph.innerHTML = "hello"
    // Sending data to Pyth
    var dataToSend = "Hello, world!"; // Data to send to the text file

    fetch('http://localhost:5000/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: dataToSend })
    })
    .then(response => response.text())
    .then(data => {
        console.log('Response from server:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

});
// export default paragraphs