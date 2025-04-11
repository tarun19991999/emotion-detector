const emotionGifs = {
    admiration: "https://media.giphy.com/media/xT9IgIc0lryrxvqVGM/giphy.gif",
    amusement: "https://media.giphy.com/media/3o6ZsZKnI3P1P7UQbG/giphy.gif",
    anger: "https://media.giphy.com/media/l3vR9O2qfKAGTjCo0/giphy.gif",
    annoyance: "https://media.giphy.com/media/3ohc1fQjGmrpA9G26c/giphy.gif",
    approval: "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
    caring: "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
    confusion: "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif",
    curiosity: "https://media.giphy.com/media/3ohhwC8bQy9YDBNUNm/giphy.gif",
    desire: "https://media.giphy.com/media/XA3ZlB9QGPaEo/giphy.gif",
    disappointment: "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    disapproval: "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
    disgust: "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif",
    embarrassment: "https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif",
    excitement: "https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif",
    fear: "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif",
    gratitude: "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif",
    grief: "https://media.giphy.com/media/l0IylOPCNkiqOgMyA/giphy.gif",
    joy: "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif",
    love: "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    nervousness: "https://media.giphy.com/media/3orieVcQmAa0VW7C3y/giphy.gif",
    optimism: "https://media.giphy.com/media/3og0IvFudLI4lM9b6s/giphy.gif",
    pride: "https://media.giphy.com/media/3ohzdYJK1wAdPWVk88/giphy.gif",
    realization: "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
    relief: "https://media.giphy.com/media/l3q2Vh8Y3bb9mV4JW/giphy.gif",
    remorse: "https://media.giphy.com/media/l2Je0c1fQ9H3HJ7dO/giphy.gif",
    sadness: "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
    surprise: "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
    neutral: "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif"
  };
  
  const emotionSongs = {
    admiration: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    amusement: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    anger: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    annoyance: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    approval: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
    caring: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    confusion: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
    curiosity: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    desire: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3",
    disappointment: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3",
    disapproval: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3",
    disgust: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3",
    embarrassment: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3",
    excitement: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3",
    fear: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3",
    gratitude: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3",
    grief: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    joy: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    love: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    nervousness: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    optimism: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
    pride: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    realization: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
    relief: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    remorse: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3",
    sadness: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3",
    surprise: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3",
    neutral: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"
  };
  
  async function detectEmotion() {
    const text = document.getElementById("textInput").value;
    const resultDiv = document.getElementById("result");
    const gifBox = document.getElementById("gifBox");
  
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    });
  
    const data = await response.json();
    const emotion = data.emotion;
    const confidence = data.confidence;
  
    resultDiv.innerHTML = `<h2>Detected Emotion: <strong>${emotion.toUpperCase()}</strong></h2>
                           <h3>Confidence: <strong>${confidence}</strong></h3>`;
  
    gifBox.innerHTML = `
      <img src="${emotionGifs[emotion]}" alt="${emotion}" style="max-width:100%; margin-top:10px;" />
      <audio controls autoplay style="margin-top: 10px;">
        <source src="${emotionSongs[emotion]}" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>`;
  }
  