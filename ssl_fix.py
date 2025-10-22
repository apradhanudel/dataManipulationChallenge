#!/usr/bin/env python3
"""
SSL Certificate Fix for macOS
Run this script to fix SSL certificate issues when downloading data
"""

import ssl
import urllib.request
import pandas as pd

# Create unverified SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Monkey patch urllib to use our SSL context
urllib.request.install_opener(
    urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ssl_context)
    )
)

print("✅ SSL context configured for unverified connections")
print("⚠️  Note: This bypasses SSL verification for development purposes only")

# Test the fix
try:
    print("\n🔄 Testing data download...")
    shipments_df = pd.read_csv(
        "https://raw.githubusercontent.com/flyaflya/persuasive/main/shipments.csv", 
        parse_dates=['plannedShipDate', 'actualShipDate']
    )
    print(f"✅ Successfully loaded shipments data: {shipments_df.shape}")
    
    product_line_df = pd.read_csv(
        "https://raw.githubusercontent.com/flyaflya/persuasive/main/productLine.csv"
    )
    print(f"✅ Successfully loaded product line data: {product_line_df.shape}")
    
except Exception as e:
    print(f"❌ Error: {e}")
