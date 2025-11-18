from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Trang chủ - Tool Vua Tốc Độ"""
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tool Vua Tốc Độ - Ares Bot AI</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            :root {
                --primary: #ff3366;
                --secondary: #ffcc00;
                --accent: #00d4ff;
                --success: #00ff9d;
                --dark: #0a0e27;
                --dark-light: #151b3d;
                --text: #e8e8e8;
                --text-dim: #a0a0a0;
            }

            body {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #0a0e27 0%, #1a1f4d 50%, #0f1535 100%);
                color: var(--text);
                line-height: 1.6;
                overflow-x: hidden;
            }

            /* ANIMATED BACKGROUND */
            .bg-animation {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                overflow: hidden;
            }

            .bg-animation::before {
                content: '';
                position: absolute;
                width: 200%;
                height: 200%;
                background: 
                    radial-gradient(circle at 20% 50%, rgba(255, 51, 102, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 40% 20%, rgba(255, 204, 0, 0.1) 0%, transparent 50%);
                animation: bgMove 20s ease-in-out infinite;
            }

            @keyframes bgMove {
                0%, 100% { transform: translate(0, 0) rotate(0deg); }
                50% { transform: translate(-50px, -50px) rotate(180deg); }
            }

            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 40px 20px;
                position: relative;
                z-index: 1;
            }

            /* HEADER */
            .header {
                text-align: center;
                margin-bottom: 60px;
            }

            .logo {
                font-family: 'Orbitron', sans-serif;
                font-size: 72px;
                font-weight: 900;
                background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 15px;
                letter-spacing: 3px;
                animation: glow 3s ease-in-out infinite;
            }

            @keyframes glow {
                0%, 100% { filter: brightness(1); }
                50% { filter: brightness(1.3); }
            }

            .tagline {
                font-family: 'Orbitron', sans-serif;
                font-size: 20px;
                color: var(--accent);
                text-transform: uppercase;
                letter-spacing: 4px;
                margin-bottom: 10px;
            }

            .subtitle {
                font-size: 16px;
                color: var(--text-dim);
                margin-top: 10px;
            }

            /* QUICK LINKS */
            .quick-links {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin: 30px 0;
                flex-wrap: wrap;
            }

            .quick-link {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                border: 2px solid rgba(255, 255, 255, 0.1);
                padding: 12px 25px;
                border-radius: 12px;
                text-decoration: none;
                color: var(--text);
                font-weight: 600;
                font-size: 14px;
                transition: all 0.3s ease;
            }

            .quick-link:hover {
                transform: translateY(-3px);
                background: rgba(255, 255, 255, 0.1);
                border-color: var(--primary);
                box-shadow: 0 10px 30px rgba(255, 51, 102, 0.3);
            }

            .quick-link.old-tool {
                border-color: var(--secondary);
            }

            .quick-link.old-tool:hover {
                border-color: var(--secondary);
                box-shadow: 0 10px 30px rgba(255, 204, 0, 0.3);
            }

            /* CARD */
            .card {
                background: rgba(21, 27, 61, 0.6);
                backdrop-filter: blur(20px);
                border-radius: 25px;
                padding: 40px;
                margin-bottom: 30px;
                border: 2px solid rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease;
            }

            .card:hover {
                border-color: rgba(255, 51, 102, 0.3);
                box-shadow: 0 20px 60px rgba(255, 51, 102, 0.2);
            }

            .card-title {
                font-family: 'Orbitron', sans-serif;
                font-size: 28px;
                color: var(--primary);
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                gap: 12px;
            }

            .step-number {
                background: linear-gradient(135deg, var(--success), var(--accent));
                color: white;
                width: 45px;
                height: 45px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 900;
                font-size: 20px;
                flex-shrink: 0;
            }

            .step-title {
                font-family: 'Orbitron', sans-serif;
                font-size: 22px;
                color: var(--success);
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 15px;
            }

            .section-text {
                color: var(--text);
                font-size: 16px;
                line-height: 1.8;
                margin-bottom: 15px;
            }

            /* CODE BLOCK */
            .code-block {
                background: #0a0e1a;
                border-radius: 12px;
                padding: 20px;
                margin: 15px 0;
                position: relative;
                border: 1px solid rgba(0, 255, 157, 0.3);
                overflow-x: auto;
            }

            .code-block pre {
                color: var(--success);
                font-family: 'Courier New', monospace;
                font-size: 14px;
                white-space: pre-wrap;
                word-wrap: break-word;
            }

            .copy-btn {
                position: absolute;
                top: 10px;
                right: 10px;
                background: var(--success);
                color: #000;
                border: none;
                padding: 8px 18px;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 700;
                font-size: 13px;
                transition: all 0.3s ease;
                font-family: 'Orbitron', sans-serif;
            }

            .copy-btn:hover {
                background: #00d97e;
                transform: scale(1.05);
            }

            /* WARNING & ERROR BOX */
            .warning-box {
                background: rgba(255, 204, 0, 0.1);
                border-left: 5px solid var(--secondary);
                padding: 20px;
                border-radius: 12px;
                margin: 20px 0;
                border: 1px solid rgba(255, 204, 0, 0.3);
            }

            .warning-box strong {
                color: var(--secondary);
            }

            .error-box {
                background: rgba(255, 51, 102, 0.1);
                border-left: 5px solid var(--primary);
                padding: 25px;
                border-radius: 12px;
                margin: 25px 0;
                border: 1px solid rgba(255, 51, 102, 0.3);
            }

            .error-title {
                color: var(--primary);
                font-weight: 900;
                font-size: 18px;
                margin-bottom: 12px;
                font-family: 'Orbitron', sans-serif;
            }

            .error-text {
                color: var(--text);
                margin-bottom: 15px;
                line-height: 1.8;
            }

            /* DOWNLOAD BTN */
            .download-section {
                text-align: center;
                margin: 50px 0;
                padding: 50px 30px;
                background: linear-gradient(135deg, rgba(255, 51, 102, 0.1), rgba(0, 212, 255, 0.1));
                border-radius: 25px;
                border: 2px solid rgba(255, 51, 102, 0.3);
            }

            .download-btn {
                display: inline-block;
                background: linear-gradient(135deg, var(--accent), #0099ff);
                color: white;
                padding: 18px 50px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 800;
                font-size: 18px;
                margin: 15px 10px;
                transition: all 0.3s ease;
                font-family: 'Orbitron', sans-serif;
                text-transform: uppercase;
                box-shadow: 0 10px 40px rgba(0, 212, 255, 0.4);
            }

            .download-btn:hover {
                transform: translateY(-5px) scale(1.05);
                box-shadow: 0 20px 60px rgba(0, 212, 255, 0.6);
            }

            /* PRICING */
            .pricing-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin: 40px 0;
            }

            .pricing-card {
                background: rgba(21, 27, 61, 0.6);
                backdrop-filter: blur(20px);
                border-radius: 25px;
                padding: 40px 30px;
                border: 2px solid rgba(255, 255, 255, 0.1);
                transition: all 0.4s ease;
                position: relative;
                overflow: hidden;
            }

            .pricing-card:hover {
                transform: translateY(-10px);
                border-color: var(--primary);
                box-shadow: 0 25px 70px rgba(255, 51, 102, 0.3);
            }

            .pricing-card.vip {
                border-color: var(--primary);
                background: linear-gradient(135deg, rgba(255, 51, 102, 0.1), rgba(255, 204, 0, 0.1));
            }

            .pricing-card.vip::after {
                content: '🔥 HOT';
                position: absolute;
                top: 20px;
                right: -30px;
                background: var(--primary);
                color: white;
                padding: 5px 40px;
                font-size: 12px;
                font-weight: 900;
                transform: rotate(45deg);
                font-family: 'Orbitron', sans-serif;
            }

            .pricing-name {
                font-family: 'Orbitron', sans-serif;
                font-size: 26px;
                font-weight: 900;
                margin-bottom: 10px;
                text-align: center;
                text-transform: uppercase;
            }

            .pricing-card.free .pricing-name {
                color: var(--text-dim);
            }

            .pricing-card.vip .pricing-name {
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .pricing-price {
                font-family: 'Orbitron', sans-serif;
                font-size: 48px;
                font-weight: 900;
                margin: 15px 0;
                text-align: center;
            }

            .pricing-card.free .pricing-price {
                color: var(--text-dim);
            }

            .pricing-card.vip .pricing-price {
                color: var(--primary);
            }

            .pricing-features {
                list-style: none;
                margin: 30px 0;
            }

            .pricing-features li {
                padding: 12px 0;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                display: flex;
                align-items: flex-start;
                gap: 12px;
                font-size: 15px;
            }

            .pricing-features li::before {
                content: '✓';
                color: var(--accent);
                font-size: 18px;
                font-weight: 900;
                flex-shrink: 0;
            }

            .pricing-features li.disabled {
                color: var(--text-dim);
                text-decoration: line-through;
                opacity: 0.5;
            }

            .pricing-features li.disabled::before {
                content: '✗';
                color: #666;
            }

            .pricing-btn {
                display: block;
                text-align: center;
                padding: 15px 30px;
                border-radius: 15px;
                text-decoration: none;
                font-weight: 700;
                font-size: 16px;
                margin-top: 25px;
                transition: all 0.3s ease;
                font-family: 'Orbitron', sans-serif;
                text-transform: uppercase;
            }

            .pricing-card.free .pricing-btn {
                background: rgba(255, 255, 255, 0.1);
                color: var(--text);
                border: 2px solid rgba(255, 255, 255, 0.2);
            }

            .pricing-card.vip .pricing-btn {
                background: linear-gradient(135deg, var(--primary), #ff0844);
                color: white;
                box-shadow: 0 10px 30px rgba(255, 51, 102, 0.4);
            }

            .pricing-card.vip .pricing-btn:hover {
                transform: scale(1.08);
                box-shadow: 0 15px 45px rgba(255, 51, 102, 0.6);
            }

            /* SOCIAL */
            .social-section {
                text-align: center;
                margin: 50px 0;
                padding: 40px;
                background: rgba(21, 27, 61, 0.6);
                backdrop-filter: blur(20px);
                border-radius: 25px;
                border: 2px solid rgba(255, 255, 255, 0.1);
            }

            .social-section h2 {
                font-family: 'Orbitron', sans-serif;
                font-size: 32px;
                color: var(--primary);
                margin-bottom: 30px;
            }

            .social-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }

            .social-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                padding: 15px 25px;
                border-radius: 15px;
                text-decoration: none;
                font-weight: 700;
                font-size: 16px;
                transition: all 0.3s ease;
                border: 2px solid rgba(255, 255, 255, 0.1);
            }

            .social-btn:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
            }

            .social-btn.zalo {
                background: linear-gradient(135deg, #0068ff, #0099ff);
                color: white;
            }

            .social-btn.telegram {
                background: linear-gradient(135deg, #0088cc, #00aaff);
                color: white;
            }

            .social-btn.tiktok {
                background: linear-gradient(135deg, #000000, #333333);
                color: white;
            }

            .social-btn.youtube {
                background: linear-gradient(135deg, #ff0000, #cc0000);
                color: white;
            }

            .social-btn.group-zalo {
                background: linear-gradient(135deg, #0068ff, #4da6ff);
                color: white;
            }

            /* FOOTER */
            .footer {
                text-align: center;
                margin-top: 60px;
                padding-top: 40px;
                border-top: 2px solid rgba(255, 255, 255, 0.1);
                color: var(--text-dim);
            }

            /* RESPONSIVE */
            @media (max-width: 768px) {
                .logo { font-size: 48px; }
                .tagline { font-size: 16px; }
                .card { padding: 25px; }
                .pricing-grid, .social-grid { grid-template-columns: 1fr; }
            }
        </style>
    </head>
    <body>
        <div class="bg-animation"></div>
        
        <div class="container">
            <!-- HEADER -->
            <div class="header">
                <div class="logo">VUA TỐC ĐỘ</div>
                <div class="tagline">⚡ ARES AI BOT ⚡</div>
                <p class="subtitle">Sprint Run Bot - Phân tích AI siêu tốc, Quản lý vốn thông minh</p>
                
                <div class="quick-links">
                    <a href="https://areskey.vercel.app" target="_blank" class="quick-link old-tool">🛡️ Tool Vua Thoát Hiểm</a>
                    <a href="#download" class="quick-link">📥 Tải Tool</a>
                    <a href="#guide" class="quick-link">📖 Hướng Dẫn</a>
                    <a href="#pricing" class="quick-link">💎 Bảng Giá</a>
                    <a href="#contact" class="quick-link">📞 Liên Hệ</a>
                </div>
            </div>

            <!-- DOWNLOAD -->
            <div class="download-section" id="download">
                <h2 style="font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--accent); margin-bottom: 20px;">
                    📥 TẢI TOOL VUA TỐC ĐỘ
                </h2>
                <p style="font-size: 16px; margin-bottom: 30px;">
                    Click để tải ngay phiên bản mới nhất!
                </p>
                <a href="https://raw.githubusercontent.com/quocdung1303/toolares/main/toolares.py" class="download-btn" download>
                    ⚡ TẢI NGAY
                </a>
            </div>

            <!-- GUIDE -->
            <div class="card" id="guide">
                <h2 class="card-title">📖 Hướng dẫn chi tiết cài đặt Tool Ares</h2>

                <!-- BƯỚC 1: TERMUX -->
                <div style="margin-top: 30px;">
                    <div class="step-title">
                        <span class="step-number">1</span>
                        Termux là gì?
                    </div>
                    <p class="section-text">
                        <strong>Termux</strong> là ứng dụng mô phỏng terminal Linux trên Android. 
                        Nó cho phép bạn sử dụng các công cụ dòng lệnh Linux trên điện thoại.
                    </p>
                </div>

                <!-- BƯỚC 2: CÀI TERMUX -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">2</span>
                        Cài đặt Termux
                    </div>
                    <p class="section-text">
                        Tải Termux từ <strong>F-Droid</strong> (không dùng Google Play Store vì không được cập nhật):
                        <br>
                        <a href="https://f-droid.org/en/packages/com.termux/" style="color: var(--accent); font-weight: 700;" target="_blank">
                            👉 Tải Termux từ F-Droid
                        </a>
                    </p>
                    <p class="section-text" style="margin-top: 15px;">
                        Sau khi cài đặt, mở Termux và chờ khởi động xong.
                    </p>
                </div>

                <!-- BƯỚC 3: CẬP NHẬT HỆ THỐNG -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">3</span>
                        Cập nhật các gói hệ thống
                    </div>
                    <p class="section-text">Chạy lệnh sau trong Termux:</p>
                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pkg update')">Copy</button>
                        <pre>pkg update</pre>
                    </div>
                    <p class="section-text" style="margin-top: 10px;">
                        Nếu có yêu cầu xác nhận, nhấn <strong>Y</strong> và Enter.
                    </p>

                    <p class="section-text" style="margin-top: 20px; color: var(--success); font-weight: 700;">
                        Cài đặt Python và pip:
                    </p>
                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pkg install python')">Copy</button>
                        <pre>pkg install python</pre>
                    </div>
                </div>

                <!-- BƯỚC 4: CÀI THƯ VIỆN -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">4</span>
                        Cài đặt các thư viện Python
                    </div>
                    <p class="section-text">Chạy từng lệnh sau (từng cái một):</p>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install requests')">Copy</button>
                        <pre>pip install requests</pre>
                    </div>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install beautifulsoup4')">Copy</button>
                        <pre>pip install beautifulsoup4</pre>
                    </div>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install colorama')">Copy</button>
                        <pre>pip install colorama</pre>
                    </div>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install websocket-client')">Copy</button>
                        <pre>pip install websocket-client</pre>
                    </div>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install pysocks')">Copy</button>
                        <pre>pip install pysocks</pre>
                    </div>

                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pip install rich')">Copy</button>
                        <pre>pip install rich</pre>
                    </div>
                </div>

                <!-- BƯỚC 5: TẢI TOOL -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">5</span>
                        Tải tool ARES
                    </div>
                    
                    <p class="section-text" style="color: var(--success); font-weight: 700;">
                        1. Cài đặt curl:
                    </p>
                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'pkg install curl')">Copy</button>
                        <pre>pkg install curl</pre>
                    </div>

                    <p class="section-text" style="margin-top: 25px; color: var(--success); font-weight: 700;">
                        2. Tải file tool:
                    </p>
                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'curl -o toolares.py https://raw.githubusercontent.com/quocdung1303/toolares/main/toolares.py')">Copy</button>
                        <pre>curl -o toolares.py https://raw.githubusercontent.com/quocdung1303/toolares/main/toolares.py</pre>
                    </div>

                    <div class="warning-box">
                        <strong>💡 Lưu ý:</strong> Nếu gửi file qua Zalo, đổi đuôi thành <strong>.txt</strong> để tránh lỗi. Sau khi tải về, đổi lại thành <strong>.py</strong>
                    </div>
                </div>

                <!-- BƯỚC 6: CHẠY TOOL -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">6</span>
                        Cách chạy tool
                    </div>
                    <p class="section-text">Sau khi tải file thành công, chạy lệnh:</p>
                    <div class="code-block">
                        <button class="copy-btn" onclick="copyCode(this, 'python toolares.py')">Copy</button>
                        <pre>python toolares.py</pre>
                    </div>
                    <p class="section-text" style="margin-top: 15px; color: var(--success);">
                        ✅ Nếu mọi thứ đúng, tool sẽ bắt đầu chạy!
                    </p>
                </div>

                <!-- LỖI THƯỜNG GẶP -->
                <div style="margin-top: 50px;">
                    <div class="step-title">
                        <span class="step-number">⚠️</span>
                        Lỗi thường gặp và cách khắc phục
                    </div>

                    <!-- LỖI 1 -->
                    <div class="error-box">
                        <div class="error-title">Lỗi 1: command not found: curl</div>
                        <p class="error-text">
                            Lỗi này xảy ra khi 'curl' chưa được cài đặt trong Termux.
                        </p>
                        <p class="error-text" style="color: var(--success); font-weight: 700;">
                            Cách khắc phục:
                        </p>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this, 'pkg install curl')">Copy</button>
                            <pre>pkg install curl</pre>
                        </div>
                    </div>

                    <!-- LỖI 2 -->
                    <div class="error-box">
                        <div class="error-title">Lỗi 2: No module named 'requests'</div>
                        <p class="error-text">
                            Lỗi này xảy ra khi một trong các thư viện chưa được cài đặt thành công.
                        </p>
                        <p class="error-text" style="color: var(--success); font-weight: 700;">
                            Cách khắc phục: Chạy lại từng lệnh cài thư viện ở bước 4
                        </p>
                    </div>

                    <!-- LỖI 3 -->
                    <div class="error-box">
                        <div class="error-title">Lỗi 3: Permission denied</div>
                        <p class="error-text">
                            Lỗi này xảy ra khi file không có quyền thực thi.
                        </p>
                        <p class="error-text" style="color: var(--success); font-weight: 700;">
                            Cách khắc phục:
                        </p>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this, 'chmod +x toolares.py')">Copy</button>
                            <pre>chmod +x toolares.py</pre>
                        </div>
                    </div>
                </div>

                <!-- LƯU Ý -->
                <div style="margin-top: 40px;">
                    <div class="step-title">
                        <span class="step-number">7</span>
                        Lưu ý quan trọng
                    </div>
                    <ul style="margin-left: 30px; color: var(--text);">
                        <li style="margin-bottom: 12px;">Luôn cập nhật Termux và Python lên phiên bản mới nhất</li>
                        <li style="margin-bottom: 12px;">Khi có phiên bản tool mới, chỉ cần tải lại file bằng lệnh curl ở bước 5</li>
                        <li style="margin-bottom: 12px;">Nếu gặp lỗi không có trong danh sách, liên hệ admin để được hỗ trợ</li>
                    </ul>
                </div>
            </div>

            <!-- GIỚI THIỆU -->
            <div class="card">
                <h2 class="card-title">🚀 Giới thiệu Tool Vua Tốc Độ</h2>
                <p class="section-text">
                    <strong>Tool Vua Tốc Độ</strong> là phiên bản nâng cấp của Tool Vua Thoát Hiểm, 
                    tập trung vào <strong style="color: var(--primary);">tốc độ xử lý cực nhanh</strong> 
                    và <strong style="color: var(--accent);">AI phân tích thông minh</strong>.
                </p>
                <p class="section-text">
                    ✨ Tự động phân tích xu hướng với AI<br>
                    ⚡ Xử lý siêu nhanh, phản hồi tức thì<br>
                    💎 Quản lý vốn chuyên nghiệp<br>
                    🛡️ Stop-loss & Take-profit tự động
                </p>
            </div>

            <!-- PRICING -->
            <div class="card" id="pricing">
                <h2 class="card-title">💎 So sánh gói Free & VIP</h2>

                <div class="pricing-grid">
                    <div class="pricing-card free">
                        <div class="pricing-name">Free</div>
                        <div class="pricing-price">0đ</div>
                        <p style="color: var(--text-dim); font-size: 14px; text-align: center;">Miễn phí mãi mãi</p>

                        <ul class="pricing-features">
                            <li>Logic cược cơ bản</li>
                            <li>AI Strategy (1-4)</li>
                            <li>Chọn loại cược Winner</li>
                            <li class="disabled">AI phân tích sâu 50+ vòng</li>
                            <li class="disabled">Auto Bet thông minh</li>
                            <li class="disabled">Quản lý vốn Kelly/Martingale</li>
                            <li class="disabled">Stop-loss & Take-profit</li>
                        </ul>

                        <a href="#contact" class="pricing-btn">Nhận Key Free</a>
                    </div>

                    <div class="pricing-card vip">
                        <div class="pricing-name">VIP</div>
                        <div class="pricing-price">💰</div>
                        <p style="color: var(--text-dim); font-size: 14px; text-align: center;">Liên hệ để biết giá</p>

                        <ul class="pricing-features">
                            <li><strong>Tất cả tính năng Free</strong></li>
                            <li>🔥 AI phân tích chuyên sâu 50+ vòng</li>
                            <li>⚡ Auto Bet siêu tốc</li>
                            <li>💎 Quản lý vốn Kelly/Martingale/Fibonacci</li>
                            <li>🛡️ Stop-loss tự động</li>
                            <li>🎯 Take-profit thông minh</li>
                            <li>📊 Thống kê chi tiết</li>
                            <li>🚀 Hỗ trợ VIP 24/7</li>
                        </ul>

                        <a href="#contact" class="pricing-btn">Nâng cấp VIP</a>
                    </div>
                </div>
            </div>

            <!-- CONTACT -->
            <div class="social-section" id="contact">
                <h2>📞 Kết nối với chúng tôi</h2>
                <p style="color: var(--text-dim); margin-bottom: 20px;">
                    Liên hệ để nhận key, hỗ trợ 24/7 và cập nhật tin tức mới nhất!
                </p>

                <div class="social-grid">
                    <a href="https://zalo.me/0767564895" target="_blank" class="social-btn zalo">💬 Zalo Admin</a>
                    <a href="https://t.me/qdungdeptrai" target="_blank" class="social-btn telegram">✈️ Telegram</a>
                    <a href="https://zalo.me/g/rhyrmn931" target="_blank" class="social-btn group-zalo">👥 Group Zalo</a>
                    <a href="https://www.tiktok.com/@xworldhi?_r=1&_t=ZS-91VUc5JFJwO" target="_blank" class="social-btn tiktok">🎵 TikTok</a>
                    <a href="https://youtube.com/@aresstool?si=7eLqLOS8hs_iq234" target="_blank" class="social-btn youtube">▶️ YouTube</a>
                </div>
            </div>

            <!-- FOOTER -->
            <div class="footer">
                <p><strong>© 2025 ARES TOOL - VUA TỐC ĐỘ</strong></p>
                <p>Sprint Run Bot | AI Strategy | VIP + FREE License</p>
                <p style="margin-top: 15px;">
                    <a href="https://areskey.vercel.app" style="color: var(--secondary); text-decoration: none;" target="_blank">🛡️ Tool Vua Thoát Hiểm</a>
                </p>
            </div>
        </div>

        <script>
            function copyCode(button, text) {
                navigator.clipboard.writeText(text).then(function() {
                    const originalText = button.innerText;
                    button.innerText = '✓ Copied!';
                    button.style.background = '#00d97e';
                    
                    setTimeout(function() {
                        button.innerText = originalText;
                        button.style.background = '#00ff9d';
                    }, 2000);
                }).catch(function(err) {
                    alert('Không thể copy!');
                });
            }
        </script>
    </body>
    </html>
    """

@app.route("/huong-dan")
def huong_dan():
    return home()

if __name__ == "__main__":
    app.run(debug=True)
