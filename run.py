#!/usr/bin/env python3
"""
Portfolio Website Runner
Simple script to run the Flask portfolio application
"""

from app import app

if __name__ == '__main__':
    print("🚀 Starting Kashish Chopra's Portfolio Website...")
    print("📱 Website will be available at: http://localhost:5000")
    print("✨ Press Ctrl+C to stop the server")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )