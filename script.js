document.getElementById('imageForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const prompt = document.getElementById('prompt').value;
    const resultDiv = document.getElementById('result');
    const generatedImage = document.getElementById('generatedImage');

    if (!prompt) {
        alert('कृपया एक विवरण दर्ज करें।');
        return;
    }

    resultDiv.innerHTML = 'Generating...';

    try {
        const response = await fetch('/generate-image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt }),
        });

        const data = await response.json();
        if (data.imageUrl) {
            generatedImage.src = data.imageUrl;
            generatedImage.style.display = 'block';
            resultDiv.innerHTML = '';
        } else {
            resultDiv.innerHTML = 'Error generating image.';
        }
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerHTML = 'An error occurred. Please try again.';
    }
});