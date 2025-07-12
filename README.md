# love_animation

# 💘 Simple Love Calculator

A fun and romantic web app built with Streamlit that calculates a playful "love score" based on two names. This app is designed for pure entertainment, blending quirky logic, aesthetic design, and a touch of desi charm.

## ✨ Features

- 🎀 Beautiful pastel background with gradient love theme
- 💬 Interactive input fields with placeholders for name hints
- 🎯 Unique score calculation based on character frequency in "true" and "love"
- 📊 Animated progress bar with matching vibes
- 💌 Personalized result messages with emojis and cultural flavor
- 🚫 Disclaimer to remind users it’s all for fun!

## 📦 How It Works

The app calculates the love score using a custom logic:

```python
combined = (name1 + name2).lower()
true_score = sum(combined.count(char) for char in "true")
love_score = sum(combined.count(char) for char in "love")
final_score = true_score * 10 + love_score
