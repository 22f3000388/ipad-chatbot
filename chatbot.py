from dotenv import load_dotenv
import streamlit as st
import os
import json
import google.generativeai as genai


load_dotenv() 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

KNOWLEDGE_BASE = {
  "iPad Pro (M4)": {
    "release_date": "May 15, 2024",
    "display": "Ultra Retina XDR display with Tandem OLED technology and The new Ultra Retina XDR display introduces groundbreaking tandem OLED technology. Extreme brightness, incredibly precise contrast and advanced technologies like ProMotion and True Tone give you a jaw-dropping visual experience. And you can use Reference Mode for colour-accurate workflows.",
    "display_specs": {
      "full_screen_brightness": "1,000 nits",
      "peak_hdr_brightness": "1,600 nits",
      "contrast_ratio": "20,00,000:1",
      "true_tone": "for comfortable viewing",
      "promotion": "adaptive 10-120Hz refresh rate",
      "color_gamut": "P3 wide colour",
      "precision_highlights": "Precision specular highlights convey more true-to-life details and accurate reflections of light in every image. So breathtaking HDR landscapes, textures and tones feel even more vibrant and realistic.",
      "contrast_ratio_details": "20,00,000:1 contrast ratio delivers deeper blacks for extreme dynamic range. There is pinpoint brightness in the stars and incredible detail in low light and shadows.",
      "nano_texture_glass": "Nano‑texture display glass is a new option that's perfect for high‑end, colour-managed workflows or the most demanding ambient lighting environments. Precisely etched at a nanometre scale, nano‑texture glass maintains image quality and contrast while scattering ambient light for even less glare.",
      "resolution": "2420 x 1668 pixels (11-inch), 2752 x 2064 pixels (13-inch)",
      "pixel_density": "264 pixels per inch",
      "reference_mode": "for colour-accurate workflows",
      "tandem_oled": "Dual-layer OLED technology for enhanced brightness and contrast"
    },
    "sizes": ["11-inch", "13-inch"],
    "chip": "Apple M4 chip",
    "chip_details": {
      "description": "Introducing M4, the next generation of Apple silicon. M4 is built for Apple Intelligence on iPad Pro, helping you write, express yourself and get things done effortlessly. And it delivers outrageous performance in an exceptionally thin and light design. An entirely new display engine enables stunning precision, colour and brightness. A powerful GPU with hardware-accelerated ray tracing renders game-changing graphics. And the Neural Engine in M4 makes iPad Pro an absolute powerhouse for AI.",
      "performance": {
        "pro_rendering": "Up to 4x faster pro rendering performance than M2",
        "cpu_performance": "Up to 1.5x faster CPU performance than M2"
      }
    },
    "camera": "12MP Wide camera, 4K video recording",
    "camera_features": {
      "rear_camera": "12MP Wide camera with ƒ/1.8 aperture",
      "front_camera": "12MP Ultra Wide camera with Center Stage",
      "video_recording": "4K video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
      "features": "Smart HDR 4, Portrait mode, Portrait Lighting, and Center Stage",
      "pro_camera_system": "Advanced camera system for professional photography"
    },
    "apple_pencil_compatibility": "Apple Pencil Pro",
    "apple_pencil_features": {
      "compatibility": "Apple Pencil Pro",
      "features": "Hover, tilt, and pressure sensitivity, Double-tap to switch tools, Squeeze for quick actions, and Find My integration",
      "hover": "Precise hover detection for enhanced drawing experience",
      "squeeze": "Squeeze gesture for quick tool switching",
      "find_my": "Find My integration for locating lost Apple Pencil"
    },
    "price_inr_starting": "₹99,900",
    "storage_options": ["256GB", "512GB", "1TB", "2TB"],
    "connectivity": {
      "wifi": "Wi-Fi 6E (802.11ax)",
      "cellular": "5G (Cellular models)",
      "bluetooth": "Bluetooth 5.3",
      "usb_c": "USB-C connector with Thunderbolt / USB 4"
    },
    "design": {
      "colors": ["Silver", "Space Black"],
      "materials": "100% recycled aluminum enclosure",
      "thickness": "5.1mm (thinnest Apple product ever)",
      "weight": "444g (11-inch Wi-Fi), 460g (11-inch Cellular), 579g (13-inch Wi-Fi), 595g (13-inch Cellular)",
      "durability": "100% recycled rare earth elements in all magnets"
    },
    "battery": {
      "life": "Up to 10 hours of surfing the web on Wi-Fi or watching video",
      "cellular_life": "Up to 9 hours of surfing the web using cellular data network",
      "charging": "USB-C connector for charging"
    },
    "audio": {
      "speakers": "Four-speaker audio system",
      "microphone": "Studio-quality microphones",
      "headphone_jack": "No 3.5mm headphone jack"
    },
    "security": {
      "face_id": "Face ID for secure authentication and Apple Pay",
      "touch_id": "No Touch ID (uses Face ID instead)"
    },
    "accessories": {
      "magic_keyboard": "Redesigned, thinner Magic Keyboard with comfortable typing and haptic trackpad",
      "smart_keyboard_folio": "Smart Keyboard Folio compatibility",
      "smart_cover": "Smart Cover compatibility"
    },
    "software": {
      "os": "iPadOS",
      "apps": "Access to millions of apps on the App Store",
      "pro_apps": "Professional apps like Final Cut Pro, Logic Pro, and more"
    },
    "feature1": "All-new pro design. Incredibly portable. The thinnest Apple product ever. -- 5.1mm",
    "featuer2" : "Ultra Retina XDR. The world’s most advanced display. Extreme brightness and precise contrast.",
    "feature3" : "Apple M4 chip is built for Apple Intelligence with outrageous performance and game-changing graphics.",
    "feature4" : "Crush pro workflows with the ease of iPadOS and amazing apps.",
    "feature5" : "Redesigned, thinner Magic Keyboard.Comfortable typing and haptic trackpad experience.1 ",
    "feature6" : "The all-new iPad Pro packs astonishing power into an unbelievably thin, light and portable design. Push the limits of what’s possible on iPad with a super-portable 11″ iPad Pro and an expansive 13″ iPad Pro that is the thinnest product Apple has ever created.",
    "feature7": "iPad Pro combines next‑level performance with an ultra-sleek design so you can do your best work anywhere you go. The 13″ iPad Pro is nearly around 100 grams lighter than the previous generation, giving you unmatched capability and portability.",
    "feature8" :"iPad Pro comes in two great finishes — Silver and new Space Black. The durable design is made of 100% recycled aluminium in the enclosure.",
    "feature9" : "Two models, iPad Pro, Space black, back exterior, iPad Pro, silver, back exterior, Pro Camera SystemiPad Pro includes 100% recycled rare earth elements in all magnets."
  },
  "iPad Air (M3)": {
    "release_date": "March 12, 2025",
    "display": "Liquid Retina display with True Tone and P3 wide color",
    "display_specs": {
      "resolution": "2360 x 1640 pixels (11-inch), 2732 x 2048 pixels (13-inch)",
      "brightness": "500 nits",
      "true_tone": "for comfortable viewing",
      "color_gamut": "P3 wide color",
      "refresh_rate": "60Hz"
    },
    "sizes": ["11-inch", "13-inch"],
    "chip": "Apple M3 chip",
    "chip_details": {
      "description": "The Apple M3 chip brings incredible performance to iPad Air. Built with a 3-nanometer process, it features an 8-core CPU with 4 performance cores and 4 efficiency cores, a 10-core GPU, and a 16-core Neural Engine. This delivers up to 50% faster performance than the previous generation.",
      "performance": {
        "cpu_cores": "8-core CPU (4 performance + 4 efficiency)",
        "gpu_cores": "10-core GPU",
        "neural_engine": "16-core Neural Engine",
        "performance_improvement": "Up to 50% faster than previous generation"
      }
    },
    "camera": "12MP Wide camera with 4K video recording",
    "camera_features": {
      "rear_camera": "12MP Wide camera with ƒ/1.8 aperture",
      "front_camera": "12MP Ultra Wide camera with Center Stage",
      "video_recording": "4K video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
      "features": "Smart HDR 4, Portrait mode, Portrait Lighting, and Center Stage"
    },
    "apple_pencil_compatibility": "Apple Pencil Pro",
    "apple_pencil_features": {
      "compatibility": "Apple Pencil Pro",
      "features": "Hover, tilt, and pressure sensitivity, Double-tap to switch tools, Squeeze for quick actions, and Find My integration"
    },
    "price_inr_starting": "₹59,900",
    "storage_options": ["128GB", "256GB", "512GB", "1TB"],
    "connectivity": {
      "wifi": "Wi-Fi 6E (802.11ax)",
      "cellular": "5G (Cellular models)",
      "bluetooth": "Bluetooth 5.3"
    },
    "design": {
      "colors": ["Blue", "Purple", "Pink", "Starlight", "Space Gray"],
      "materials": "100% recycled aluminum enclosure",
      "thickness": "6.1mm",
      "weight": "462g (11-inch Wi-Fi), 470g (11-inch Cellular), 617g (13-inch Wi-Fi), 625g (13-inch Cellular)"
    },
    "battery": {
      "life": "Up to 10 hours of surfing the web on Wi-Fi or watching video",
      "cellular_life": "Up to 9 hours of surfing the web using cellular data network",
      "charging": "USB-C connector for charging"
    },
    "audio": {
      "speakers": "Landscape stereo speakers",
      "microphone": "Dual microphones",
      "headphone_jack": "No 3.5mm headphone jack"
    },
    "security": {
      "touch_id": "Touch ID built into the top button",
      "face_id": "No Face ID (uses Touch ID instead)"
    },
    "accessories": {
      "magic_keyboard": "Magic Keyboard compatibility",
      "smart_keyboard_folio": "Smart Keyboard Folio compatibility",
      "smart_cover": "Smart Cover compatibility"
    },
    "software": {
      "os": "iPadOS",
      "apps": "Access to millions of apps on the App Store",
      "productivity": "Powerful productivity and creativity features"
    },
    "features": {
      "feature1": "Powerful M3 chip for incredible performance and efficiency",
      "feature2": "Liquid Retina display with True Tone and P3 wide color for stunning visuals",
      "feature3": "12MP Wide camera and 12MP Ultra Wide front camera with Center Stage",
      "feature4": "Apple Pencil Pro support with advanced features like Hover and Squeeze",
      "feature5": "All-day battery life up to 10 hours",
      "feature6": "Available in two sizes: 11-inch and 13-inch",
      "feature7": "5G connectivity for fast downloads and streaming",
      "feature8": "USB-C connector for versatile connectivity",
      "feature9": "iPadOS with powerful productivity and creativity features"
    }
  },
  "iPad (11th generation)": {
    "release_date": "March 12, 2025",
    "display": "Liquid Retina display with True Tone",
    "display_specs": {
      "resolution": "2360 x 1640 pixels",
      "brightness": "500 nits",
      "true_tone": "for comfortable viewing",
      "color_gamut": "sRGB",
      "refresh_rate": "60Hz"
    },
    "sizes": ["10.9-inch"],
    "chip": "A16 Bionic chip",
    "chip_details": {
      "description": "The A16 Bionic chip powers the iPad with incredible performance and efficiency. Built with a 4-nanometer process, it features a 6-core CPU with 2 performance cores and 4 efficiency cores, a 5-core GPU, and a 16-core Neural Engine.",
      "performance": {
        "cpu_cores": "6-core CPU (2 performance + 4 efficiency)",
        "gpu_cores": "5-core GPU",
        "neural_engine": "16-core Neural Engine",
        "process": "4-nanometer process"
      }
    },
    "camera": "12MP Wide camera with 4K video recording",
    "camera_features": {
      "rear_camera": "12MP Wide camera with ƒ/1.8 aperture",
      "front_camera": "12MP Ultra Wide camera with Center Stage",
      "video_recording": "4K video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
      "features": "Smart HDR 4, Portrait mode, Portrait Lighting, and Center Stage"
    },
    "apple_pencil_compatibility": "Apple Pencil (USB-C)",
    "apple_pencil_features": {
      "compatibility": "Apple Pencil (USB-C)",
      "features": "Tilt and pressure sensitivity, Magnetic attachment and charging, and Find My integration"
    },
    "price_inr_starting": "₹39,900",
    "storage_options": ["64GB", "128GB", "256GB"],
    "connectivity": {
      "wifi": "Wi-Fi 6 (802.11ax)",
      "cellular": "5G (Cellular models)",
      "bluetooth": "Bluetooth 5.3"
    },
    "design": {
      "colors": ["Blue", "Pink", "Yellow", "Silver", "Space Gray"],
      "materials": "100% recycled aluminum enclosure",
      "thickness": "7.4mm",
      "weight": "481g (Wi-Fi), 487g (Cellular)"
    },
    "battery": {
      "life": "Up to 10 hours of surfing the web on Wi-Fi or watching video",
      "cellular_life": "Up to 9 hours of surfing the web using cellular data network",
      "charging": "USB-C connector for charging"
    },
    "audio": {
      "speakers": "Landscape stereo speakers",
      "microphone": "Dual microphones",
      "headphone_jack": "No 3.5mm headphone jack"
    },
    "security": {
      "touch_id": "Touch ID built into the top button",
      "face_id": "No Face ID (uses Touch ID instead)"
    },
    "accessories": {
      "magic_keyboard": "Magic Keyboard compatibility",
      "smart_keyboard_folio": "Smart Keyboard Folio compatibility",
      "smart_cover": "Smart Cover compatibility"
    },
    "software": {
      "os": "iPadOS",
      "apps": "Access to millions of apps on the App Store",
      "productivity": "Powerful productivity and creativity features"
    },
    "features": {
      "feature1": "A16 Bionic chip for powerful performance and efficiency",
      "feature2": "10.9-inch Liquid Retina display with True Tone for stunning visuals",
      "feature3": "12MP Wide camera and 12MP Ultra Wide front camera with Center Stage",
      "feature4": "Apple Pencil (USB-C) support for creative work",
      "feature5": "All-day battery life up to 10 hours",
      "feature6": "5G connectivity for fast downloads and streaming",
      "feature7": "USB-C connector for versatile connectivity",
      "feature8": "iPadOS with powerful productivity and creativity features",
      "feature9": "Perfect for everyday tasks, creativity, and entertainment"
    }
  },
  "iPad mini (A17 Pro)": {
    "release_date": "October 23, 2024",
    "display": "Liquid Retina display with True Tone and P3 wide color",
    "display_specs": {
      "resolution": "2266 x 1488 pixels",
      "brightness": "500 nits",
      "true_tone": "for comfortable viewing",
      "color_gamut": "P3 wide color",
      "refresh_rate": "60Hz"
    },
    "sizes": ["8.3-inch"],
    "chip": "A17 Pro chip",
    "chip_details": {
      "description": "The A17 Pro chip delivers incredible performance in the compact iPad mini. Built with a 3-nanometer process, it features a 6-core CPU with 2 performance cores and 4 efficiency cores, a 6-core GPU, and a 16-core Neural Engine with 35% faster performance than the previous generation.",
      "performance": {
        "cpu_cores": "6-core CPU (2 performance + 4 efficiency)",
        "gpu_cores": "6-core GPU",
        "neural_engine": "16-core Neural Engine",
        "process": "3-nanometer process",
        "performance_improvement": "35% faster than previous generation"
      }
    },
    "camera": "12MP Wide camera with 4K video recording",
    "camera_features": {
      "rear_camera": "12MP Wide camera with ƒ/1.8 aperture",
      "front_camera": "12MP Ultra Wide camera with Center Stage",
      "video_recording": "4K video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
      "features": "Smart HDR 4, Portrait mode, Portrait Lighting, and Center Stage"
    },
    "apple_pencil_compatibility": "Apple Pencil (USB-C)",
    "apple_pencil_features": {
      "compatibility": "Apple Pencil (USB-C)",
      "features": "Tilt and pressure sensitivity, Magnetic attachment and charging, and Find My integration"
    },
    "price_inr_starting": "₹49,900",
    "storage_options": ["64GB", "128GB", "256GB", "512GB"],
    "connectivity": {
      "wifi": "Wi-Fi 6E (802.11ax)",
      "cellular": "5G (Cellular models)",
      "bluetooth": "Bluetooth 5.3"
    },
    "design": {
      "colors": ["Purple", "Pink", "Starlight", "Space Gray"],
      "materials": "100% recycled aluminum enclosure",
      "thickness": "6.3mm",
      "weight": "293g (Wi-Fi), 297g (Cellular)"
    },
    "battery": {
      "life": "Up to 10 hours of surfing the web on Wi-Fi or watching video",
      "cellular_life": "Up to 9 hours of surfing the web using cellular data network",
      "charging": "USB-C connector for charging"
    },
    "audio": {
      "speakers": "Landscape stereo speakers",
      "microphone": "Dual microphones",
      "headphone_jack": "No 3.5mm headphone jack"
    },
    "security": {
      "touch_id": "Touch ID built into the top button",
      "face_id": "No Face ID (uses Touch ID instead)"
    },
    "accessories": {
      "magic_keyboard": "Magic Keyboard compatibility",
      "smart_keyboard_folio": "Smart Keyboard Folio compatibility",
      "smart_cover": "Smart Cover compatibility"
    },
    "software": {
      "os": "iPadOS",
      "apps": "Access to millions of apps on the App Store",
      "productivity": "Powerful productivity and creativity features"
    },
    "features": {
      "feature1": "A17 Pro chip for incredible performance in a compact design",
      "feature2": "8.3-inch Liquid Retina display with True Tone and P3 wide color",
      "feature3": "12MP Wide camera and 12MP Ultra Wide front camera with Center Stage",
      "feature4": "Apple Pencil (USB-C) support for creative work",
      "feature5": "All-day battery life up to 10 hours",
      "feature6": "5G connectivity for fast downloads and streaming",
      "feature7": "USB-C connector for versatile connectivity",
      "feature8": "iPadOS with powerful productivity and creativity features",
      "feature9": "Perfect portable size for reading, gaming, and creativity on the go"
    }
  }
}


