#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    #WEB APP CONFIGURATION
    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "8e238ea7-631a-413a-b03d-c93556e296d2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    
    #LUIS APP CONFIGURATION
    LUIS_APP_ID = os.environ.get("LuisAppId","4db15818-bb28-46a9-b231-c9d38a27b515")#pred
    LUIS_API_KEY = os.environ.get("LuisAPIKey","a021d05eb5074cff848a795b98180709")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint","https://flymeap-authoring.cognitiveservices.azure.com/")
    
    #APP INSIGHTS CONFIGURATION 
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "0a404c38-03e3-4d07-a3d0-322e6bff8f05")
