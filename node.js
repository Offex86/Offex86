const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Gemini API Key
const GEMINI_API_KEY = 'AIzaSyCOqzcsmUkWjRFo1HyeKQB5ECgkNn5BQUM'; // अपना API Key यहां डालें

// Generate Image Route
app.post('/generate-image', async (req, res) => {
    const { prompt } = req.body;

    if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required.' });
    }

    try {
        // Gemini API को कॉल करें
        const response = await axios.post(
            `https://api.gemini.com/v1/generate-image?key=${GEMINI_API_KEY}`,
            { prompt }
        );

        // इमेज URL प्राप्त करें
        const imageUrl = response.data.imageUrl;
        res.json({ imageUrl });
    } catch (error) {
        console.error('Error calling Gemini API:', error);
        res.status(500).json({ error: 'Failed to generate image.' });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});