model = genai.GenerativeModel("gemini-2.5-flash") 

def get_gemini_response(question, knowledge_base):    
    context = ""
    query_lower = question.lower()

    mentioned_ipads = [ipad for ipad in knowledge_base if ipad.split(' ')[1].lower() in query_lower]
    
    if mentioned_ipads:
        context_data = {ipad: knowledge_base[ipad] for ipad in mentioned_ipads}
        context = json.dumps(context_data, indent=2)
    else:
        context = json.dumps(knowledge_base, indent=2)


    prompt = f"""
    You are a helpful and friendly expert on Apple iPads. Your task is to answer the user's question based *only* on the provided data context.
    Do not use any external knowledge. If the answer cannot be found in the context, clearly state that.
    Be conversational and format your response in a clear, easy-to-read way.

    --- DATA CONTEXT ---
    {context}
    --------------------

    USER'S QUESTION: "{question}"

    ANSWER:
    """
    
   
    response = model.generate_content(prompt, stream=True)
    

    def text_generator():
        for chunk in response:
            if chunk.text:
                yield chunk.text
    
    return text_generator()



st.set_page_config(page_title="iPad Q&A Bot")
st.header("iPad Chatbot")
st.write("Ask me anything about the latest iPad models!")


input_text = st.text_input("For example: 'Compare the chips in the iPad Pro and iPad Air'", key="input")
submit_button = st.button("Ask the question")


if submit_button and input_text:
    response_stream = get_gemini_response(input_text, KNOWLEDGE_BASE)
    st.subheader("The Response is")
    st.write_stream(response_stream)
