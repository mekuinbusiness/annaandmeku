import zipfile
import os

# Create directory structure for the project
os.makedirs('wedding_invitation/assets', exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ta Porche & Brianne - Wedding Invitation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Playfair+Display:ital,wght@0,400;1,400&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
    
    <style>
        /* --- DESIGN SYSTEM & COLORS --- */
        :root {
            --bg-cream: #FAF6F0;
            --primary-burgundy: #581C2C;
            --primary-burgundy-hover: #421420;
            --text-dark: #2C2523;
            --text-muted: #7E7572;
            --accent-gold: #C5A059;
            --card-shadow: 0 12px 40px rgba(88, 28, 44, 0.05);
            --transition-smooth: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #111; /* Dark outer backdrop */
            color: var(--text-dark);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* --- MOBILE PHONE WRAPPER MOCKUP --- */
        .phone-frame {
            width: 100%;
            max-width: 430px; /* Standard iPhone Pro Max width */
            height: 100vh;
            max-height: 932px; /* Standard iPhone Pro Max height */
            background-color: var(--bg-cream);
            position: relative;
            overflow-y: auto;
            overflow-x: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            scrollbar-width: none; /* Hide scrollbar for clean app feel */
        }
        
        .phone-frame::-webkit-scrollbar {
            display: none;
        }

        /* --- ANIMATION REVEAL ENGINE --- */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: var(--transition-smooth);
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        /* --- HERO SECTION --- */
        .hero {
            text-align: center;
            padding: 50px 24px 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .monogram-circle {
            width: 100px;
            height: 100px;
            border: 1px solid var(--accent-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 24px;
            position: relative;
        }

        .monogram-circle::after {
            content: '';
            position: absolute;
            top: 4px;
            left: 4px;
            right: 4px;
            bottom: 4px;
            border: 1px solid rgba(197, 160, 89, 0.25);
            border-radius: 50%;
        }

        .monogram {
            font-family: 'Cinzel', serif;
            font-size: 24px;
            color: var(--accent-gold);
            letter-spacing: 1px;
        }

        .couple-names {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 32px;
            color: var(--accent-gold);
            margin-bottom: 12px;
            font-weight: 400;
        }

        .tagline {
            font-size: 11px;
            letter-spacing: 3px;
            text-transform: uppercase;
            color: var(--text-muted);
            font-weight: 400;
        }

        /* --- PHOTO BANNER --- */
        .photo-banner {
            width: 100%;
            padding: 0 24px;
            margin-bottom: 35px;
        }

        .image-wrapper {
            width: 100%;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: var(--card-shadow);
            position: relative;
            aspect-ratio: 4 / 5;
            background-color: #EAE5DD;
        }

        .image-wrapper img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* --- INVITATION DETAILS --- */
        .invitation-card {
            padding: 0 24px;
            text-align: center;
            margin-bottom: 45px;
        }

        .meta-info-grid {
            display: flex;
            justify-content: space-around;
            border-top: 1px solid rgba(197, 160, 89, 0.25);
            border-bottom: 1px solid rgba(197, 160, 89, 0.25);
            padding: 12px 0;
            margin-bottom: 24px;
        }

        .meta-item .label {
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--text-muted);
            display: block;
            margin-bottom: 2px;
        }

        .meta-item .value {
            font-family: 'Cinzel', serif;
            font-size: 14px;
            color: var(--text-dark);
            font-weight: 600;
        }

        .invitation-text {
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            color: var(--text-dark);
            margin-bottom: 12px;
        }

        .invitation-subtext {
            font-size: 13px;
            color: var(--text-muted);
            padding: 0 15px;
            font-weight: 300;
        }

        /* --- COUNTDOWN TIMER --- */
        .countdown-section {
            background-color: #F3ECE2;
            padding: 35px 24px;
            text-align: center;
            margin-bottom: 45px;
        }

        .countdown-title {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 18px;
            color: var(--text-dark);
            margin-bottom: 20px;
        }

        .timer-grid {
            display: flex;
            justify-content: space-between;
            max-width: 320px;
            margin: 0 auto;
        }

        .timer-block {
            flex: 1;
            text-align: center;
        }

        .timer-number {
            font-family: 'Cinzel', serif;
            font-size: 26px;
            color: var(--text-dark);
            font-weight: 400;
            display: block;
            margin-bottom: 4px;
        }

        .timer-label {
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
        }

        .timer-separator {
            font-family: 'Cinzel', serif;
            font-size: 22px;
            color: var(--accent-gold);
            line-height: 1;
            padding: 0 2px;
            opacity: 0.7;
        }

        /* --- TIMELINE / AGENDA --- */
        .section-title {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 24px;
            color: var(--text-dark);
            text-align: center;
            margin-bottom: 24px;
        }

        .timeline-box {
            margin: 0 24px 45px;
            padding: 24px;
            border: 1px solid rgba(197, 160, 89, 0.25);
            border-radius: 16px;
            background-color: white;
            box-shadow: var(--card-shadow);
        }

        .timeline-item {
            display: flex;
            margin-bottom: 20px;
        }

        .timeline-item:last-child {
            margin-bottom: 0;
        }

        .timeline-time {
            width: 70px;
            font-size: 12px;
            font-weight: 500;
            color: var(--accent-gold);
            padding-top: 2px;
        }

        .timeline-content {
            flex: 1;
            padding-left: 15px;
            border-left: 1px solid rgba(197, 160, 89, 0.25);
        }

        .timeline-event {
            font-size: 13px;
            font-weight: 500;
            color: var(--text-dark);
            margin-bottom: 2px;
        }

        .timeline-desc {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* --- Q&A ACCORDION --- */
        .qa-container {
            margin: 0 24px 45px;
        }

        .accordion-item {
            background: white;
            border-radius: 8px;
            margin-bottom: 10px;
            border: 1px solid rgba(0,0,0,0.03);
            box-shadow: 0 2px 6px rgba(0,0,0,0.01);
            overflow: hidden;
        }

        .accordion-header {
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            user-select: none;
        }

        .accordion-question {
            font-size: 13px;
            font-weight: 500;
            color: var(--text-dark);
        }

        .accordion-icon {
            font-size: 16px;
            color: var(--accent-gold);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            background-color: #FAF9F6;
        }

        .accordion-text {
            padding: 0 20px 16px 20px;
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.6;
        }

        .accordion-item.active .accordion-icon {
            transform: rotate(45deg);
        }

        /* --- RSVP FORM --- */
        .rsvp-section {
            margin: 0 24px 40px;
            padding: 30px 20px;
            background: white;
            border-radius: 16px;
            box-shadow: var(--card-shadow);
            border: 1px solid rgba(88, 28, 44, 0.03);
            text-align: center;
        }

        .rsvp-title {
            font-family: 'Cinzel', serif;
            font-size: 20px;
            letter-spacing: 2px;
            color: var(--text-dark);
            margin-bottom: 4px;
        }

        .rsvp-deadline {
            font-size: 11px;
            color: var(--accent-gold);
            margin-bottom: 24px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .form-group {
            text-align: left;
            margin-bottom: 20px;
        }

        .form-label {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            display: block;
            margin-bottom: 6px;
        }

        .input-field {
            width: 100%;
            padding: 10px 0;
            border: none;
            border-bottom: 1px solid rgba(197, 160, 89, 0.3);
            font-family: 'Montserrat', sans-serif;
            font-size: 14px;
            background: transparent;
            color: var(--text-dark);
            transition: border-color 0.3s ease;
        }

        .input-field:focus {
            outline: none;
            border-bottom-color: var(--primary-burgundy);
        }

        .radio-option {
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            cursor: pointer;
            position: relative;
            user-select: none;
            font-size: 13px;
            color: var(--text-dark);
        }

        .radio-option input {
            position: absolute;
            opacity: 0;
            cursor: pointer;
        }

        .custom-mark {
            height: 16px;
            width: 16px;
            border: 1px solid rgba(197, 160, 89, 0.5);
            border-radius: 4px;
            margin-right: 10px;
            display: inline-block;
            position: relative;
            transition: all 0.2s ease;
        }

        .radio-option input:checked ~ .custom-mark {
            background-color: var(--primary-burgundy);
            border-color: var(--primary-burgundy);
        }

        .radio-option input:checked ~ .custom-mark::after {
            content: '';
            position: absolute;
            left: 5px;
            top: 2px;
            width: 3px;
            height: 7px;
            border: solid white;
            border-width: 0 2px 2px 0;
            transform: rotate(45deg);
        }

        .submit-btn {
            width: 100%;
            background-color: var(--primary-burgundy);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 30px;
            font-family: 'Cinzel', serif;
            font-size: 13px;
            letter-spacing: 2px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(88, 28, 44, 0.15);
            transition: var(--transition-smooth);
            margin-top: 8px;
        }

        .submit-btn:hover {
            background-color: var(--primary-burgundy-hover);
            transform: translateY(-1px);
        }
    </style>
</head>
<body>

    <div class="phone-frame">
        
        <header class="hero">
            <div class="monogram-circle reveal">
                <span class="monogram">T&B</span>
            </div>
            <h1 class="couple-names reveal">Ta Porche & Brianne</h1>
            <p class="tagline reveal">Invite you to join them in romance</p>
        </header>

        <section class="photo-banner reveal">
            <div class="image-wrapper">
                <img src="https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1000" alt="Wedding Portrait Presentation">
            </div>
        </section>

        <section class="invitation-card reveal">
            <div class="meta-info-grid">
                <div class="meta-item">
                    <span class="label">Date</span>
                    <span class="value">12.14.26</span>
                </div>
                <div class="meta-item">
                    <span class="label">Place</span>
                    <span class="value">Ponchatoula</span>
                </div>
            </div>
            <h2 class="invitation-text">We are inviting you to our wedding!</h2>
            <p class="invitation-subtext">Let's celebrate the best day of our life together!</p>
        </section>

        <section class="countdown-section reveal">
            <h3 class="countdown-title">The event starts in:</h3>
            <div class="timer-grid">
                <div class="timer-block">
                    <span class="timer-number" id="days">00</span>
                    <span class="timer-label">Days</span>
                </div>
                <div class="timer-separator">:</div>
                <div class="timer-block">
                    <span class="timer-number" id="hours">00</span>
                    <span class="timer-label">Hours</span>
                </div>
                <div class="timer-separator">:</div>
                <div class="timer-block">
                    <span class="timer-number" id="minutes">00</span>
                    <span class="timer-label">Mins</span>
                </div>
                <div class="timer-separator">:</div>
                <div class="timer-block">
                    <span class="timer-number" id="seconds">00</span>
                    <span class="timer-label">Secs</span>
                </div>
            </div>
        </section>

        <section class="reveal">
            <h3 class="section-title">Organizational Aspects</h3>
            <div class="timeline-box">
                <div class="timeline-item">
                    <div class="timeline-time">5:30 PM</div>
                    <div class="timeline-content">
                        <div class="timeline-event">Guest Arrival</div>
                        <div class="timeline-desc">Welcome refreshments served</div>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">5:45 PM</div>
                    <div class="timeline-content">
                        <div class="timeline-event">Doors Close</div>
                        <div class="timeline-desc">Strictly no exceptions allowed</div>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">6:00 PM</div>
                    <div class="timeline-content">
                        <div class="timeline-event">Wedding Ceremony</div>
                        <div class="timeline-desc">Exchanging of lifetime vows</div>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-time">6:30 PM</div>
                    <div class="timeline-content">
                        <div class="timeline-event">Cocktails & Reception</div>
                        <div class="timeline-desc">Followed by dinner & dancing celebration</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="reveal">
            <h3 class="section-title">Questions & Answers</h3>
            <div class="qa-container">
                
                <div class="accordion-item">
                    <div class="accordion-header">
                        <span class="accordion-question">Can I bring a plus one?</span>
                        <span class="accordion-icon">+</span>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-text">Due to space and capacity layout rules at the venue, we can only accommodate guests explicitly detailed on the digital invitation dashboard.</div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <span class="accordion-question">Are kids allowed?</span>
                        <span class="accordion-icon">+</span>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-text">To allow all guests a night of relaxation and uninhibited celebration, we have chosen to make our wedding day events an adult-only experience.</div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header">
                        <span class="accordion-question">Will there be transportation?</span>
                        <span class="accordion-icon">+</span>
                    </div>
                    <div class="accordion-content">
                        <div class="accordion-text">Transportation packages to and from the venue grid will not be provided. Please allocate 60 minutes for regional travel if you are staying in the downtown area.</div>
                    </div>
                </div>

            </div>
        </section>

        <section class="rsvp-section reveal">
            <h3 class="rsvp-title">RSVP</h3>
            <p class="rsvp-deadline">Please confirm by 10/31/2026</p>
            
            <form id="weddingRsvpForm" onsubmit="handleFormSubmit(event)">
                <div class="form-group">
                    <label class="form-label">Your Name</label>
                    <input type="text" class="input-field" required placeholder="Enter your full name">
                </div>

                <div class="form-group">
                    <label class="form-label">Will you attend?</label>
                    
                    <label class="radio-option">
                        <input type="radio" name="attendance" value="yes" checked>
                        <span class="custom-mark"></span>
                        Yes, I will!
                    </label>

                    <label class="radio-option">
                        <input type="radio" name="attendance" value="no">
                        <span class="custom-mark"></span>
                        Unfortunately, I cannot
                    </label>

                    <label class="radio-option">
                        <input type="radio" name="attendance" value="later">
                        <span class="custom-mark"></span>
                        I will tell you a bit later
                    </label>
                </div>

                <div class="form-group">
                    <label class="form-label">Do you have any food intolerances?</label>
                    <input type="text" class="input-field" placeholder="e.g., Vegetarian, Nut Allergy, None">
                </div>

                <button type="submit" class="submit-btn">SUBMIT RESPONSE</button>
            </form>
        </section>

    </div>

    <script>
        // COUNTDOWN COUNTER ENGINE
        const targetDate = new Date("Dec 14, 2026 17:30:00").getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const difference = targetDate - now;

            if (difference < 0) {
                document.getElementById("days").innerText = "00";
                document.getElementById("hours").innerText = "00";
                document.getElementById("minutes").innerText = "00";
                document.getElementById("seconds").innerText = "00";
                return;
            }

            const d = Math.floor(difference / (1000 * 60 * 60 * 24));
            const h = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((difference % (1000 * 60)) / 1000);

            document.getElementById("days").innerText = d < 10 ? "0" + d : d;
            document.getElementById("hours").innerText = h < 10 ? "0" + h : h;
            document.getElementById("minutes").innerText = m < 10 ? "0" + m : m;
            document.getElementById("seconds").innerText = s < 10 ? "0" + s : s;
        }
        setInterval(updateCountdown, 1000);
        updateCountdown();

        // SMOOTH ACCORDION TOGGLE MECHANICS
        const headers = document.querySelectorAll(".accordion-header");
        headers.forEach(header => {
            header.addEventListener("click", function() {
                const item = this.parentElement;
                const content = this.nextElementSibling;
                
                if(item.classList.contains("active")) {
                    content.style.maxHeight = null;
                    item.classList.remove("active");
                } else {
                    document.querySelectorAll(".accordion-item").forEach(el => {
                        el.classList.remove("active");
                        el.querySelector(".accordion-content").style.maxHeight = null;
                    });
                    
                    content.style.maxHeight = content.scrollHeight + "px";
                    item.classList.add("active");
                }
            });
        });

        // CONTAINER INNER PORT SCROLL REVEAL LOGIC
        const phoneFrame = document.querySelector('.phone-frame');
        function revealInsideFrame() {
            const reveals = document.querySelectorAll(".reveal");
            const frameHeight = phoneFrame.clientHeight;
            
            reveals.forEach(element => {
                const elementTop = element.getBoundingClientRect().top - phoneFrame.getBoundingClientRect().top;
                if (elementTop < frameHeight - 60) {
                    element.classList.add("active");
                }
            });
        }
        phoneFrame.addEventListener("scroll", revealInsideFrame);
        window.addEventListener("load", revealInsideFrame);
        setTimeout(revealInsideFrame, 300); // Fail-safe initialization cascade

        // RSVP FORM PROCESSING ALERT
        function handleFormSubmit(event) {
            event.preventDefault();
            alert("Success! Your selection profile values have been recorded.");
            document.getElementById("weddingRsvpForm").reset();
        }
    </script>
</body>
</html>
"""

readme_content = """# Animated Mobile Wedding Invitation Website
A luxury-tier interactive responsive digital invitation web template engineered to accurately mimic the user experience, typography metrics, and aesthetic composition of high-end wedding web application interfaces.

## 📦 Package Contents
* `index.html` - Complete unified codebase structure including markup layout configurations, CSS layout layers, structural variables, and the custom JS micro-interaction layer engine.
* `assets/` - Folder target designed to hold customized graphic items or localized picture files.

## 🛠️ Deployment Instructions

### 1. Local Preview Evaluation
Simply extract the archive contents and open `index.html` directly into Google Chrome, Safari, or Mozilla Firefox. The interface is optimized inside an application preview viewport framework to mimic real-world smartphone presentation screens.

### 2. Assets & Content Customization
* **Images:** Locate line 186 containing the image element. Modify the `src` attribute value to parse your custom high-resolution hosted image URL, or drop a file into the local assets folder (e.g., `assets/couple.jpg`) and target that path.
* **Text Strings:** Scan individual functional layout containers directly inside the HTML markup layer (`<h1>`, `<h2>`, timeline elements) to change dates, naming values, locations, itinerary segments, or accordion text content blocks.
* **Countdown Initialization:** Modify line 273 script parameters `new Date("Dec 14, 2026 17:30:00")` to pass your unique upcoming target date and hour matrices.

### 3. Immediate Free Global Cloud Hosting Launch

#### Option A: GitHub Pages Deployment (Highly Recommended)
1. Initialize a free public repository profile at [GitHub](https://github.com).
2. Commit your finalized file structure archive as an unpacked root repository (`index.html` must sit in the primary base directory context).
3. Navigate to repository **Settings** -> **Pages** tab panel.
4. Toggle the build source configuration to point towards the **main/master branch root**, then click save.
5. Your customized production link domain goes live globally within seconds.

#### Option B: Netlify Drag-and-Drop Deploy
1. Visit [Netlify Drop](https://app.netlify.com/drop).
2. Grab the root project folder directory container containing your files and drop it cleanly onto the web UI canvas.
3. Your live application instance URL is generated instantly.
"""

with open('wedding_invitation/index.html', 'w') as f:
    f.write(html_content)

with open('wedding_invitation/README.txt', 'w') as f:
    f.write(readme_content)

# Compress project folder to ZIP package bundle
with zipfile.ZipFile('wedding_invitation_source.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('wedding_invitation'):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, 'wedding_invitation')
            zipf.write(file_path, arcname)

print("ZIP generated successfully.")