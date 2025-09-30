# 🌾 AgriSense AI - User Guide

## 📱 Getting Started

### Step 1: Access AgriSense AI
- **Web App**: Visit your deployment URL
- **Mobile**: Works on any smartphone browser
- **Desktop**: Compatible with all modern browsers

### Step 2: Complete Your Profile
Fill in your farming details:
- **Name**: Your name or farm name
- **Location**: Village, District, State
- **Farm Size**: Total area in acres
- **Primary Crop**: Main crop you grow
- **Soil Type**: Type of soil on your farm

## 🗣️ Using Voice Features

### Voice Input
1. Click the **🎤 microphone** button
2. Speak your question clearly
3. Wait for the transcription to appear
4. The AI will respond with voice + text

### Supported Languages
- **English**: "Should I water my wheat today?"
- **हिंदी**: "क्या आज मुझे अपनी गेहूं की फसल में पानी देना चाहिए?"
- **తెలుగు**: "నేడు నా గోధుమకు నీరు పెట్టాలా?"
- **தமிழ்**: "இன்று என் கோதுமைக்கு தண்ணீர் ஊற்ற வேண்டுமா?"
- **मराठी**: "आज माझ्या गव्हाला पाणी द्यावे का?"

## 💬 Sample Questions to Ask

### 🌧️ Weather & Irrigation
- "Should I irrigate my crops today?"
- "What's the weather forecast for farming?"
- "When is the best time to water plants?"
- "Will it rain tomorrow?"

### 🌱 Fertilizers & Nutrients
- "What fertilizer should I use for rice?"
- "When to apply fertilizer to wheat?"
- "How much nitrogen does my crop need?"
- "Organic fertilizer recommendations?"

### 🐛 Pests & Diseases
- "How to control aphids in wheat?"
- "My tomato plants have yellow leaves, what to do?"
- "Organic pest control methods?"
- "Early signs of crop diseases?"

### 📈 Market & Prices
- "Current market price of onions?"
- "Best time to sell my wheat?"
- "Where can I get better prices?"
- "Market trends for cotton?"

### 🌾 Crop Management
- "When to plant rice this season?"
- "How to improve crop yield?"
- "Crop rotation suggestions?"
- "Harvesting time for sugarcane?"

## 📊 Understanding Recommendations

### Priority Levels
- **🔴 High Priority**: Urgent actions needed (weather alerts, pest outbreaks)
- **🟡 Medium Priority**: Important but not urgent (fertilizer application)
- **🟢 Low Priority**: General maintenance (record keeping)

### Action Buttons
- **Done**: Mark recommendation as completed
- **More Info**: Get detailed information
- **Remind Later**: Set reminder for later

## 📅 Crop Calendar Features

### Automatic Scheduling
- **Today**: Current day's recommended activities
- **Tomorrow**: Next day's planned tasks
- **This Week**: 7-day activity overview

### Task Categories
- **🌱 Sowing/Planting**: Seed sowing activities
- **💧 Irrigation**: Watering schedules
- **🌿 Fertilization**: Nutrient application
- **🔍 Monitoring**: Pest and disease checks
- **🚜 Harvesting**: Crop harvesting activities

## 📈 Farm Analytics

### Performance Metrics
- **Total Queries**: Number of questions asked
- **Average Yield**: Expected yield based on practices
- **Cost Savings**: Money saved through optimization
- **AI Accuracy**: Reliability of recommendations

### Tracking Benefits
- Monitor improvement in farming decisions
- Track cost savings from AI recommendations
- Compare yields across seasons
- Measure efficiency gains

## 🌤️ Weather Integration

### Current Conditions
- **Temperature**: Real-time temperature data
- **Humidity**: Moisture levels in air
- **Rainfall**: Precipitation forecast
- **Wind Speed**: Air movement patterns

### Weather Alerts
- **🌧️ Rain Alerts**: Heavy rainfall warnings
- **🔥 Heat Warnings**: High temperature alerts
- **💨 Wind Alerts**: Strong wind notifications
- **❄️ Cold Alerts**: Frost and cold warnings

## 📱 Mobile Usage Tips

### Best Practices
1. **Stable Internet**: Ensure good internet connection
2. **Microphone Access**: Allow microphone permissions
3. **Location Services**: Enable location for weather data
4. **Regular Updates**: Keep browser updated

### Battery Saving
- Use text input when battery is low
- Close other apps while using voice features
- Enable power saving mode if needed

## 🔒 Privacy & Security

### Data Protection
- **Local Storage**: Profile data stored on your device
- **No Personal Info Sharing**: Your data stays private
- **Secure Communication**: All data encrypted
- **No Third-party Tracking**: Your privacy is protected

### Data You Can Control
- **Profile Information**: Update anytime
- **Conversation History**: Clear when needed
- **Preferences**: Customize language and settings

## ❓ Troubleshooting

### Common Issues

