AgriSense AI - Hugging Face Spaces Deployment
"""
import gradio as gr
import os

# Read the main HTML file
def load_html():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """
        <html>
        <head><title>AgriSense AI</title></head>
        <body style="font-family: Arial, sans-serif; padding: 40px; text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh;">
            <h1>🌾 AgriSense AI - Smart Crop Advisory Agent</h1>
            <h2>🚨 Setup Required</h2>
            <p>Please upload the complete AgriSense AI HTML file as 'index.html'</p>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin: 20px 0;">
                <h3>✨ Features Ready to Deploy:</h3>
                <p>🤖 AI Crop Advisory • 🌤️ Weather Integration • 📈 Market Prices<br>
                   🗣️ Voice Support • 📅 Smart Calendar • 💧 Irrigation Management</p>
                <h3>🎯 Expected Impact:</h3>
                <p>25-30% yield increase • ₹10,000+ savings per acre • 50% faster decisions</p>
            </div>
            <p>Built with ❤️ for farmers worldwide</p>
        </body>
        </html>
        """

# Create Gradio interface
with gr.Blocks(
    title="AgriSense AI - Smart Crop Advisory Agent",
    theme=gr.themes.Soft(primary_hue="green"),
    css="""
        .gradio-container {
            max-width: 100% !important;
            padding: 0 !important;
        }
        .contain {
            max-width: 100% !important;
            padding: 0 !important;
        }
    """
) as app:
    gr.HTML(
        load_html(),
        show_label=False
    )

# Launch configuration
if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        share=False
    )
