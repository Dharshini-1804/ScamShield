
import gradio as gr
import joblib
from pathlib import Path

# Load the trained model
MODEL_PATH = Path(__file__).parent / "models" / "scamshield_model.pkl"
model = joblib.load(MODEL_PATH)

def check_message(message):
    if not message or not message.strip():
        return "Please enter a message.", "N/A"

    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    confidence = max(probabilities) * 100

    if prediction == "spam":
        result = "🚨 SPAM MESSAGE DETECTED"
    else:
        result = "✅ HAM MESSAGE"

    return result, f"{confidence:.2f}%"

with gr.Blocks(
    theme=gr.themes.Soft(),
    title="ScamShield"
) as demo:

    gr.Markdown("# 🛡️ ScamShield")
    gr.Markdown("### AI-Powered SMS Spam Detection")

    message = gr.Textbox(
        label="Enter your SMS message",
        placeholder="Paste your message here...",
        lines=4
    )

    button = gr.Button("🔍 Analyze Message")

    result = gr.Textbox(label="Detection Result")
    confidence = gr.Textbox(label="Confidence Score")

    button.click(
        check_message,
        inputs=message,
        outputs=[result, confidence]
    )

    gr.Examples(
        examples=[
            ["Congratulations! You won a free prize. Click this link now!"],
            ["Hey, are you coming to college tomorrow?"],
            ["URGENT! Your bank account will be blocked. Verify your details now."],
            ["Good morning! Have a nice day."]
        ],
        inputs=message
    )

demo.launch()
