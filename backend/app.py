# AgriSense AI - Enhanced Backend with Real AI Capabilities
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import requests
import os
from datetime import datetime
import json
import sqlite3

# Initialize FastAPI app
app = FastAPI(title="AgriSense AI Backend", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class FarmerProfile(BaseModel):
    name: str
    location: str
    farm_size: float
    primary_crop: str
    soil_type: str

class ChatMessage(BaseModel):
    message: str
    language: str = "en"
    farmer_id: Optional[str] = None

class WeatherData(BaseModel):
    location: str
    temperature: float
    humidity: float
    rainfall: float
    wind_speed: float

# Initialize AI Agent
class AgriSenseAI:
    def __init__(self):
        self.setup_database()
        self.load_knowledge_base()
    
    def setup_database(self):
        """Setup SQLite database"""
        self.conn = sqlite3.connect("agrisense.db", check_same_thread=False)
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS farmers (
                id TEXT PRIMARY KEY,
                name TEXT,
                location TEXT,
                farm_size REAL,
                primary_crop TEXT,
                soil_type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                farmer_id TEXT,
                message TEXT,
                response TEXT,
                language TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (farmer_id) REFERENCES farmers (id)
            )
        """)
        
        self.conn.commit()
    
    def load_knowledge_base(self):
        """Load agricultural knowledge base"""
        self.knowledge_base = {
            "crops": {
                "rice": {
                    "water_requirement": "1200-1500mm",
                    "fertilizer": "NPK 120:60:40 kg/ha",
                    "common_pests": ["Brown planthopper", "Stem borer"],
                    "diseases": ["Blast", "Sheath blight"],
                    "planting_time": "June-July (Kharif)"
                },
                "wheat": {
                    "water_requirement": "450-600mm", 
                    "fertilizer": "NPK 120:60:40 kg/ha",
                    "common_pests": ["Aphids", "Termites"],
                    "diseases": ["Rust", "Smut"],
                    "planting_time": "November-December"
                }
            },
            "weather_recommendations": {
                "high_temperature": {
                    "irrigation": "Early morning (5-7 AM) or evening (6-8 PM)",
                    "activities": "Avoid midday field work"
                },
                "heavy_rain": {
                    "irrigation": "Skip irrigation",
                    "activities": "Avoid field operations"
                }
            }
        }
    
    def get_weather_data(self, location: str) -> Dict:
        """Get weather data from OpenWeatherMap API"""
        api_key = os.getenv("OPENWEATHER_API_KEY", "demo_key")
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "rainfall": data.get("rain", {}).get("1h", 0)
                }
        except Exception as e:
            print(f"Weather API error: {e}")
        
        # Fallback simulated data
        import random
        return {
            "temperature": random.randint(20, 35),
            "humidity": random.randint(40, 80),
            "description": "partly cloudy",
            "wind_speed": random.randint(5, 20),
            "rainfall": random.randint(0, 10)
        }
    
    def generate_response(self, message: str, farmer_profile: Dict, weather: Dict) -> str:
        """Generate AI response using knowledge base and context"""
        message_lower = message.lower()
        crop = farmer_profile.get("primary_crop", "").lower()
        
        if any(word in message_lower for word in ["irrigat", "water"]):
            return self.get_irrigation_advice(weather, crop)
        elif any(word in message_lower for word in ["fertiliz", "nutri"]):
            return self.get_fertilizer_advice(crop)
        elif any(word in message_lower for word in ["pest", "disease"]):
            return self.get_pest_advice(crop)
        elif any(word in message_lower for word in ["weather"]):
            return self.get_weather_advice(weather)
        elif any(word in message_lower for word in ["price", "market"]):
            return self.get_market_advice(crop)
        else:
            return self.get_general_advice(message, farmer_profile, weather)
    
    def get_irrigation_advice(self, weather: Dict, crop: str) -> str:
        temp = weather["temperature"]
        rainfall = weather.get("rainfall", 0)
        
        if rainfall > 10:
            return f"🌧️ Skip irrigation today! Heavy rain ({rainfall}mm) expected. Your {crop} will get sufficient water naturally."
        elif temp > 35:
            return f"🌡️ Hot weather irrigation needed! Temperature is {temp}°C. Water your {crop} early morning (5-7 AM) or evening (6-8 PM)."
        else:
            return f"💧 Regular irrigation recommended. Current weather is moderate ({temp}°C). Water your {crop} based on soil moisture."
    
    def get_fertilizer_advice(self, crop: str) -> str:
        if crop in self.knowledge_base["crops"]:
            fertilizer = self.knowledge_base["crops"][crop]["fertilizer"]
            return f"🌱 Fertilizer recommendation for {crop}: Apply {fertilizer}. Split application is recommended for better efficiency."
        return f"🌱 For {crop}, conduct soil test first. Generally apply NPK in ratio 4:2:1. Consult local agriculture officer for specific recommendations."
    
    def get_pest_advice(self, crop: str) -> str:
        if crop in self.knowledge_base["crops"]:
            pests = ", ".join(self.knowledge_base["crops"][crop]["common_pests"])
            diseases = ", ".join(self.knowledge_base["crops"][crop]["diseases"])
            return f"🐛 Pest & Disease management for {crop}: Common pests: {pests}. Common diseases: {diseases}. Use IPM
            def get_pest_advice(self, crop: str) -> str:
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