#### Voice Not Working
- **Check Microphone**: Ensure microphone is enabled
- **Browser Permissions**: Allow microphone access
- **Speak Clearly**: Use clear pronunciation
- **Retry**: Try again if transcription is unclear

#### Slow Response
- **Internet Connection**: Check your internet speed
- **Browser Cache**: Clear browser cache
- **Refresh Page**: Reload the application
- **Try Again**: Retry your question

#### Incorrect Recommendations
- **Update Profile**: Ensure profile information is correct
- **Be Specific**: Ask more detailed questions
- **Provide Context**: Mention your location and crop
- **Try Different Phrasing**: Rephrase your question

#### Weather Data Not Showing    def get_pest_advice(self, crop: str) -> str:
        if crop in self.knowledge_base["crops"]:
            pests = ", ".join(self.knowledge_base["crops"][crop]["common_pests"])
            diseases = ", ".join(self.knowledge_base["crops"][crop]["diseases"])
            return f"🐛 Pest & Disease management for {crop}: Common pests: {pests}. Common diseases: {diseases}. Use IPM approach - biological control first, then chemical if needed."
        return "🐛 General pest management: Monitor crops daily, use yellow sticky traps, apply neem oil spray (10ml/liter) for soft-bodied insects."
    
    def get_weather_advice(self, weather: Dict) -> str:
        temp = weather["temperature"]
        humidity = weather["humidity"]
        description = weather["description"]
        
        advice = f"🌤️ Current weather: {temp}°C, {humidity}% humidity, {description.title()}. "
        
        if temp > 35:
            advice += "🔥 Heat stress alert: Provide shade to crops and livestock, increase irrigation frequency."
        elif humidity > 80:
            advice += "💨 High humidity alert: Monitor for fungal diseases, improve air circulation."
        else:
            advice += "✅ Good weather for farming: Suitable for most field operations."
        
        return advice
    
    def get_market_advice(self, crop: str) -> str:
        # Simulated market data
        market_prices = {
            "rice": "₹2,100/quintal",
            "wheat": "₹2,300/quintal", 
            "cotton": "₹6,200/quintal"
        }
        
        price = market_prices.get(crop, "₹2,000/quintal")
        return f"📈 Market update for {crop}: Current price: {price}. Trend: Stable. Recommendation: Monitor daily prices using eNAM app."
    
    def get_general_advice(self, message: str, farmer_profile: Dict, weather: Dict) -> str:
        name = farmer_profile.get("name", "Farmer")
        crop = farmer_profile.get("primary_crop", "crops")
        
        return f"👨‍🌾 Hello {name}! For your {crop}: Monitor crop health daily, follow weather-based decisions, maintain proper records, use quality inputs. Need specific help? Ask about irrigation, fertilizers, pests, or market prices!"

# Initialize AI instance
ai_agent = AgriSenseAI()

# API Routes
@app.get("/")
async def root():
    """Serve the main HTML page"""
    try:
        with open("../frontend/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>AgriSense AI Backend</h1><p>Frontend not found. Please ensure frontend/index.html exists.</p>")

@app.post("/api/chat")
async def chat(message: ChatMessage):
    """Handle chat messages and generate AI responses"""
    try:
        # Get farmer profile if farmer_id provided
        farmer_profile = {}
        if message.farmer_id:
            cursor = ai_agent.conn.cursor()
            cursor.execute("SELECT * FROM farmers WHERE id = ?", (message.farmer_id,))
            row = cursor.fetchone()
            if row:
                farmer_profile = {
                    "name": row[1],
                    "location": row[2],
                    "farm_size": row[3],
                    "primary_crop": row[4],
                    "soil_type": row[5]
                }
        
        # Get weather data
        location = farmer_profile.get("location", "India")
        weather = ai_agent.get_weather_data(location)
        
        # Generate AI response
        response = ai_agent.generate_response(message.message, farmer_profile, weather)
        
        # Save conversation to database
        if message.farmer_id:
            cursor = ai_agent.conn.cursor()
            cursor.execute(
                "INSERT INTO conversations (farmer_id, message, response, language) VALUES (?, ?, ?, ?)",
                (message.farmer_id, message.message, response, message.language)
            )
            ai_agent.conn.commit()
        
        return {
            "response": response,
            "weather": weather,
            "timestamp": datetime.now().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.post("/api/farmer/profile")
async def save_farmer_profile(profile: FarmerProfile):
    """Save or update farmer profile"""
    try:
        farmer_id = f"farmer_{hash(profile.name + profile.location)}"
        
        cursor = ai_agent.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO farmers (id, name, location, farm_size, primary_crop, soil_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (farmer_id, profile.name, profile.location, profile.farm_size, profile.primary_crop, profile.soil_type))
        
        ai_agent.conn.commit()
        
        return {"farmer_id": farmer_id, "message": "Profile saved successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving profile: {str(e)}")

@app.get("/api/weather/{location}")
async def get_weather(location: str):
    """Get weather data for a location"""
    try:
        weather = ai_agent.get_weather_data(location)
        return weather
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching weather: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# For deployment
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
